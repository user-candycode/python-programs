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

@app.route("/user/delete/<id>", methods=["DELETE"])
def user_delete_controller(id):
    return obj.user_delete_controller(id)

@app.route("/user/patch/<id>", methods=["PATCH"])
def user_patch_controller(id):
    return obj.user_patch_model(request.form, id)

@app.route("/user/getall/limit/<limit>/page/<page>", methods=["GET"])
def user_pagination_controller(limit,page):
    return obj.user_pagination_model(limit, page)