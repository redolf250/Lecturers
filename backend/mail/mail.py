from packages.pyqt import *
from packages.system import *
from packages.ui_files import *

class Mail(QDialog):
    def __init__(self):
        QDialog.__init__(self)
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
        details=self.load_data('C:\\ProgramData\\iLecturers\\email_details\\details.json')
        self.ui_mail.email_from.setText(details['sender'])
        self.ui_mail.email_sender.setText(details['mail'])
        self.ui_mail.email_subject.setText(details['subject'])
        self.ui_mail.sender_password.setText(details['password'])

    def load_data(self,resource_path):
        with open(resource_path,'r') as f:
            data = f.read()
            try:
                return json.loads(data)
            except Exception as e:
                pass

