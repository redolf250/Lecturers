from packages.pyqt import *

class SendThread(QRunnable):
    def __init__(self,details):
        super(SendThread,self).__init__()
        self.details = details

    def run(self):
        self.details()