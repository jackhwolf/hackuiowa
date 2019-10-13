from time import time
import boto3
from boto3.dynamodb.conditions import Key, Attr, Not
from dotenv import load_dotenv
import os


load_dotenv()

#################
# base db class #
#################

class db:
    ''' subclass to handle db conn - throws errors '''

    def __init__(self):
        ''' get a dynamodb resource '''
        self.res = boto3.resource(
                        'dynamodb',
                        aws_access_key_id=os.environ.get('access'),
                        aws_secret_access_key=os.environ.get('secret'),
                        region_name='us-west-1'
                    )

    def create_(self, tid, key_schema, attribute_defn, **kw):
        ''' create table '''
        self.res.create_table(
            TableName=tid,
            KeySchema=key_schema,
            AttributeDefinitions=attribute_defn,
            ProvisionedThroughput={
                "ReadCapacityUnits": kw.get('RCU', 2),
                "WriteCapacityUnits": kw.get('WCU', 2)
            }
        )

    def put_(self, tid, item):
        ''' put item(s) into table '''
        table = self.res.Table(tid)
        if not issubclass(type(item), list):
            item = [item]
        for i in item:
            table.put_item(Item=i)

    def query_(self, tid, keycondexpr):
        ''' lookup something in table '''
        table = self.res.Table(tid)
        resp = table.query(KeyConditionExpression=keycondexpr)
        return resp

    def delete_(self, tid, keytodelete):
        ''' delete something from table '''
        table = self.res.Table(tid)
        resp = table.delete_item(Key=keytodelete)
        return resp


######################
# class for ddb conn #
######################

class ddbconn(db):
    ''' class to handle connection to user db '''

    def __init__(self, tid, key_schema, attr_defn):
        db.__init__(self)
        self.tid = tid
        self.key_schema = key_schema
        self.attr_defn = attr_defn

    def create(self, **kw):
        ''' create table '''
        try:
            self.create_(
                self.tid,
                self.key_schema,
                self.attr_defn, **kw
            )
            return True
        except Exception as e:
            return {'error': str(e)}

    def put(self, item, **kw):
        ''' put item into table and handle errors '''
        try:
            self.put_(
                self.tid,
                item
            )
            return True
        except Exception as e:
            return {'error': str(e)}

    def query(self, keycondexpr, **kw):
        ''' look up item in table and handle errors '''
        try:
            resp = self.query_(self.tid, keycondexpr)
            return resp
        except Exception as e:
            return {'error': str(e)}

    def delete(self, keytodelete, **kw):
        ''' delete item from table and handle errors '''
        try:
            resp = self.delete_(self.tid, keytodelete)
            return resp
        except Exception as e:
            return {'error': str(e)}

######################
# how we track users #
######################

class userddbconn(ddbconn):
    ''' connect to user db '''

    def __init__(self):
        ''' define table name and schema, init connection '''
        self.tid = 'users-hackuiowa'    # name of table
        self.key_schema = [             # schema for keys
                    {
                        'AttributeName': 'username',
                        'KeyType': 'HASH'
                    },
                    {
                        'AttributeName': 'password',
                        'KeyType': 'RANGE'
                    }
                ]
        self.attr_defn = [              # what types are our keys
                    {
                        'AttributeName': 'username',
                        'AttributeType': 'S'
                    },
                    {
                        'AttributeName': 'password',
                        'AttributeType': 'S'
                    }
                ]
        ddbconn.__init__(self, self.tid, self.key_schema, self.attr_defn)

    def hash__(self, x):
        ''' return hashed version of x '''
        return x

    def fmtentry__(self, **kw):
        '''
        clean up our input into a standard format
        args: username, password, email
        '''
        return {
            'username':    self.hash__(kw.get('username')),
            'password':    self.hash__(kw.get('password')),
            'email':       self.hash__(kw.get('email')),
            'signup-date': str(int(time()))
        }

    def createTable(self, **kw):
        ''' create ourself '''
        return self.create()

    def getUser(self, **kw):
        ''' get a user '''
        return self.query(Key('username').eq(kw.get('username')))

    def doesUserExist(self, **kw):
        '''
        is user in ddb?
        args: username, password
        '''
        u = self.getUser(**kw)
        print(u)
        if u.get('Count', -1) > 0:
            return {'Response': 1, 'meta': u.get('Items')[0]}
        return {'Response': 0}

    def signUpUser(self, **kw):
        '''
        add user to ddb
        args: username, password, email
        '''
        self.put(self.fmtentry__(**kw))
        return {'message': 'user signed up.',
                'meta': {'newuname': kw.get('username')}}

    def logInUser(self, **kw):
        ''' if user exists, send them a cookie '''
        if self.doesUserExist(**kw)['Response'] == 1:
            return {'Result': 1, 'Cookie': 'COOKIE!!!'}
        else:
            return {'Result': 0, 'meta': {'message': 'User does not exist'}}

    def deleteUser(self, **kw):
        '''
        delete user from ddb
        args: username, password
        '''
        self.delete({
                    'username': kw.get('username'),
                    'password': kw.get('password')
                })
        return {'message': 'user deleted.'}
