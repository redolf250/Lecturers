from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *

class SendThread(QRunnable):
    def __init__(self,details):
        super(SendThread,self).__init__()
        self.details = details

    def run(self):
        self.details()