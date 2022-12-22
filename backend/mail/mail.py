
import os
import requests

from PySide2 import QtCore, QtWidgets
from PySide2.QtGui import (QColor)
from mail.ui_mail import Ui_Mail
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *

class Mail(QtWidgets.QDialog):
    def __init__(self):
        QtWidgets.QDialog.__init__(self)
        self.ui_mail = Ui_Mail()
        self.ui_mail.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.ui_mail.btn_close.clicked.connect(self.close)
        self.ui_mail.btn_minimize.clicked.connect(self.showMinimized)
        self.ui_mail.frame.mouseMoveEvent = self.MoveWindow 

        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(230, 230, 230, 50))
        self.ui_mail.frame.setGraphicsEffect(self.shadow)
        self.set_sender_details()     
    
    def MoveWindow(self, event):
        if self.isMaximized() == False:
            self.move(self.pos() + event.globalPos() - self.clickPosition)
            self.clickPosition = event.globalPos()
            event.accept()

    def mousePressEvent(self, event):
        self.clickPosition = event.globalPos()

    def connected_to_internet(self,url='http://www.google.com/', timeout=5):
        try:
            _ = requests.head(url, timeout=timeout)
            return True
        except requests.ConnectionError:  
            return False

    def get_email_details(self):
        from_ = self.ui_mail.email_from.text()
        from_email = self.ui_mail.email_sender.text()
        subject = self.ui_mail.email_subject.text()
        password = self.ui_mail.sender_password.text()
        return subject, from_email, from_, password

    def set_sender_details(self):
        details=self.get_details()
        self.ui_mail.email_from.setText(details[2])
        self.ui_mail.email_sender.setText(details[1])
        self.ui_mail.email_subject.setText(details[0])
        self.ui_mail.sender_password.setText(details[3])

    def get_details(self):
        path = 'C:\\ProgramData\\iLecturers\\data\\email_details\\detail.txt'
        if os.path.exists(path):
            with open(path,'r') as f:
                details = f.read().split(',')
            return details
   
