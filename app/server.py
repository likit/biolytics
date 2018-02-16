# -*- coding: utf8 -*-
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('antibiogram.html')

def run_server():
    app.run(host='127.0.0.1', port=5000, threaded=True)


if __name__ == '__main__':
    app.run(debug=True, port=5000)