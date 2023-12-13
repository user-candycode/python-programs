from app import app
from model.user_model import User_model
from flask import request

obj = User_model()


@app.route("/user/getall", methods=["GET"])
def user_getall_controller():
    return obj.user_getall_model()

@app.route("/user/addone", methods=["POST"])
def user_addone_controller():
    return obj.user_addone_model(request.form)

@app.route("/user/update", methods=["PUT"])
def user_update_controller():
    return obj.user_update_controller(request.form)
