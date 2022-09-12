# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 11:12:43 2022

@author: S545443
"""

# This program is to send email to the user
from jinja2 import Environment # jinja2 is a templating engine
import smtplib # python tool to send emails
from email.mime.multipart import MIMEMultipart # MIME helps fill out emails
from email.mime.text import MIMEText
import os
import pandas as pd

template_path = os.path.join(os.getenv("AUTOMATION_TEMPLATES"), "computer_access_directions", "template.html")

# sends computer access directions to new students in email
def send_email(to_email, user_name, b_id):
    print(to_email, user_name, b_id)
    fromaddr = 'bearcat.bulletin@gmail.com'
    rcpt = [to_email]
    msg = MIMEMultipart()    
    body = open(template_path).read()
    body = MIMEText(Environment().from_string(body).render(
        SID=user_name, STUDENTID = b_id
    ),'html')
    msg['Subject'] = 'computer access directions'
    msg['To'] = to_email
    msg.attach(body)
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    try:
        nm = "bearcat.bulletin@gmail.com"
        pm = "cgevkvxeaxuzixcp"
        server.login(nm , pm)
    except Exception as e:
        print(e)
    server.sendmail(fromaddr, rcpt, msg.as_string())
    server.quit()

# generates parameters for send email function
def generate_computer_access_directions(data_file):
    # Reading data
    dataframe = pd.read_csv(data_file)
    for i in range(0, dataframe.shape[0]):
        to_email = dataframe['Email'][i]
        b_id = dataframe['BID'][i]
        user_name = dataframe['USERNAME'][i]

        send_email(to_email, user_name, b_id)
        break