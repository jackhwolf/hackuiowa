import boto3
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
        print(os.environ.get('access'))
        print(os.environ.get('secret'))
        print()
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
        table = self.res.Table(tid)
        resp = table.query(KeyConditionExpression=keycondexpr)
        return resp

    def delete_(self, tid, keytodelete):
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
        try:
            self.put_(
                self.tid,
                item
            )
            return True
        except Exception as e:
            print(e)
            return {'error': str(e)}

    def query(self, keycondexpr, **kw):
        try:
            resp = self.query_(self.tid, keycondexpr)
            return resp
        except Exception as e:
            print(e)
            return {'error': str(e)}

    def delete(self, keytodelete, **kw):
        try:
            resp = self.delete_(self.tid, keytodelete)
            return resp
        except Exception as e:
            print(e)
            return {'error': str(e)}
