
from flask import Flask, render_template
import requests

app = Flask(__name__)

# @app.route("/")
# def function():
#     #return "Hello World."
#     return render_template("index.html")

@app.route("/<name>")
def guess(name):
    gender_data = requests.get(url=f"https://api.genderize.io?name={name}").json()
    gender = gender_data["gender"]
    age_data = requests.get(url=f"https://api.agify.io?name={name}").json()
    age = age_data["age"]
    return render_template("index.html", name=name, gender=gender, age=age)


if __name__ == "__main__":
    app.run(debug=True)