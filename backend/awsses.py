import boto3
from dotenv import load_dotenv
import os


load_dotenv()

class ses:
    ''' to email people '''

    def __init__(self):
        self.cli = boto3.client(
                        'ses',
                        aws_access_key_id=os.environ.get('access'),
                        aws_secret_access_key=os.environ.get('secret'),
                        region_name='us-west-2'
                    )

    def send(to, msg):
        self.cli.send_email(
            Source='1jackwolf1@gmail.com',
            Destination={
                'ToAddresses': ['1jackwolf1@gmail.com']
            },
            Message={
                'Subject': {
                    'Data': 'SES test...'
                },
                'Body': {
                    'Data': 'SES test!!'
                },
                'Html': {
                    'Data': '<h1>SES test :)</h1>'
                }
            }
        )
