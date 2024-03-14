# server.py
import os
from livekit import api

def getToken():
  token = api.AccessToken("APIPaJ4P4szVYU2", "HCnleH98FnqiCNKjNYZK3e8KmHeEsaBoUHhOAgxgeEID") \
    .with_identity("User4") \
    .with_name("User4") \
    .with_grants(api.VideoGrants(
        room_join=True,
        room="March_11_Room",
    ))
  return token.to_jwt()
  
print(getToken())

