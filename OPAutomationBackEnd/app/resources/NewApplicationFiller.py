from flask import Blueprint, abort, jsonify
import requests

import requests
from apifairy import authenticate, body, response, other_responses, arguments


new_application_filler = Blueprint('new_application_filler', __name__)