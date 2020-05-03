"""
This file contains code to send an email with the json file attachment.
Author: Rutuja Tikhile.
Data:9/4/2020
"""
import os
from dotenv import load_dotenv
load_dotenv()
from email.message import EmailMessage
import smtplib


class SMTP_Mail:

    def send_mail(self, user_email):

        msg = EmailMessage()
        password = os.getenv('password')
        msg['From'] = os.getenv('from')
        msg['To'] = user_email
        msg['Subject'] = 'SCRAPED DATA'
        msg.set_content('Trying to attach a .json file, This is the data from weather site')

        with open(r'C:\Users\Dell\PycharmProjects\Weather\Weather\weatherfeild.json', 'rb') as f:
            file_data = f.read()
            file_name = f.name

        # Attach
        msg.add_attachment(file_data, maintype='application', subtype='json', filename=file_name)
        # by setting the maintype and subtype that's what the python documentation called a generic tag.

        with smtplib.SMTP_SSL('smtp.gmail.com', os.getenv('port')) as smtp: #587 465
            smtp.login(msg['From'], password)
            smtp.send_message(msg)
