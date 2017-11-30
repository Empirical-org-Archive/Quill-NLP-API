from flask import Flask, jsonify
app = Flask(__name__)

@app.route("/")
def ping():
    return jsonify(200)