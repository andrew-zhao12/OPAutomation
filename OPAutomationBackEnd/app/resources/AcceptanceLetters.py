from flask import Blueprint, request, send_file
# from apifairy import authenticate, body, response, other_responses, arguments
import time
import os
import zipfile
import io
from app.resources.utils import AcceptanceLetters

# blueprint to organize group of related views
acceptance_letters = Blueprint('acceptance_letters', __name__)

@acceptance_letters.route("/acceptance_letters", methods= ['POST'])
def generate_acceptance_letters():
    temp_folder_name = os.path.join(os.getenv("TEMP_FOLDER"), str(time.time_ns()))
    os.mkdir(temp_folder_name)
    data_file = request.files["file"]
    if AcceptanceLetters.generate_acceptance_letters(data_file, temp_folder_name):
        memory_file = io.BytesIO()
        with zipfile.ZipFile(memory_file, 'w') as zf:
            files = os.listdir(temp_folder_name)
            for filename in files:
                FILEPATH = os.path.join(temp_folder_name, filename)
                zf.write(FILEPATH, arcname=filename)
        memory_file.seek(0)
        return send_file(memory_file, mimetype='application/zip', attachment_filename="download.zip")