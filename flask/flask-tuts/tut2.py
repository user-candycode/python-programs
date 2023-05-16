from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("indextest.html")

@app.route("/about")
def about():
    name = "MrK!"
    return render_template('about.html', name2 = name)

@app.route("/boots")
def boots():
    return render_template('bootstrap.html')









app.run(debug = True)
