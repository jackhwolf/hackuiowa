from time import time
from boto3.dynamodb.conditions import Key, Attr, Not
from backend.ddbconn import ddbconn


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
        return self.create()

    def getUser(self, **kw):
        return self.query(Key('username').eq(kw.get('username')))

    def doesUserExist(self, **kw):
        '''
        is user in ddb?
        args: username, password
        '''
        u = self.getUser(**kw)
        print(u)
        if u.get('Count', -1) > 0:
            return u.get('Items')[0]
        return 0

    def signUpUser(self, **kw):
        '''
        add user to ddb
        args: username, password, email
        '''
        self.put(self.fmtentry__(**kw))
        return {'message': 'user signed up.',
                'meta': {'newuname': kw.get('username')}}

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
