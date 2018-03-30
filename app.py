# coding=utf8
from flask import Flask, jsonify, request
import pos
from qfragment import check

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

@app.route("/get_pos_match", methods=["POST"])
def get_pos_match():
    val = pos.get_pos_match(request.form['text'], request.form['question_id'])
    return jsonify({'text': request.form['text'], 'match': val})

@app.route("/sentence_or_not", methods=["POST"])
def sentence_or_not():
    result = check(request.form['text']).to_dict()
    return jsonify(check(request.form['text']).to_dict())

# run the app.
if __name__ == "__main__":
    app.run()
