import base64
import os
from twilio.rest import Client

def hello_pubsub(event, context):
    """Triggered from a message on a Cloud Pub/Sub topic.
    Args:
         event (dict): Event payload.
         context (google.cloud.functions.Context): Metadata for the event.
    """
    pubsub_message = base64.b64decode(event['data']).decode('utf-8')
    print(pubsub_message)

    account_sid = 'AC6440630c3dfee0be975a27dab8a657b6'
    auth_token = 'b363e7c8d9caf64c67b82b28b7c9c88c'
    client = Client(account_sid, auth_token)
    
    message = client.messages.create(
                              body='Message from twillo pubsub : ' +pubsub_message,
                              from_='func-lab',
                              to='5144302841'
                          )

    print(message.sid)
