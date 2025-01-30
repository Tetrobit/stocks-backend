import os

import jwt

def generateJwt(payload):
    return jwt.encode(payload, os.environ['JWT_SECRET'], algorithm="HS256")
