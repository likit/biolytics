# -*- coding: utf8 -*-
activate_this = '/Users/likit/.virtualenvs/biolytics/bin/activate_this.py'
exec(open(activate_this).read(), dict(__file__=activate_this))

import os
import sqlite3
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request
from flask_uploads import UploadSet, configure_uploads

app = Flask(__name__)

rootdir = os.path.abspath(os.path.dirname(__file__))
database_uri = 'sqlite:///{}'.format(os.path.join(rootdir, 'database.sqlite').replace('\\', '\\\\'))
app.config['SQLALCHEMY_DATABASE_URI'] = database_uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

import models

db.create_all()

app.config['UPLOADED_DATAFILES_DEST'] = os.path.join(rootdir, 'uploads')
datafiles = UploadSet('datafiles', ('xls', 'xlsx', 'csv', 'txt', 'tsv'))
configure_uploads(app, (datafiles,))


from antibiogram import antibiogram as antibiogram_blueprint
app.register_blueprint(antibiogram_blueprint)

from analytics import analytics as analytics_blueprint
app.register_blueprint(analytics_blueprint)


@app.route('/')
def index():
    return render_template('index.html')


def run_server():
    app.run(host='127.0.0.1', port=5000, threaded=True)


if __name__ == '__main__':
    app.run(debug=True, port=5000)