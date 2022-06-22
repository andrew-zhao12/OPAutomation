from flask import Blueprint, abort, jsonify
import requests

import requests
from apifairy import authenticate, body, response, other_responses, arguments


acceptance_letters = Blueprint('acceptance_letters', __name__)