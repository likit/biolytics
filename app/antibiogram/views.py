from flask import render_template
from . import antibiogram as abg

@abg.route('/')
def index():
    return render_template('antibiogram/index.html')