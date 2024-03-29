﻿
from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def home():
    # return "Hello, World!"
    return render_template("home.html")

@app.route("/about/")
def about():
    # return "About here."
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)