import urllib
import os
import pandas as pd
from flask import render_template, jsonify, request, redirect, url_for

from . import analytics
from server import datafiles, app, db
from models import UploadedData

ALLOWED_EXTENSIONS = set(['txt', 'csv', 'xls', 'xlsx'])

@analytics.route('/', methods=['POST', 'GET'])
def upload():
    if 'POST' == request.method and 'datafile' in request.files:
        filename = datafiles.save(request.files['datafile'])
        description = request.form['description']
        upload = UploadedData(filename=filename, description=description)
        db.session.add(upload)
        db.session.commit()
        print('finished uploading..')
        return redirect(url_for('analytics.inspect_data', filename=filename))
    else:
        all_uploads = UploadedData.query.all()
    return render_template('analytics/upload.html', all_uploads=all_uploads)


@analytics.route('/data/inspect/')
def inspect_data():
    filename = request.args.get('filename', None)
    if filename:
        datafile = os.path.join(app.config['UPLOADED_DATAFILES_DEST'], filename)
        df = pd.read_excel(datafile)
    return render_template('analytics/inspect.html')
