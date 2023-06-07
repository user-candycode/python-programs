from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

# import mysql.connector

import json

from datetime import datetime


#================================================
#scrapping values from json file for easy access
with open("flask-tuts/config.json") as c:
    params = json.load(c)["params"]

local_server = True
#================================================


#initilizing flask app
app = Flask(__name__)

# ==============================================================
#Making sql server connection
if(local_server):
    app.config['SQLALCHEMY_DATABASE_URI'] = params["prod_uri"]
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = params["local_uri"]
# ==============================================================

#initilizing sql database as sqlalchemy app
db = SQLAlchemy(app)

#creating a table name Contacts
# class Contacts(db.Model):
#     # sno = db.Column(db.serial, primary_key=True)
#     name = db.Column(db.String(80), nullable=False)
#     phone_num = db.Column(db.String(12), nullable=False)
#     msg = db.Column(db.String(120), nullable=False)
#     date = db.Column(db.String(12), nullable=True)
#     email = db.Column(db.String(20), nullable=False)

# ************************************************************************
'''
Below this are page routes
1. /
2. about
3. contact
    - 3.1 getting data from post page to be stored in sql
4. post
'''

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # Getting values from html page using name
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        message = request.form.get('message')

        '''ADD entry to the database'''
        # entry = Contacts(name=name, phone_num=phone, msg=message,
        #                  date=datetime.datetime.now(), email=email)

        # pushing an insert query to db
        # db.session.add(entry)
        # db.session.commit()
        # db.execute("select * from users")
        result_set = db.execute("SELECT * FROM users")  
        for r in result_set:  
            print(r)
    return render_template("contact.html")


@app.route("/post")
def post():
    return render_template("post.html")

# ************************************************************************


if __name__ == '__main__':
    app.run(debug=True)
