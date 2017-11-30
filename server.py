from flask import Flask, jsonify, request
import libs.pos
app = Flask(__name__)

@app.route("/")
def hello():
    return jsonify("Hello!")

@app.route("/ping")
def ping():
    return jsonify(200)

@app.route("/get_POS", methods=["POST"])
def get_pos():
  return jsonify({'text': libs.pos.get_POS(request.form['text'])})
