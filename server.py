# Simple Flask server to serve Emberosaurus API
from flask import Flask, request, jsonify
from components.ember import Ember
from components.emberosaurus import Emberosaurus

app = Flask(__name__)

ember = Ember()
emberosaurus = Emberosaurus(ember)


@app.route("/synonyms", methods=["POST"])
def synonyms():
    data = request.json
    sentence = data["sentence"]
    word = data["word"]
    ranked = emberosaurus.ranked_synonyms(sentence, word)
    return jsonify(ranked)


if __name__ == "__main__":
    app.run(port=5000, debug=True)
