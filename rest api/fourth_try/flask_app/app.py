from flask import Flask
import sys

# Set pythondontwritebytecode to True
sys.dont_write_bytecode = True


app = Flask(__name__)
# app.debug = True

@app.route("/")
def welcome():
    return "Hello!"


@app.route("/home")
def home():
    return "Home"


# from controller import user_controller, product_controller
from controller import *


# if __name__ == '__main__':
#     # Enable debug mode
#     app.run(debug=True)
