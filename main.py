from flask import Flask, render_template, request
import json

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def home():
    return render_template("index.html")


@app.route('/translate', methods=["GET", "POST"])
def translate():
    if request.method == "POST":
        word = list(request.form["word"].upper())
        morse = []
        try:
            with open("alphabet.json", "r") as data:
                alphabet = json.load(data)
            for letter in word:
                morse.append(alphabet[letter])
        except KeyError:
            return render_template("index.html", error=True)
    return render_template("translate.html", word=word, morse=morse)


if __name__ == "__main__":
    app.run(debug=True)
