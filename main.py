"""
Start with creating account:
*https://console.twilio.com/
and add the required stuff in `keys.pyy`
"""
from twilio.rest import Client
import keys

client = Client(keys.account_sid, keys.auth_token)

while True:
    message = client.messages.create(
        body="You are hacked :-))))",
        from_=keys.twilio_number,
        to=keys.target_number,
    )
