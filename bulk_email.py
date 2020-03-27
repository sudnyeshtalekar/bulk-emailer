#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: justsud
"""

import csv                                        
import smtplib       
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

email_id = '***your_emailid***'
email_password = '****enter_your_password_here****'


subject = 'Test mail'  

msg = MIMEMultipart()
msg['From'] = email_id
msg['Subject'] = subject

body = 'Hi there test email sent from python'
msg.attach(MIMEText(body,'plain'))

with open('mail_list.csv','r') as mail_list:          
    csvreader = csv.reader(mail_list)

    for i in csvreader:
        mail_id = i[0]
        email_send = mail_id
        msg['To'] = email_sendemailer
        text = msg.as_string()
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(email_id, email_password)
        server.sendmail(email_id, email_send, text)
        server.quit()
        

#https://myaccount.google.com/lesssecureapps        
