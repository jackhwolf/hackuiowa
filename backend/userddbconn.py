from backend.ddbconn import ddbconn
from time import time


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
        conn.__init__(self, self.tid, self.key_schema, self.attr_defn)

    def hash__(self, x):
        return x

    def fmtentry__(self, *args):
        '''
        clean up our input into a standard format
        args: username, password, email
        '''
        return {
            'username':    self.hash__(args[0]),
            'password':    self.hash__(args[1]),
            'email':       self.hash__(args[2]),
            'signup-date': int(time())
        }

    def createTable(self, **kw):
        try:
            self.create_(
                self.tid,
                self.key_schema,
                self.attr_defn, **kw
            )
            return True
        except Exception as e:
            print(e)
            return False

    def doesUserExist(self, *args, **kw):
        '''
        is user in ddb?
        args: username, password
        '''
        return True

    def signUpUser(self, *args, **kw):
        '''
        add user to ddb
        args: username, password, email
        '''
        entry = self.fmtentry__(*args)
        return False
