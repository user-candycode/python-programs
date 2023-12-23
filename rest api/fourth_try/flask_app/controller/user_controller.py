from app import app
from model.user_model import User_model
from model.auth_model import Auth_model
from flask import request, send_file
from datetime import datetime

obj = User_model()
auth = Auth_model()

@app.route("/user/getall", methods=["GET"])
@auth.token_auth("/user/getall")
def user_getall_controller():
    return obj.user_getall_model()

@app.route("/user/addone", methods=["POST"])
def user_addone_controller():
    return obj.user_addone_model(request.form)

@app.route("/user/update", methods=["PUT"])
def user_update_controller():
    return obj.user_update_controller(request.form)

@app.route("/user/delete/<id>", methods=["DELETE"])
def user_delete_controller(id):
    return obj.user_delete_controller(id)

@app.route("/user/patch/<id>", methods=["PATCH"])
def user_patch_controller(id):
    return obj.user_patch_model(request.form, id)

@app.route("/user/getall/limit/<limit>/page/<page>", methods=["GET"])
def user_pagination_controller(limit,page):
    return obj.user_pagination_model(limit, page)

# file options 
'''
    1. uploading file from a postman to server 
    2. saving file into the file system with unique file name
    3. updating filepath in database with respective entity
    4. creating end point to read file 
'''
@app.route("/user/<uid>/upload/avatar", methods=["PUT"])
def user_upload_avtar_controller(uid):
    file = request.files['avatar']
    # file.save(f"uploads/{file.filename}")
    uniqueFileName = str(datetime.now().timestamp()).replace(".","")
    fileNameSplit = file.filename.split(".")
    ext = fileNameSplit[-1]
    finalFilePath = f"uploads/{uniqueFileName}.{ext}"
    file.save(finalFilePath)
    return obj.user_upload_avatar_controller(uid,finalFilePath)

# routes
@app.route("/uploads/<filename>")
def user_getavatar_controller(filename):
    return send_file(f"uploads/{filename}")


#JWT
@app.route("/user/login", methods=["POST"])
def user_login_controller():
    # request.form
    return obj.user_login_model(request.form)