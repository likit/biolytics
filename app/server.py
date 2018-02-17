# -*- coding: utf8 -*-
import os
from flask import Flask, render_template, request
from flask_uploads import UploadSet, configure_uploads

app = Flask(__name__)

rootdir = os.path.abspath(os.path.dirname(__file__))
app.config['UPLOADED_DATAFILES_DEST'] = os.path.join(rootdir, 'uploads')
datafiles = UploadSet('datafiles', ('xlsx', 'csv', 'txt', 'tsv'))
configure_uploads(app, (datafiles,))


from antibiogram import antibiogram as antibiogram_blueprint
app.register_blueprint(antibiogram_blueprint)

@app.route('/')
def index():
    return render_template('antibiogram.html')


@app.route('/upload', methods=['POST', 'GET'])
def upload():
    if 'POST' == request.method and 'datafile' in request.files:
        filename = datafiles.save(request.files['datafile'])
        return datafiles.url(filename)
    return render_template('uploads.html')


def run_server():
    app.run(host='127.0.0.1', port=5000, threaded=True)


if __name__ == '__main__':
    app.run(debug=True, port=5000)