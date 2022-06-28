# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 12:27:11 2022

@author: S545443
"""

import os
import pandas as pd

from fillpdf import fillpdfs
from sqlalchemy import true



template_path = os.path.join(os.getenv("AUTOMATION_TEMPLATES"), "new_applications_filler", "OPElectronicCoversheet.pdf")


def generate_new_applications(data_file, output_folder):
    dataframe =  pd.read_csv(data_file)
    dataframe.dropna(inplace= True)
    for i in range(0, dataframe.shape[0]):
        data_dict = {
        'lastName': dataframe['Last Name'][i],
        'Text1': dataframe['First Name'][i],
        'Mailing Address': str(dataframe['Street Line 1'][i])+', '+str(dataframe['City'][i])+', '+ str(dataframe['State'][i])+ ' '+ str(int(dataframe['ZIP'][i])),
        '919': str(int(dataframe['ID'][i])),
        'Degree Applied': dataframe['Degree'][i],
        'Program Applied': dataframe['Major'][i]
        }
        fileName = os.path.join(output_folder, "{0}_Application.pdf".format(str(dataframe['Last Name'][i])))

        fillpdfs.write_fillable_pdf(template_path, fileName, data_dict)
    return True