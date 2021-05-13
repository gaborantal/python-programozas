from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template("index_simple.html")


if __name__ == '__main__':
    app.run(debug=False, host="127.0.0.1")
