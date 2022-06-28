from flask import Blueprint, abort, jsonify, request

from app.resources.utils import ComputerAccessDirections



computer_access_directions = Blueprint('computer_access_directions', __name__)

@computer_access_directions.route("/computer_access_directions", methods= ['POST'])
def generate_computer_access_directions():
    data_file = request.files["file"]
    ComputerAccessDirections.generate_computer_access_directions(data_file)
    return "success"