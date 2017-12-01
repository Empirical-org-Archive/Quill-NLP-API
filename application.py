from flask import Flask, jsonify, request
import libs.pos
import libs.ai
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

@app.route("/sentence_or_not", methods=["POST"])
def sentence_or_not():
    return jsonify({'text': libs.ai.test_sentence(request.form['text'])})

# run the app.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    app.debug = True
    app.run()