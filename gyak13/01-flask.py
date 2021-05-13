import datetime
import json
from flask import Flask

app = Flask(__name__)


@app.route('/now')
def now():
    # return datetime.datetime.now()
    return datetime.datetime.now().isoformat()


@app.route('/now/json')
def now_json():
    return json.dumps(dict(current_date=datetime.datetime.now().isoformat()))


@app.route('/')
@app.route('/hello')
def hello():
    return 'Hello, World!'


if __name__ == '__main__':
    app.run(debug=False, host="127.0.0.1")
