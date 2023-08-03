from twilio.rest import Client
SID = 'ACf5a19f9b908d13b186d4ac94df4fffd0'
AUTH_TOKEN = 'f0abbd93482a7f80c270db072c033baf'

cl = Client(SID, AUTH_TOKEN)

cl.messages.create(body='Hey, I am GreyMatters Here', from_='+14704666619',to='+91**********')
