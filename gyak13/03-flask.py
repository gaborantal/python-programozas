import random

from flask import Flask, render_template, Markup

import markov_lyrics

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/dobokocka/<int:num>')
# @app.route('/dobokocka/<num>')
def dobokocka(num):
    return f"<h1>{random.randint(0, num)+1}</h1>"


@app.route('/generate_lyrics')
def generate_lyrics():
    return render_template("lyrics_simple.html", generated_lyrics=Markup(markov_lyrics.get_lyrics("taylor_swift")))


@app.route('/generate_lyrics/<string:eloado>')
def generate_lyrics_by_eloado(eloado):
    return render_template("lyrics_simple.html", generated_lyrics=Markup(markov_lyrics.get_lyrics(eloado)))


if __name__ == '__main__':
    app.run(debug=False, host="127.0.0.1")
