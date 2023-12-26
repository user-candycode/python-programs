import mysql.connector
import json
from flask import make_response,request
import jwt
import re

class Auth_model:
    def __init__(self):
            hostname = "localhost"
            username = "candy"
            passwd = "root"
            db_name = "flask_tutorial"
            # Connections establishment
            try:
                self.con = mysql.connector.connect(host=hostname,user=username,password=passwd,database=db_name)
                self.con.autocommit=True
                self.cur = self.con.cursor(dictionary=True)
                print("Connection sucessfull to mysql")
            except:
                print("Some Error")

    def token_auth(self,endpoint):
        def inner1(func):
            def inner2(*args):
                authorization = request.headers.get("authorization")
                if re.match("^Bearer *([^ ]+) *$", authorization, flags=0):
                    token = authorization.split(" ")[1]
                    
                    try:
                        jwt_decoded = jwt.decode(token,"MrK",algorithm="HS256")
                    except jwt.ExpiredSignatureError:
                        return make_response({"ERROR":"Token Expired"},401)

                    roll_id = jwt_decoded['payload']['role_id']
                    self.cur.execute(f'SELECT roles FROM accessibility_view WHERE endpoint="{endpoint}"')
                    result = self.cur.fetchall()
                    if len(result) >0:
                        print(result)
                        return func(*args)
                    else:
                        return make_response({"Error":"Unknown End Point"}, 404)
                else:
                    return make_response({"ERROR":"INVALID_TOKEN"},401)
            return inner2
        return inner1 # no parenthesis as we are returning function as object