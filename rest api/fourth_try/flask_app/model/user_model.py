import mysql.connector
import json
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
             return json.dumps(result)
        else:
             return "No data found"
        
    def user_addone_model(self,data):
         self.cur.execute(f"INSERT INTO users(name,email,phone,role,password) VALUES('{data['name']}','{data['email']}','{data['phone']}','{data['role']}','{data['password']}')")
         return "<h1>user created sucessfull</h1>"
    
    def user_update_controller(self,data):
         self.cur.execute(f"UPDATE users SET name='{data['name']}',email='{data['email']}',phone='{data['phone']}',role='{data['role']}',password='{data['password']}' WHERE id={data['id']}")
         
         if self.cur.rowcount>0:
            return "User Updated Sucessfully"
         else:
              return "Nothing to update"
              
         