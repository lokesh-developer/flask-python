from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/<int:id>")
def get_id(id):
    return jsonify({"id": id})