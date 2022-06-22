from flask import Blueprint, abort, jsonify
import requests

import requests
from apifairy import authenticate, body, response, other_responses, arguments


computer_access_directions = Blueprint('computer_access_directions', __name__)