from flask import Flask

app = Flask(__name__)

@app.route("/")
def name():
    return "This is my practice flask application for HW2"

@app.route("/about")
def about():
    return "My name is Alejandro Alvarado Mora, I am 22 years old"