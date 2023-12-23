import mysql.connector
import json
from flask import make_response
class User_model:
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
    def user_getall_model(self):
        # business logic
        self.cur.execute("SELECT * FROM users;")
        result = self.cur.fetchall()
        if len(result)>0:
            res = make_response({"payload": result}, 200)
            res.headers['Access-Control-Allow-Origin'] = "*"
            return res
        else:
             return make_response({"message":"No data found"}, 204)
        
    def user_addone_model(self,data):
         self.cur.execute(f"INSERT INTO users(name,email,phone,role,password) VALUES('{data['name']}','{data['email']}','{data['phone']}','{data['role']}','{data['password']}')")
         return make_response({"message":"User Created Sucessfully"}, 201)
    
    def user_update_controller(self,data):
         self.cur.execute(f"UPDATE users SET name='{data['name']}',email='{data['email']}',phone='{data['phone']}',role='{data['role']}',password='{data['password']}' WHERE id={data['id']}")
         
         if self.cur.rowcount>0:
            return make_response({"message":"USer Updated Sucessfully"}, 201)
         else:
              return make_response({"message":"Didnt updated anything"}, 202)
              
    def user_delete_controller(self,id):
         self.cur.execute(f"DELETE FROM users WHERE id={id}")
         if self.cur.rowcount>0:
            return make_response({"message":"User DELETED Sucessfully"}, 200)
         else:
              return make_response({"message":"Nothing to delete"}, 202)
         
    def user_patch_model(self,data,id):
        # Update users SET col=val ,col2=val2 WHERE id={id}
        qry ="UPDATE users SET "
        for key in data:
            qry +=f"{key}='{data[key]}',"
        qry = qry[:-1]
        qry += f" WHERE id={id};"

        self.cur.execute(qry)
        if self.cur.rowcount>0:
            return make_response({"message":"USer patched Sucessfully"}, 201)
        else:
              return make_response({"message":"Didnt patched anything"}, 202)
    
    def user_pagination_model(self,limit,page):
        limit = (int(limit))
        page = int(page)
        total = int(page*limit)
        start = total - limit
        qry = f"SELECT * FROM users LIMIT {start},{limit};"

        self.cur.execute(qry)
        result = self.cur.fetchall()
        if len(result)>0:
            res = make_response({"payload": result, "page_no":page, "limit":limit}, 200)
            return res
        else:
             return make_response({"message":"No data found"}, 204)

    def user_upload_avatar_controller(self, uid, filepath):
        self.cur.execute(f"UPDATE users SET avatar='{filepath}' WHERE id={uid}")
        if self.cur.rowcount>0:
            return make_response({"message":"File uploaded Sucessfully"}, 201)
        else:
            return make_response({"message":"Didnt uploaded File"}, 202)
        