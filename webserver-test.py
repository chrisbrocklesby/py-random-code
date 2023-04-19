from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/name/<name>")
def hello(name):
    return f"Hello, {escape(name).title()}!"  # Escape the name


@app.errorhandler(404)
def not_found(error):
    return "not found", 404


app.run(port=8000, debug=True)
