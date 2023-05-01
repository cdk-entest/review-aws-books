# Hai Tran 13 JUN 2022
# Setup flask

from flask import Flask, render_template
import json

# app = Flask(__name__)
app = Flask("my app")

app.jinja_env.auto_reload = True
app.config["TEMPLATES_AUTO_RELOAD"] = True

# get book list should be even number
with open("./static/book.json", "rb") as file:
    books = json.load(file)


@app.route("/")
def index():
    return render_template("index.html", books=books, nrow=len(books))


def gen_static_web():
    with app.app_context():
        rendered = render_template(
            "index.html", books=books, nrow=len(books)
        )
        print(rendered)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8081, debug=True)
# gen_static_web()
