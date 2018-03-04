import urllib
import os
import pandas as pd
from flask import render_template, jsonify, request, redirect, url_for

from . import analytics
from server import datafiles, app, db
import models

ALLOWED_EXTENSIONS = set(['txt', 'csv', 'xls', 'xlsx'])

@analytics.route('/', methods=['POST', 'GET'])
def upload():
    if 'POST' == request.method and 'datafile' in request.files:
        filename = datafiles.save(request.files['datafile'])
        description = request.form['description']
        # need to handle failed upload
        upload = models.UploadedData(filename=filename, description=description)
        db.session.add(upload)
        db.session.commit()
        print('finished uploading..')
        return redirect(url_for('analytics.inspect_data', filename=filename))
    else:
        all_uploads = models.UploadedData.query.all()
    return render_template('analytics/upload.html', all_uploads=all_uploads)


@analytics.route('/data/inspect/')
def inspect_data():
    filename = request.args.get('filename', None)
    if filename:
        datafile = os.path.join(app.config['UPLOADED_DATAFILES_DEST'], filename)
        return render_template('analytics/inspect.html', datafile=datafile, filename=filename)
    return '<h1>No file was specified.</h1>'


@analytics.route('/api/inspect')
def api_inspect_data():
    datafile = request.args.get('datafile', None)
    print('inspecting file', datafile)
    if datafile:
        df = pd.read_excel(datafile)
        data = []
        for col in df.columns:
            # colname, dtype, count, included
            data.append([col, str(df[col].dtypes), int(df[col].count()), True])
        return jsonify(data)
