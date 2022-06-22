from flask import Blueprint, abort, jsonify
import requests

import requests
from apifairy import authenticate, body, response, other_responses, arguments


welcome_emails = Blueprint('welcome_emails', __name__)