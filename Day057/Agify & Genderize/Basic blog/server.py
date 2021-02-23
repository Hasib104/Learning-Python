
from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/")
def function():
    return "Hello World."

@app.route("/blog")
def blog():
    url = "https://api.npoint.io/5abcca6f4e39b4955965"
    response = requests.get(url=url)
    posts = response.json()
    return render_template("index.html", posts=posts)


if __name__ == "__main__":
    app.run(debug=True)