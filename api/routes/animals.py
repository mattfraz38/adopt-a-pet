from flask import Blueprint, render_template
from ..helper import pets

animals_blueprint = Blueprint('animals', __name__, url_prefix='/GET')


@animals_blueprint.route('/<pet_type>')
def get_animals(pet_type):
  # pet_details = pets[pet_type][pet_id] 

  return render_template('animals.html', pets=pets, pet_type=pet_type)
