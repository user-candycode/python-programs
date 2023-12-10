from flask import Flask
# from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqllite:///data.db'
# db = SQLAlchemy(app)

#
# class Drink(db.model):
#     id = db.column(db.Integer, primary_key=True)
#     mane = db.column(db.String(80),unique=True,nullable=False)
#     description = db.Column(db.String(120))
#
#     def __repr__(self):
#         return f"{self.name} - {self.description}"


@app.route('/',methods=['GET'])
def index():
    return "Hello!"


@app.route('/drinks')
def get_drinks():
    return {"drinks": "drink_data"}


# start of app ==============================================================
if __name__ == "__main__":
    app.run(debug=True)
# start of app ==============================================================



# drink = Drink.query.get_or_404(id)
