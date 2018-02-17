from flask import Blueprint

antibiogram = Blueprint('antibiogram', __name__, url_prefix='/antibiogram')

from . import views
