import os
import smtplib
from pathlib import Path
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *

class QRCodeMailThread(QRunnable):
    def __init__(self,details:list,mail_content,file_path,receiver):
        super(QRCodeMailThread,self).__init__()
        self.details = details
        self.mail_content = mail_content
        self.file_path = file_path
        self.receiver = receiver   
 
    def run(self):
        message = MIMEMultipart()
        message['from']= self.details[2]
        message['to']= self.receiver
        message['subject']= self.details[0]
        message.attach(MIMEText(self.mail_content,'plain'))
        message.attach(MIMEImage(Path(self.file_path).read_bytes()))
        with smtplib.SMTP(host='smtp.gmail.com', port=587) as server:
            server.starttls()
            server.login(self.details[1],self.details[3])
            try:
                server.send_message(message)
            except:   
                pass