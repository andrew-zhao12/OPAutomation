from flask import Blueprint, abort, jsonify, request, send_file

from apifairy import authenticate, body, response, other_responses, arguments
from app.resources.utils import NewApplicationsFiller
import os
import time
import io
import zipfile


new_application_filler = Blueprint('new_application_filler', __name__)

@new_application_filler.route("/new_applications_filler", methods= ['POST'])
def generate_new_application_filler():
    data_file = request.files["file"]
    temp_folder_name = os.path.join(os.getenv("TEMP_FOLDER"), "new_applications"+str(time.time_ns()))
    os.mkdir(temp_folder_name)
    if NewApplicationsFiller.generate_new_applications(data_file, temp_folder_name):
        memory_file = io.BytesIO()
        with zipfile.ZipFile(memory_file, 'w') as zf:
            files = os.listdir(temp_folder_name)
            for filename in files:
                FILEPATH = os.path.join(temp_folder_name, filename)
                zf.write(FILEPATH, arcname=filename)
        memory_file.seek(0)
        return send_file(memory_file, mimetype='application/zip', attachment_filename="download.zip")