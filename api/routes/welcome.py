from flask import Blueprint, render_template, url_for
from ..helper import pets

welcome_blueprint = Blueprint('welcome', __name__, url_prefix='/')

@welcome_blueprint.route('/')
def index():

  return render_template('welcome.html', pets=pets)
