from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/left-sidebar")
def about():
    return render_template("left-sidebar.html")


@app.route("/right-sidebar")
def work():
    return render_template("right-sidebar.html")


@app.route("/no-sidebar")
def contact():
    return render_template("no-sidebar.html")


if __name__ == "__main__":
    app.run(debug=True)
