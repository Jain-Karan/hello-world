# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
sender = os.environ['TWILIO_SENDER']
reciever = os.environ['TWILIO_RECIEVER']
client = Client(account_sid, auth_token)

def sendsms(smsbody,sender,reciever):
    message = client.messages.create(
                              body=smsbody,
                              from_=sender,
                              to=reciever
                          )
    print(f'SMS: {message.sid} sent to {reciever} .')
