from flask import Flask, render_template, Markup, request, url_for, redirect
import markov_lyrics

app = Flask(__name__)

eloadok = {
    "Taylor Swift": "taylor_swift",
    "Three Days Grace": "three_days_grace",
    "Linkin Park": None,
    "Queen": None
}

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/generate_lyrics')
def generate_lyrics():
    return render_template("lyrics.html", eloadok=eloadok, generated_lyrics=Markup(markov_lyrics.get_lyrics("taylor_swift")))


@app.route('/generate_lyrics/<string:eloado>')
def generate_lyrics_by_eloado(eloado):
    return render_template("lyrics.html", eloadok=eloadok, generated_lyrics=Markup(markov_lyrics.get_lyrics(eloado)))


@app.route('/handle_new', methods=['POST'])
def handle_data():
    eloado_post = request.form['eloado']
    return redirect(url_for("generate_lyrics_by_eloado", eloado=eloado_post))


if __name__ == '__main__':
    app.run(debug=False, host="127.0.0.1")
