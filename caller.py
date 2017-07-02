# Download the library from twilio.com/docs/libraries
from twilio.rest import Client

# Get these credentials from http://twilio.com/user/account
account_sid = "SIDHERE"
auth_token = "TOKENHERE"
client = Client(account_sid, auth_token)

# Make the call
call = client.api.account.calls\
      .create(to="+1NUMTOCALL",  # Any phone number
              from_="+1NUMFROMCALL", # Must be a valid Twilio number
              url="http://twimlets.com/holdmusic?Bucket=com.twilio.music.ambient",
              record=True
)

print(call.sid)
