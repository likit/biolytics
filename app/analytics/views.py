from . import analytics
from flask import render_template, jsonify
import pandas as pd


@analytics.route('/')
def upload():
    '''Upload data file.'''
    return '<h1>Please upload your data file.</h1>'