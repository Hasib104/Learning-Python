
from flask import Flask, render_template
import random
import datetime

app = Flask(__name__)

@app.route("/")
def function():
    #return "Hello World."
    random_num = random.randint(0,9)
    year = datetime.datetime.now().year
    return render_template("index.html", random_num=random_num, year=year)

if __name__ == "__main__":
    app.run(debug=True)