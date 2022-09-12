# -*- coding: utf-8 -*-
"""
Created on Mon Jun  6 14:31:06 2022

@author: S545443
"""

import pandas as pd # pandas is a data analysis and manipulation tool 
from mailmerge import MailMerge # mailmerge is able to transform data into text form
from docx2pdf import convert # tool to convert docx to pdf
import re
import os

templates_folder = os.path.join(os.getenv("AUTOMATION_TEMPLATES"), "acceptance_letters")

def generate_acceptance_letters(data_file, output_folder):
    # Reading data
    dataframe = pd.read_csv(data_file)

    # removes students that are returning graduates and returning specialists
    dataframe = dataframe[(dataframe['Student Type'] != "Returning Graduate") & (dataframe['Student Type'] != "Returning Specialist")]

    # loops through dataframe columns
    for i in range(0, dataframe.shape[0]):
        degree = dataframe['Major'][i]
        
        # joins file path of template folder and accept letter
        if dataframe['Latest Decision'][i] == "Graduate Acceptance":
            template_file_path = os.path.join(templates_folder,"{0}_Accept Letter.docx".format(degree))
        else:
            template_file_path = os.path.join(templates_folder,"{0}_Conditional Accept Letter.docx".format(degree))

        document = MailMerge(template_file_path)
        print(document.get_merge_fields())
        
        lastName = dataframe['Last Name'][i]
        
        # sorting students to advisors
        if 'MBA' in dataframe['Major'][i] and re.match(r"^[A-L]", lastName):
            advisor = "Dr. Araceli Hernandez"
            advisor_email = "araceli@nwmissouri.edu"
        elif 'MBA' in dataframe['Major'][i]:
            advisor = "Dr. Renee Oyotode- Adebile"
            advisor_email = "reneeo@nwmissouri.edu"
        else:
            advisor = "Dr. Joni Adkins"
            advisor_email = "jadkins@nwmissouri.edu"
        
        # merges personal information onto document using merge fields
        document.merge(
            LASTNAME = lastName,
            FIRSTNAME = dataframe['First Name'][i],
            STATE = dataframe['State'][i],
            CITY = dataframe['City'][i],
            STREET = dataframe['Street'][i],
            ZIP = str(dataframe['Zip'][i]),
            TERM = dataframe['Term Desc'][i],
            ADVISOR = advisor,
            ADVISOREMAIL = advisor_email)
        
        save_temp_docx = os.path.join(os.getenv("TEMP_FOLDER"), "temp_acceptance_letters.docx")
        document.write(save_temp_docx)
        
        fileName = dataframe['First Name'][i].replace(" ","")+dataframe['Last Name'][i]
        fileName = os.path.join(output_folder, "{0}AcceptanceLetter.pdf".format(fileName))
        
        # converts from docx to pdf
        convert(save_temp_docx, fileName)    
    return True