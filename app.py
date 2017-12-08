# coding=utf8
from flask import Flask, jsonify, request
import pos
import ai
app = Flask(__name__)

@app.route("/")
def hello():
    return jsonify("Hallo!")

@app.route("/ping")
def ping():
    return jsonify(200)

@app.route("/get_POS", methods=["POST"])
def get_pos():
    return jsonify({'text': pos.get_POS(request.form['text'])})

@app.route("/sentence_or_not", methods=["POST"])
def sentence_or_not():
    return jsonify({'text': ai.test_sentence(request.form['text'])})

# run the app.
if __name__ == "__main__":
    app.run()