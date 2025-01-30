import os

import jwt

def generateJwt(payload):
    return jwt.encode(payload, os.environ['JWT_SECRET'], algorithm="HS256")

def verifyJwt(token) -> bool | dict:
    return jwt.decode(token, os.environ['JWT_SECRET'], verify=True, algorithms=["HS256"])
