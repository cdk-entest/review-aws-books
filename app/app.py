# Hai Tran 13 JUN 2022
# Setup flask

from flask import Flask, render_template
import json

app = Flask(__name__)

# get book list should be even number
with open("./static/book.json", "rb") as file:
    books = json.load(file)


@app.route("/")
def index():
    return render_template("index.html", books=books, nrow=len(books))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
