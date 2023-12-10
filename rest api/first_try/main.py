from flask import Flask
import jsonify # for producing a json data

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, There!</p>"



# random logic ==============================================================

@app.route("/armstrong/<int:n>") # simple rotue setup
def armstrong(n):
    sum = 0
    order = len(str(n))
    copy_n = n
    while n>0:
        digit = n%10
        sum += digit **order
        n = n // 10

    if sum == copy_n:
        print(f"{copy_n} is an armstrong number")
        result = {
            "number": copy_n,
            "armstrong": True,
            "random_string": "sahi chala"
        }
    else:
        print(f"{copy_n} is a normal number")
        result = {
            "number": copy_n,
            "armstrong": False,
            "random_string": "sahi nahi chala"
        }
    return jsonify(result) # returns json object on an address

# random logic ==============================================================






# start of app ==============================================================
if __name__ == "__main__":
    app.run(debug=True)
# start of app ==============================================================
