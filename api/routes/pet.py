from flask import Blueprint, render_template, url_for
from ..helper import pets

pet_blueprint = Blueprint('pet', __name__, url_prefix='/GET/<pet_type>')


@pet_blueprint.route('/<int:pet_id>')
def get_pet(pet_type, pet_id):
  pet_details = pets[pet_type][pet_id]

  return render_template('pet.html', pet_details=pet_details, pet_type=pet_type, pet_id=pet_id)
