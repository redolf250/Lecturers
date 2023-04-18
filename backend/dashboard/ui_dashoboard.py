# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dashoboardeXqlQE.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt,QDateTime,QDate,QTime)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *

import asset_rc

class Ui_dashboard(object):
    def setupUi(self, dashboard):
        if dashboard.objectName():
            dashboard.setObjectName(u"dashboard")
        dashboard.resize(1339, 869)
        dashboard.setMinimumSize(QSize(1339, 869))
        dashboard.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.centralwidget = QWidget(dashboard)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(1200, 800))
        self.centralwidget.setStyleSheet(u"")
        self.drop_shadow_layout = QFrame(self.centralwidget)
        self.drop_shadow_layout.setObjectName(u"drop_shadow_layout")
        self.drop_shadow_layout.setGeometry(QRect(0, 0, 1361, 871))
        self.drop_shadow_layout.setMinimumSize(QSize(1200, 800))
        self.drop_shadow_layout.setStyleSheet(u"")
        self.drop_shadow_layout.setFrameShape(QFrame.NoFrame)
        self.drop_shadow_layout.setFrameShadow(QFrame.Raised)
        self.drop_shadow_layout.setLineWidth(0)
        self.content_layout = QVBoxLayout(self.drop_shadow_layout)
        self.content_layout.setSpacing(0)
        self.content_layout.setObjectName(u"content_layout")
        self.content_layout.setContentsMargins(0, 0, 20, 0)
        self.title_bar = QFrame(self.drop_shadow_layout)
        self.title_bar.setObjectName(u"title_bar")
        self.title_bar.setMinimumSize(QSize(0, 50))
        self.title_bar.setMaximumSize(QSize(16777215, 50))
        self.title_bar.setStyleSheet(u"\n"
"background-color: rgb(35, 35, 35);")
        self.title_bar.setFrameShape(QFrame.NoFrame)
        self.title_bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.title_bar)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 15, 0)
        self.other_fields = QFrame(self.title_bar)
        self.other_fields.setObjectName(u"other_fields")
        self.other_fields.setFrameShape(QFrame.NoFrame)
        self.other_fields.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.other_fields)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.logo = QFrame(self.other_fields)
        self.logo.setObjectName(u"logo")
        self.logo.setMinimumSize(QSize(5, 0))
        self.logo.setMaximumSize(QSize(60, 16777215))
        self.logo.setFrameShape(QFrame.NoFrame)
        self.logo.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.logo)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.logo)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(60, 0))
        self.label.setMaximumSize(QSize(60, 16777215))
        font = QFont()
        font.setFamily(u"Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"padding-left:5px;")
        self.label.setPixmap(QPixmap(u":/icons/asset/layers.svg"))
        self.label.setMargin(10)

        self.verticalLayout_2.addWidget(self.label)


        self.horizontalLayout_2.addWidget(self.logo)

        self.options = QFrame(self.other_fields)
        self.options.setObjectName(u"options")
        self.options.setFrameShape(QFrame.NoFrame)
        self.options.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.options)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.label_4 = QLabel(self.options)
        self.label_4.setObjectName(u"label_4")
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(False)
        font1.setWeight(50)
        self.label_4.setFont(font1)
        self.label_4.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"padding-left:5px;")

        self.horizontalLayout_19.addWidget(self.label_4)


        self.horizontalLayout_2.addWidget(self.options)


        self.horizontalLayout.addWidget(self.other_fields)

        self.controls_frame = QFrame(self.title_bar)
        self.controls_frame.setObjectName(u"controls_frame")
        self.controls_frame.setMinimumSize(QSize(87, 0))
        self.controls_frame.setMaximumSize(QSize(87, 16777215))
        self.controls_frame.setFrameShape(QFrame.NoFrame)
        self.controls_frame.setFrameShadow(QFrame.Raised)
        self.btn_maximize = QPushButton(self.controls_frame)
        self.btn_maximize.setObjectName(u"btn_maximize")
        self.btn_maximize.setGeometry(QRect(40, 20, 16, 16))
        self.btn_maximize.setMinimumSize(QSize(16, 16))
        self.btn_maximize.setMaximumSize(QSize(17, 17))
        self.btn_maximize.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(255, 170, 0);\n"
"	border:none;\n"
"	border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton:hover{	\n"
"	background-color: rgba(255, 170, 0,150);\n"
"	\n"
"}")
        self.btn_minimize = QPushButton(self.controls_frame)
        self.btn_minimize.setObjectName(u"btn_minimize")
        self.btn_minimize.setGeometry(QRect(10, 20, 16, 16))
        self.btn_minimize.setMinimumSize(QSize(16, 16))
        self.btn_minimize.setMaximumSize(QSize(17, 17))
        self.btn_minimize.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(85, 255, 127);\n"
"	border:none;\n"
"	border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton:hover{	\n"
"	background-color: rgba(85, 255, 127,150);\n"
"	\n"
"}")
        self.btn_close = QPushButton(self.controls_frame)
        self.btn_close.setObjectName(u"btn_close")
        self.btn_close.setGeometry(QRect(70, 20, 16, 16))
        self.btn_close.setMinimumSize(QSize(16, 16))
        self.btn_close.setMaximumSize(QSize(17, 17))
        self.btn_close.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255, 0, 0);\n"
"	border:none;\n"
"	border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton:hover{	\n"
"	background-color: rgba(255, 0, 0,150);\n"
"	\n"
"}")

        self.horizontalLayout.addWidget(self.controls_frame)


        self.content_layout.addWidget(self.title_bar)

        self.content = QFrame(self.drop_shadow_layout)
        self.content.setObjectName(u"content")
        self.content.setStyleSheet(u"background-color: rgb(45, 45, 45);")
        self.content.setFrameShape(QFrame.NoFrame)
        self.content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.content)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.menu_frame = QFrame(self.content)
        self.menu_frame.setObjectName(u"menu_frame")
        self.menu_frame.setMinimumSize(QSize(70, 0))
        self.menu_frame.setMaximumSize(QSize(80, 16777215))
        self.menu_frame.setStyleSheet(u"background-color: rgb(35, 35, 35);")
        self.menu_frame.setFrameShape(QFrame.NoFrame)
        self.menu_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.menu_frame)
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 3)
        self.frame = QFrame(self.menu_frame)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 350))
        self.frame.setMaximumSize(QSize(16777215, 300))
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, -1, 0, -1)
        self.btn_home = QPushButton(self.frame)
        self.btn_home.setObjectName(u"btn_home")
        self.btn_home.setMinimumSize(QSize(0, 70))
        self.btn_home.setMaximumSize(QSize(16777215, 70))
        self.btn_home.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	border: 0px solid;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border-left: 3px solid;\n"
"	border-left-color: rgb(0, 170, 255);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	border-left-color: 3px solid rgb(255, 255, 255);\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"")
        icon = QIcon()
        icon.addFile(u":/icons/asset/home.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_home.setIcon(icon)
        self.btn_home.setIconSize(QSize(40, 40))
        self.btn_home.setCheckable(True)
        self.btn_home.setChecked(False)
        self.btn_home.setFlat(True)

        self.verticalLayout.addWidget(self.btn_home)

        self.btn_search = QPushButton(self.frame)
        self.btn_search.setObjectName(u"btn_search")
        self.btn_search.setMinimumSize(QSize(0, 70))
        self.btn_search.setMaximumSize(QSize(16777215, 70))
        self.btn_search.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	border: 0px solid;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border-left: 3px solid;\n"
"	border-left-color: rgb(0, 170, 255);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	border-left-color: rgb(255, 255, 255);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/icons/asset/search.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_search.setIcon(icon1)
        self.btn_search.setIconSize(QSize(40, 40))
        self.btn_search.setCheckable(True)
        self.btn_search.setFlat(True)

        self.verticalLayout.addWidget(self.btn_search)

        self.btn_active_count = QPushButton(self.frame)
        self.btn_active_count.setObjectName(u"btn_active_count")
        self.btn_active_count.setMinimumSize(QSize(0, 70))
        self.btn_active_count.setMaximumSize(QSize(16777215, 70))
        self.btn_active_count.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	border: 0px solid;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border-left: 3px solid;\n"
"	border-left-color: rgb(0, 170, 255);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	border-left-color: rgb(255, 255, 255);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/icons/asset/users.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_active_count.setIcon(icon2)
        self.btn_active_count.setIconSize(QSize(40, 40))
        self.btn_active_count.setCheckable(True)
        self.btn_active_count.setFlat(True)

        self.verticalLayout.addWidget(self.btn_active_count)

        self.btn_send_mail = QPushButton(self.frame)
        self.btn_send_mail.setObjectName(u"btn_send_mail")
        self.btn_send_mail.setMinimumSize(QSize(0, 70))
        self.btn_send_mail.setMaximumSize(QSize(16777215, 70))
        self.btn_send_mail.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	border: 0px solid;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border-left: 3px solid;\n"
"	border-left-color: rgb(0, 170, 255);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	border-left-color: rgb(255, 255, 255);\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/icons/asset/mail.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_send_mail.setIcon(icon3)
        self.btn_send_mail.setIconSize(QSize(40, 40))
        self.btn_send_mail.setCheckable(True)
        self.btn_send_mail.setFlat(True)

        self.verticalLayout.addWidget(self.btn_send_mail)


        self.verticalLayout_3.addWidget(self.frame, 0, Qt.AlignTop)


        self.horizontalLayout_3.addWidget(self.menu_frame)

        self.content_frame = QFrame(self.content)
        self.content_frame.setObjectName(u"content_frame")
        self.content_frame.setFrameShape(QFrame.NoFrame)
        self.content_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.content_frame)
        self.verticalLayout_5.setSpacing(9)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 9, 0)
        self.stackedWidget = QStackedWidget(self.content_frame)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setMinimumSize(QSize(500, 0))
        self.stackedWidget.setStyleSheet(u"background-color: rgb(45, 45, 45);")
        self.home = QWidget()
        self.home.setObjectName(u"home")
        self.home.setMinimumSize(QSize(200, 0))
        self.horizontalLayout_4 = QHBoxLayout(self.home)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.left_frame = QFrame(self.home)
        self.left_frame.setObjectName(u"left_frame")
        self.left_frame.setMinimumSize(QSize(500, 0))
        self.left_frame.setMaximumSize(QSize(400, 16777215))
        self.left_frame.setStyleSheet(u"")
        self.left_frame.setFrameShape(QFrame.NoFrame)
        self.left_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.left_frame)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.info_frame = QFrame(self.left_frame)
        self.info_frame.setObjectName(u"info_frame")
        self.info_frame.setMinimumSize(QSize(0, 390))
        self.info_frame.setMaximumSize(QSize(16777215, 390))
        self.info_frame.setFrameShape(QFrame.NoFrame)
        self.info_frame.setFrameShadow(QFrame.Raised)
        self.image = QLabel(self.info_frame)
        self.image.setObjectName(u"image")
        self.image.setGeometry(QRect(20, 30, 251, 281))
        font2 = QFont()
        font2.setFamily(u"Arial")
        font2.setPointSize(14)
        font2.setBold(False)
        font2.setWeight(50)
        self.image.setFont(font2)
        self.image.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-radius: 10px;\n"
"}")
        self.image.setPixmap(QPixmap(u":/icons/asset/image.svg"))
        self.image.setAlignment(Qt.AlignCenter)
        self.firstname = QLabel(self.info_frame)
        self.firstname.setObjectName(u"firstname")
        self.firstname.setGeometry(QRect(280, 30, 201, 41))
        font3 = QFont()
        font3.setFamily(u"MS Shell Dlg 2")
        font3.setPointSize(10)
        font3.setBold(False)
        font3.setWeight(50)
        self.firstname.setFont(font3)
        self.firstname.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"\n"
"}")
        self.firstname.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.middlename = QLabel(self.info_frame)
        self.middlename.setObjectName(u"middlename")
        self.middlename.setGeometry(QRect(280, 90, 201, 41))
        self.middlename.setFont(font3)
        self.middlename.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"\n"
"}")
        self.middlename.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.lastname = QLabel(self.info_frame)
        self.lastname.setObjectName(u"lastname")
        self.lastname.setGeometry(QRect(280, 150, 201, 41))
        self.lastname.setFont(font3)
        self.lastname.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.lastname.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.refrence = QLabel(self.info_frame)
        self.refrence.setObjectName(u"refrence")
        self.refrence.setGeometry(QRect(280, 210, 201, 41))
        self.refrence.setFont(font3)
        self.refrence.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"\n"
"}")
        self.refrence.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.index = QLabel(self.info_frame)
        self.index.setObjectName(u"index")
        self.index.setGeometry(QRect(280, 270, 201, 41))
        self.index.setFont(font3)
        self.index.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"\n"
"}")
        self.index.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.program = QLabel(self.info_frame)
        self.program.setObjectName(u"program")
        self.program.setGeometry(QRect(20, 330, 461, 41))
        self.program.setFont(font3)
        self.program.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"\n"
"}")
        self.program.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.image_2 = QLabel(self.info_frame)
        self.image_2.setObjectName(u"image_2")
        self.image_2.setGeometry(QRect(10, 10, 481, 381))
        self.image_2.setFont(font2)
        self.image_2.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"}")
        self.image_2.setAlignment(Qt.AlignCenter)
        self.image_2.raise_()
        self.image.raise_()
        self.firstname.raise_()
        self.middlename.raise_()
        self.lastname.raise_()
        self.refrence.raise_()
        self.index.raise_()
        self.program.raise_()

        self.verticalLayout_6.addWidget(self.info_frame)

        self.frame_3 = QFrame(self.left_frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 530))
        self.frame_3.setMaximumSize(QSize(16777215, 530))
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.label_notification = QLabel(self.frame_3)
        self.label_notification.setObjectName(u"label_notification")
        self.label_notification.setGeometry(QRect(10, 310, 481, 111))
        self.label_notification.setFont(font3)
        self.label_notification.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"}")
        self.label_notification.setAlignment(Qt.AlignCenter)
        self.label_notification.setWordWrap(True)
        self.btn_connect_detect = QPushButton(self.frame_3)
        self.btn_connect_detect.setObjectName(u"btn_connect_detect")
        self.btn_connect_detect.setGeometry(QRect(200, 230, 131, 41))
        font4 = QFont()
        font4.setPointSize(10)
        self.btn_connect_detect.setFont(font4)
        self.btn_connect_detect.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border:none;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	border: 2px solid rgb(255,255,255);	\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/icons/asset/video.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_connect_detect.setIcon(icon4)
        self.btn_connect_detect.setIconSize(QSize(30, 30))
        self.btn_connect_detect.setFlat(True)
        self.btn_disconnect = QPushButton(self.frame_3)
        self.btn_disconnect.setObjectName(u"btn_disconnect")
        self.btn_disconnect.setGeometry(QRect(340, 230, 141, 41))
        self.btn_disconnect.setFont(font4)
        self.btn_disconnect.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border:none;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	border: 2px solid rgb(255,255,255);	\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u":/icons/asset/video-off.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_disconnect.setIcon(icon5)
        self.btn_disconnect.setIconSize(QSize(30, 30))
        self.btn_disconnect.setFlat(True)
        self.comboBox = QComboBox(self.frame_3)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(20, 230, 171, 38))
        self.comboBox.setMinimumSize(QSize(0, 38))
        self.comboBox.setMaximumSize(QSize(16777215, 38))
        self.comboBox.setFont(font4)
        self.comboBox.setStyleSheet(u"QComboBox{\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid rgb(45, 45, 45);\n"
"	padding-left:10px;\n"
"	border-radius: 5px;\n"
"}")
        self.comboBox.setFrame(False)
        self.firstname_23 = QLabel(self.frame_3)
        self.firstname_23.setObjectName(u"firstname_23")
        self.firstname_23.setGeometry(QRect(10, 190, 481, 101))
        font5 = QFont()
        font5.setFamily(u"Arial")
        font5.setPointSize(10)
        font5.setBold(False)
        font5.setWeight(50)
        self.firstname_23.setFont(font5)
        self.firstname_23.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"	padding-top:5px;\n"
"}")
        self.firstname_23.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.firstname_24 = QLabel(self.frame_3)
        self.firstname_24.setObjectName(u"firstname_24")
        self.firstname_24.setGeometry(QRect(10, 100, 481, 81))
        self.firstname_24.setFont(font5)
        self.firstname_24.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"}")
        self.firstname_24.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.btn_clear_label = QPushButton(self.frame_3)
        self.btn_clear_label.setObjectName(u"btn_clear_label")
        self.btn_clear_label.setGeometry(QRect(260, 120, 221, 41))
        self.btn_clear_label.setFont(font4)
        self.btn_clear_label.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border:none;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	border: 2px solid rgb(255,255,255);	\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u":/icons/asset/delete.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_clear_label.setIcon(icon6)
        self.btn_clear_label.setIconSize(QSize(30, 30))
        self.btn_clear_label.setFlat(True)
        self.btn_open_database = QPushButton(self.frame_3)
        self.btn_open_database.setObjectName(u"btn_open_database")
        self.btn_open_database.setGeometry(QRect(20, 120, 221, 41))
        self.btn_open_database.setFont(font4)
        self.btn_open_database.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border:none;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	border: 2px solid rgb(255,255,255);	\n"
"}")
        icon7 = QIcon()
        icon7.addFile(u":/icons/asset/database.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_open_database.setIcon(icon7)
        self.btn_open_database.setIconSize(QSize(30, 30))
        self.btn_open_database.setFlat(True)
        self.firstname_25 = QLabel(self.frame_3)
        self.firstname_25.setObjectName(u"firstname_25")
        self.firstname_25.setGeometry(QRect(10, 10, 481, 81))
        self.firstname_25.setFont(font5)
        self.firstname_25.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"}")
        self.firstname_25.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.database_tables = QComboBox(self.frame_3)
        self.database_tables.setObjectName(u"database_tables")
        self.database_tables.setGeometry(QRect(20, 30, 301, 38))
        self.database_tables.setMinimumSize(QSize(0, 38))
        self.database_tables.setMaximumSize(QSize(16777215, 38))
        self.database_tables.setFont(font4)
        self.database_tables.setStyleSheet(u"QComboBox{\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid rgb(45, 45, 45);\n"
"	padding-left:10px;\n"
"	border-radius: 5px;\n"
"}")
        self.database_tables.setFrame(False)
        self.btn_refresh = QPushButton(self.frame_3)
        self.btn_refresh.setObjectName(u"btn_refresh")
        self.btn_refresh.setGeometry(QRect(340, 30, 141, 41))
        self.btn_refresh.setFont(font4)
        self.btn_refresh.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border:none;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	border: 2px solid rgb(255,255,255);	\n"
"}")
        icon8 = QIcon()
        icon8.addFile(u":/icons/asset/refresh-cw.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_refresh.setIcon(icon8)
        self.btn_refresh.setIconSize(QSize(30, 30))
        self.btn_refresh.setFlat(True)
        self.firstname_23.raise_()
        self.label_notification.raise_()
        self.btn_connect_detect.raise_()
        self.btn_disconnect.raise_()
        self.comboBox.raise_()
        self.firstname_24.raise_()
        self.btn_clear_label.raise_()
        self.btn_open_database.raise_()
        self.firstname_25.raise_()
        self.database_tables.raise_()
        self.btn_refresh.raise_()

        self.verticalLayout_6.addWidget(self.frame_3)


        self.horizontalLayout_4.addWidget(self.left_frame)

        self.right_frame = QFrame(self.home)
        self.right_frame.setObjectName(u"right_frame")
        self.right_frame.setMinimumSize(QSize(0, 500))
        self.right_frame.setFrameShape(QFrame.NoFrame)
        self.right_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.right_frame)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.camera_frame = QFrame(self.right_frame)
        self.camera_frame.setObjectName(u"camera_frame")
        self.camera_frame.setMinimumSize(QSize(0, 570))
        self.camera_frame.setMaximumSize(QSize(16777215, 570))
        self.camera_frame.setFrameShape(QFrame.NoFrame)
        self.camera_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.camera_frame)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.camera_view = QLabel(self.camera_frame)
        self.camera_view.setObjectName(u"camera_view")
        self.camera_view.setMinimumSize(QSize(0, 0))
        self.camera_view.setMaximumSize(QSize(16777215, 16777215))
        self.camera_view.setFont(font2)
        self.camera_view.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"}")
        self.camera_view.setPixmap(QPixmap(u":/icons/asset/camera-off.svg"))
        self.camera_view.setAlignment(Qt.AlignCenter)
        self.camera_view.setWordWrap(True)

        self.verticalLayout_8.addWidget(self.camera_view)


        self.verticalLayout_7.addWidget(self.camera_frame)

        self.properties_frame = QFrame(self.right_frame)
        self.properties_frame.setObjectName(u"properties_frame")
        self.properties_frame.setMaximumSize(QSize(16777215, 400))
        self.properties_frame.setFrameShape(QFrame.NoFrame)
        self.properties_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.properties_frame)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.properties_frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 230))
        self.frame_2.setMaximumSize(QSize(16777215, 230))
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(0, 0))
        self.frame_4.setMaximumSize(QSize(370, 16777215))
        self.frame_4.setStyleSheet(u"QFrame{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"}")
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Plain)
        self.gridLayout_2 = QGridLayout(self.frame_4)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setVerticalSpacing(15)
        self.gridLayout_2.setContentsMargins(15, -1, -1, -1)
        self.label_14 = QLabel(self.frame_4)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMinimumSize(QSize(0, 20))
        self.label_14.setMaximumSize(QSize(16777215, 20))
        font6 = QFont()
        font6.setFamily(u"Arial")
        font6.setPointSize(10)
        self.label_14.setFont(font6)
        self.label_14.setStyleSheet(u"")
        self.label_14.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_14, 1, 0, 1, 3)

        self.brightness_value = QLabel(self.frame_4)
        self.brightness_value.setObjectName(u"brightness_value")
        self.brightness_value.setMinimumSize(QSize(50, 0))
        self.brightness_value.setMaximumSize(QSize(50, 16777215))
        self.brightness_value.setFont(font5)
        self.brightness_value.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"}")
        self.brightness_value.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.brightness_value, 4, 2, 1, 1)

        self.brightness_label = QLabel(self.frame_4)
        self.brightness_label.setObjectName(u"brightness_label")
        self.brightness_label.setFont(font5)
        self.brightness_label.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"}")
        self.brightness_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.brightness_label, 4, 0, 1, 1)

        self.brigthness = QSlider(self.frame_4)
        self.brigthness.setObjectName(u"brigthness")
        self.brigthness.setMaximum(100)
        self.brigthness.setValue(30)
        self.brigthness.setSliderPosition(30)
        self.brigthness.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.brigthness, 4, 1, 1, 1)

        self.sharpness = QSlider(self.frame_4)
        self.sharpness.setObjectName(u"sharpness")
        self.sharpness.setMaximum(100)
        self.sharpness.setValue(50)
        self.sharpness.setSliderPosition(50)
        self.sharpness.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.sharpness, 5, 1, 1, 1)

        self.sharp_label = QLabel(self.frame_4)
        self.sharp_label.setObjectName(u"sharp_label")
        self.sharp_label.setFont(font5)
        self.sharp_label.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"}")
        self.sharp_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.sharp_label, 5, 0, 1, 1)

        self.sharp_value = QLabel(self.frame_4)
        self.sharp_value.setObjectName(u"sharp_value")
        self.sharp_value.setMinimumSize(QSize(50, 0))
        self.sharp_value.setMaximumSize(QSize(50, 16777215))
        self.sharp_value.setFont(font5)
        self.sharp_value.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"}")
        self.sharp_value.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.sharp_value, 5, 2, 1, 1)

        self.contrast = QSlider(self.frame_4)
        self.contrast.setObjectName(u"contrast")
        self.contrast.setStyleSheet(u"QSlider:groove:horizontal{\n"
"	margin:2px;\n"
"	height:1px;\n"
"}\n"
"")
        self.contrast.setMaximum(100)
        self.contrast.setValue(60)
        self.contrast.setSliderPosition(60)
        self.contrast.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.contrast, 6, 1, 1, 1)

        self.contrast_label = QLabel(self.frame_4)
        self.contrast_label.setObjectName(u"contrast_label")
        self.contrast_label.setFont(font5)
        self.contrast_label.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"}")
        self.contrast_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.contrast_label, 6, 0, 1, 1)

        self.contrast_value = QLabel(self.frame_4)
        self.contrast_value.setObjectName(u"contrast_value")
        self.contrast_value.setMinimumSize(QSize(50, 0))
        self.contrast_value.setMaximumSize(QSize(50, 16777215))
        self.contrast_value.setFont(font5)
        self.contrast_value.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"}")
        self.contrast_value.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.contrast_value, 6, 2, 1, 1)


        self.horizontalLayout_10.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.frame_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(350, 0))
        self.frame_5.setMaximumSize(QSize(360, 16777215))
        self.frame_5.setStyleSheet(u"QFrame{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"}")
        self.frame_5.setFrameShape(QFrame.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Plain)
        self.label_18 = QLabel(self.frame_5)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(100, 20, 150, 20))
        self.label_18.setMinimumSize(QSize(0, 20))
        self.label_18.setMaximumSize(QSize(16777215, 20))
        self.label_18.setFont(font6)
        self.label_18.setStyleSheet(u"")
        self.label_18.setAlignment(Qt.AlignCenter)
        self.scan_range_label = QLabel(self.frame_5)
        self.scan_range_label.setObjectName(u"scan_range_label")
        self.scan_range_label.setGeometry(QRect(20, 150, 321, 51))
        self.scan_range_label.setFont(font3)
        self.scan_range_label.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-radius: 10px;\n"
"	padding-left:45px;\n"
"\n"
"}")
        self.scan_range_label.setAlignment(Qt.AlignCenter)
        self.label_42 = QLabel(self.frame_5)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setGeometry(QRect(30, 160, 31, 31))
        self.label_42.setStyleSheet(u"background-color: rgb(45, 45, 45);")
        self.label_42.setPixmap(QPixmap(u":/icons/asset/camera.svg"))
        self.btn_scan_range = QPushButton(self.frame_5)
        self.btn_scan_range.setObjectName(u"btn_scan_range")
        self.btn_scan_range.setGeometry(QRect(230, 70, 111, 51))
        self.btn_scan_range.setFont(font4)
        self.btn_scan_range.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border:none;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	border: 2px solid rgb(255,255,255);	\n"
"}")
        self.btn_scan_range.setIcon(icon1)
        self.btn_scan_range.setIconSize(QSize(30, 30))
        self.btn_scan_range.setFlat(True)
        self.scan_range = QLineEdit(self.frame_5)
        self.scan_range.setObjectName(u"scan_range")
        self.scan_range.setGeometry(QRect(20, 70, 201, 51))
        self.scan_range.setFont(font4)
        self.scan_range.setStyleSheet(u"QLineEdit{\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid  rgb(45, 45, 45);\n"
"	border-radius:10px;\n"
"	padding-left: 10px;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	border:2px solid rgb(35, 35, 35);\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	border:2px solid rgb(255, 255, 255);\n"
"}")
        self.scan_range.setClearButtonEnabled(True)

        self.horizontalLayout_10.addWidget(self.frame_5)


        self.verticalLayout_11.addWidget(self.frame_2)


        self.verticalLayout_7.addWidget(self.properties_frame)


        self.horizontalLayout_4.addWidget(self.right_frame)

        self.stackedWidget.addWidget(self.home)
        self.active = QWidget()
        self.active.setObjectName(u"active")
        self.verticalLayout_10 = QVBoxLayout(self.active)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.frame_10 = QFrame(self.active)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMinimumSize(QSize(0, 90))
        self.frame_10.setMaximumSize(QSize(16777215, 90))
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.label_31 = QLabel(self.frame_10)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setGeometry(QRect(0, 0, 1241, 81))
        font7 = QFont()
        font7.setFamily(u"Arial")
        font7.setPointSize(11)
        font7.setBold(True)
        font7.setWeight(75)
        self.label_31.setFont(font7)
        self.label_31.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"}")
        self.label_31.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.btn_active_load_data = QPushButton(self.frame_10)
        self.btn_active_load_data.setObjectName(u"btn_active_load_data")
        self.btn_active_load_data.setGeometry(QRect(310, 20, 141, 41))
        self.btn_active_load_data.setFont(font4)
        self.btn_active_load_data.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border:none;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	border: 2px solid rgb(255,255,255);	\n"
"}")
        icon9 = QIcon()
        icon9.addFile(u":/icons/asset/download.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_active_load_data.setIcon(icon9)
        self.btn_active_load_data.setIconSize(QSize(30, 30))
        self.btn_active_load_data.setFlat(True)
        self.database_tables_active = QComboBox(self.frame_10)
        self.database_tables_active.setObjectName(u"database_tables_active")
        self.database_tables_active.setGeometry(QRect(20, 20, 281, 41))
        self.database_tables_active.setMinimumSize(QSize(0, 41))
        self.database_tables_active.setMaximumSize(QSize(16777215, 38))
        self.database_tables_active.setFont(font4)
        self.database_tables_active.setStyleSheet(u"QComboBox{\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid rgb(45, 45, 45);\n"
"	padding-left:10px;\n"
"	border-radius: 5px;\n"
"}")
        self.database_tables_active.setFrame(False)
        self.active_count_filepath = QLineEdit(self.frame_10)
        self.active_count_filepath.setObjectName(u"active_count_filepath")
        self.active_count_filepath.setGeometry(QRect(650, 20, 421, 41))
        self.active_count_filepath.setFont(font4)
        self.active_count_filepath.setStyleSheet(u"QLineEdit{\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid  rgb(45, 45, 45);\n"
"	border-radius:10px;\n"
"	padding-left: 10px;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	border:2px solid rgb(35, 35, 35);\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	border:2px solid rgb(255, 255, 255);\n"
"}")
        self.active_count_filepath.setClearButtonEnabled(True)
        self.btn_active_count_save = QPushButton(self.frame_10)
        self.btn_active_count_save.setObjectName(u"btn_active_count_save")
        self.btn_active_count_save.setGeometry(QRect(1080, 20, 141, 41))
        self.btn_active_count_save.setFont(font4)
        self.btn_active_count_save.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border:none;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	border: 2px solid rgb(255,255,255);	\n"
"}")
        icon10 = QIcon()
        icon10.addFile(u":/icons/asset/save.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_active_count_save.setIcon(icon10)
        self.btn_active_count_save.setIconSize(QSize(30, 30))
        self.btn_active_count_save.setFlat(True)
        self.btn_load_refresh = QPushButton(self.frame_10)
        self.btn_load_refresh.setObjectName(u"btn_load_refresh")
        self.btn_load_refresh.setGeometry(QRect(470, 20, 141, 41))
        self.btn_load_refresh.setFont(font4)
        self.btn_load_refresh.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border:none;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	border: 2px solid rgb(255,255,255);	\n"
"}")
        self.btn_load_refresh.setIcon(icon8)
        self.btn_load_refresh.setIconSize(QSize(30, 30))
        self.btn_load_refresh.setFlat(True)

        self.verticalLayout_10.addWidget(self.frame_10)

        self.frame_11 = QFrame(self.active)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.NoFrame)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_11)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.tableWidget_count = QTableWidget(self.frame_11)
        if (self.tableWidget_count.columnCount() < 5):
            self.tableWidget_count.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font4);
        self.tableWidget_count.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font4);
        self.tableWidget_count.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font4);
        self.tableWidget_count.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font4);
        self.tableWidget_count.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font4);
        self.tableWidget_count.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tableWidget_count.setObjectName(u"tableWidget_count")
        self.tableWidget_count.setStyleSheet(u"QTableWidget{\n"
"	background-color: rgb(45, 45, 45);\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.tableWidget_count.setFrameShape(QFrame.NoFrame)
        self.tableWidget_count.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget_count.setSortingEnabled(True)
        self.tableWidget_count.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget_count.horizontalHeader().setDefaultSectionSize(230)
        self.tableWidget_count.horizontalHeader().setProperty("showSortIndicator", True)
        self.tableWidget_count.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_14.addWidget(self.tableWidget_count)


        self.verticalLayout_10.addWidget(self.frame_11)

        self.stackedWidget.addWidget(self.active)
        self.search = QWidget()
        self.search.setObjectName(u"search")
        self.verticalLayout_9 = QVBoxLayout(self.search)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.frame_6 = QFrame(self.search)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMinimumSize(QSize(0, 90))
        self.frame_6.setMaximumSize(QSize(16777215, 100))
        self.frame_6.setFrameShape(QFrame.NoFrame)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.search_box = QLineEdit(self.frame_6)
        self.search_box.setObjectName(u"search_box")
        self.search_box.setGeometry(QRect(10, 20, 181, 41))
        self.search_box.setFont(font4)
        self.search_box.setStyleSheet(u"QLineEdit{\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid  rgb(45, 45, 45);\n"
"	border-radius:10px;\n"
"	padding-left: 10px;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	border:2px solid rgb(35, 35, 35);\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	border:2px solid rgb(255, 255, 255);\n"
"}")
        self.search_box.setClearButtonEnabled(True)
        self.label_29 = QLabel(self.frame_6)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setGeometry(QRect(0, 0, 361, 81))
        self.label_29.setFont(font7)
        self.label_29.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"}")
        self.label_29.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.btn_search_page = QPushButton(self.frame_6)
        self.btn_search_page.setObjectName(u"btn_search_page")
        self.btn_search_page.setGeometry(QRect(210, 20, 131, 41))
        self.btn_search_page.setFont(font4)
        self.btn_search_page.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border:none;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	border: 2px solid rgb(255,255,255);	\n"
"}")
        self.btn_search_page.setIcon(icon1)
        self.btn_search_page.setIconSize(QSize(30, 30))
        self.btn_search_page.setFlat(True)
        self.label_30 = QLabel(self.frame_6)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setGeometry(QRect(750, 0, 491, 81))
        self.label_30.setFont(font7)
        self.label_30.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"}")
        self.label_30.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.filename = QLineEdit(self.frame_6)
        self.filename.setObjectName(u"filename")
        self.filename.setGeometry(QRect(760, 20, 201, 45))
        self.filename.setMinimumSize(QSize(0, 45))
        self.filename.setMaximumSize(QSize(16777215, 45))
        self.filename.setFont(font4)
        self.filename.setStyleSheet(u"QLineEdit{\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid  rgb(35, 35, 35);\n"
"	border-radius:15px;\n"
"	padding-left: 10px;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	border: 2px solid  rgb(45, 45, 45);\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	border:2px solid rgb(255, 255, 255);\n"
"}")
        self.filename.setInputMethodHints(Qt.ImhPreferNumbers)
        self.filename.setClearButtonEnabled(True)
        self.btn_csv = QPushButton(self.frame_6)
        self.btn_csv.setObjectName(u"btn_csv")
        self.btn_csv.setGeometry(QRect(970, 20, 121, 42))
        self.btn_csv.setMinimumSize(QSize(0, 42))
        self.btn_csv.setMaximumSize(QSize(16777215, 42))
        self.btn_csv.setFont(font4)
        self.btn_csv.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border:none;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	border: 2px solid rgb(255,255,255);	\n"
"}")
        icon11 = QIcon()
        icon11.addFile(u":/icons/asset/file.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_csv.setIcon(icon11)
        self.btn_csv.setIconSize(QSize(30, 30))
        self.btn_csv.setFlat(True)
        self.btn_backup = QPushButton(self.frame_6)
        self.btn_backup.setObjectName(u"btn_backup")
        self.btn_backup.setGeometry(QRect(1110, 20, 121, 41))
        self.btn_backup.setFont(font4)
        self.btn_backup.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border:none;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	border: 2px solid rgb(255,255,255);	\n"
"}")
        self.btn_backup.setIcon(icon7)
        self.btn_backup.setIconSize(QSize(30, 30))
        self.btn_backup.setFlat(True)
        self.label_32 = QLabel(self.frame_6)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setGeometry(QRect(370, 0, 371, 81))
        self.label_32.setFont(font7)
        self.label_32.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"}")
        self.label_32.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.report_date = QDateEdit(self.frame_6)
        self.report_date.setObjectName(u"report_date")
        self.report_date.setGeometry(QRect(410, 20, 141, 40))
        self.report_date.setMinimumSize(QSize(0, 40))
        self.report_date.setMaximumSize(QSize(16777215, 40))
        font8 = QFont()
        font8.setPointSize(12)
        font8.setBold(False)
        font8.setWeight(50)
        self.report_date.setFont(font8)
        self.report_date.setStyleSheet(u"QDateEdit{\n"
"	color: rgb(255, 255, 255);\n"
"background-color: rgb(45, 45, 45);\n"
"border: 2px solid rgb(45, 45, 45);\n"
"padding-left:10px;\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"")
        self.report_date.setFrame(False)
        self.report_date.setReadOnly(False)
        self.report_date.setButtonSymbols(QAbstractSpinBox.UpDownArrows)
        self.report_date.setAccelerated(True)
        self.report_date.setCorrectionMode(QAbstractSpinBox.CorrectToNearestValue)
        self.report_date.setProperty("showGroupSeparator", False)
        self.report_date.setDateTime(QDateTime(QDate(2023, 1, 1), QTime(0, 0, 0)))
        self.report_date.setMinimumDate(QDate(2023, 1, 1))
        self.report_date.setCalendarPopup(True)
        self.report_date.setTimeSpec(Qt.LocalTime)
        self.report_date.setDate(QDate(2023, 1, 1))
        self.database_tables_search = QComboBox(self.frame_6)
        self.database_tables_search.setObjectName(u"database_tables_search")
        self.database_tables_search.setGeometry(QRect(560, 20, 171, 40))
        self.database_tables_search.setMinimumSize(QSize(0, 40))
        self.database_tables_search.setMaximumSize(QSize(16777215, 38))
        self.database_tables_search.setFont(font4)
        self.database_tables_search.setStyleSheet(u"QComboBox{\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid rgb(45, 45, 45);\n"
"	padding-left:10px;\n"
"	border-radius: 5px;\n"
"}")
        self.database_tables_search.setFrame(False)
        self.search_by_date = QRadioButton(self.frame_6)
        self.search_by_date.setObjectName(u"search_by_date")
        self.search_by_date.setGeometry(QRect(380, 30, 21, 23))
        self.search_by_date.setFont(font6)
        self.search_by_date.setStyleSheet(u"QRadioButton{\n"
"	background-color: rgb(35, 35, 35);\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.label_29.raise_()
        self.search_box.raise_()
        self.btn_search_page.raise_()
        self.label_30.raise_()
        self.filename.raise_()
        self.btn_csv.raise_()
        self.btn_backup.raise_()
        self.label_32.raise_()
        self.report_date.raise_()
        self.database_tables_search.raise_()
        self.search_by_date.raise_()

        self.verticalLayout_9.addWidget(self.frame_6)

        self.frame_13 = QFrame(self.search)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_13)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, -1, 0, -1)
        self.tableWidget = QTableWidget(self.frame_13)
        if (self.tableWidget.columnCount() < 6):
            self.tableWidget.setColumnCount(6)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setFont(font1);
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setFont(font1);
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setFont(font4);
        __qtablewidgetitem7.setBackground(QColor(255, 255, 255));
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setFont(font4);
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        __qtablewidgetitem9.setFont(font4);
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        __qtablewidgetitem10.setFont(font4);
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem10)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setLayoutDirection(Qt.LeftToRight)
        self.tableWidget.setStyleSheet(u"QTableWidget{\n"
"	background-color: rgb(45, 45, 45);\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.tableWidget.setFrameShape(QFrame.NoFrame)
        self.tableWidget.setFrameShadow(QFrame.Plain)
        self.tableWidget.setAutoScrollMargin(5)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget.setSortingEnabled(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(60)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(200)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(True)
        self.tableWidget.verticalHeader().setMinimumSectionSize(30)
        self.tableWidget.verticalHeader().setDefaultSectionSize(40)
        self.tableWidget.verticalHeader().setProperty("showSortIndicator", True)
        self.tableWidget.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_12.addWidget(self.tableWidget)


        self.verticalLayout_9.addWidget(self.frame_13)

        self.stackedWidget.addWidget(self.search)
        self.mail = QWidget()
        self.mail.setObjectName(u"mail")
        self.mail.setMinimumSize(QSize(1262, 0))
        self.mail.setMaximumSize(QSize(1262, 950))
        self.verticalLayout_4 = QVBoxLayout(self.mail)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(-1, -1, 0, -1)
        self.frame_8 = QFrame(self.mail)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_9 = QFrame(self.frame_8)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setStyleSheet(u"")
        self.frame_9.setFrameShape(QFrame.NoFrame)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_9)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 5, 0)
        self.frame_7 = QFrame(self.frame_9)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(0, 90))
        self.frame_7.setMaximumSize(QSize(16777215, 100))
        self.frame_7.setStyleSheet(u"")
        self.frame_7.setFrameShape(QFrame.NoFrame)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.label_notification_2 = QLabel(self.frame_7)
        self.label_notification_2.setObjectName(u"label_notification_2")
        self.label_notification_2.setGeometry(QRect(0, 0, 891, 81))
        self.label_notification_2.setFont(font3)
        self.label_notification_2.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"padding-left:10px;\n"
"}")
        self.label_notification_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label_notification_2.setWordWrap(True)
        self.label_notification_3 = QLabel(self.frame_7)
        self.label_notification_3.setObjectName(u"label_notification_3")
        self.label_notification_3.setGeometry(QRect(920, 0, 321, 81))
        self.label_notification_3.setFont(font3)
        self.label_notification_3.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"}")
        self.label_notification_3.setAlignment(Qt.AlignCenter)
        self.label_notification_3.setWordWrap(True)
        self.student_data = QLineEdit(self.frame_7)
        self.student_data.setObjectName(u"student_data")
        self.student_data.setGeometry(QRect(20, 20, 371, 45))
        self.student_data.setMinimumSize(QSize(0, 45))
        self.student_data.setMaximumSize(QSize(16777215, 45))
        self.student_data.setFont(font4)
        self.student_data.setStyleSheet(u"QLineEdit{\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid  rgb(45, 45, 45);\n"
"	border-radius:10px;\n"
"	padding-left: 10px;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	border:2px solid rgb(35, 35, 35);\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	border:2px solid rgb(255, 255, 255);\n"
"}")
        self.student_data.setClearButtonEnabled(True)
        self.btn_load_data = QPushButton(self.frame_7)
        self.btn_load_data.setObjectName(u"btn_load_data")
        self.btn_load_data.setGeometry(QRect(410, 20, 121, 45))
        self.btn_load_data.setMinimumSize(QSize(0, 45))
        self.btn_load_data.setMaximumSize(QSize(16777215, 45))
        self.btn_load_data.setFont(font4)
        self.btn_load_data.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border:none;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	border: 2px solid rgb(255,255,255);	\n"
"}")
        icon12 = QIcon()
        icon12.addFile(u":/icons/asset/upload.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_load_data.setIcon(icon12)
        self.btn_load_data.setIconSize(QSize(30, 30))
        self.btn_load_data.setFlat(True)
        self.btn_send_qr_mail = QPushButton(self.frame_7)
        self.btn_send_qr_mail.setObjectName(u"btn_send_qr_mail")
        self.btn_send_qr_mail.setGeometry(QRect(550, 20, 131, 45))
        self.btn_send_qr_mail.setMinimumSize(QSize(0, 45))
        self.btn_send_qr_mail.setMaximumSize(QSize(16777215, 45))
        self.btn_send_qr_mail.setFont(font4)
        self.btn_send_qr_mail.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border:none;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	border: 2px solid rgb(255,255,255);	\n"
"}")
        icon13 = QIcon()
        icon13.addFile(u":/icons/asset/send.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_send_qr_mail.setIcon(icon13)
        self.btn_send_qr_mail.setIconSize(QSize(30, 30))
        self.btn_send_qr_mail.setFlat(True)
        self.btn_sender_details = QPushButton(self.frame_7)
        self.btn_sender_details.setObjectName(u"btn_sender_details")
        self.btn_sender_details.setGeometry(QRect(700, 20, 171, 45))
        self.btn_sender_details.setMinimumSize(QSize(0, 45))
        self.btn_sender_details.setMaximumSize(QSize(16777215, 45))
        self.btn_sender_details.setFont(font4)
        self.btn_sender_details.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border:none;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	border: 2px solid rgb(255,255,255);	\n"
"}")
        self.btn_sender_details.setIcon(icon3)
        self.btn_sender_details.setIconSize(QSize(30, 30))
        self.btn_sender_details.setFlat(True)

        self.verticalLayout_13.addWidget(self.frame_7)

        self.frame_12 = QFrame(self.frame_9)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.NoFrame)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_12)
        self.verticalLayout_15.setSpacing(3)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.load_mail_data_table = QTableWidget(self.frame_12)
        if (self.load_mail_data_table.columnCount() < 5):
            self.load_mail_data_table.setColumnCount(5)
        __qtablewidgetitem11 = QTableWidgetItem()
        __qtablewidgetitem11.setFont(font4);
        self.load_mail_data_table.setHorizontalHeaderItem(0, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        __qtablewidgetitem12.setFont(font4);
        self.load_mail_data_table.setHorizontalHeaderItem(1, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        __qtablewidgetitem13.setFont(font4);
        self.load_mail_data_table.setHorizontalHeaderItem(2, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        __qtablewidgetitem14.setFont(font4);
        self.load_mail_data_table.setHorizontalHeaderItem(3, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        __qtablewidgetitem15.setFont(font4);
        self.load_mail_data_table.setHorizontalHeaderItem(4, __qtablewidgetitem15)
        self.load_mail_data_table.setObjectName(u"load_mail_data_table")
        self.load_mail_data_table.setStyleSheet(u"QTableWidget{\n"
"	background-color: rgb(45, 45, 45);\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.load_mail_data_table.setFrameShape(QFrame.NoFrame)
        self.load_mail_data_table.setFrameShadow(QFrame.Plain)
        self.load_mail_data_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.load_mail_data_table.horizontalHeader().setDefaultSectionSize(230)
        self.load_mail_data_table.horizontalHeader().setProperty("showSortIndicator", True)
        self.load_mail_data_table.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_15.addWidget(self.load_mail_data_table)


        self.verticalLayout_13.addWidget(self.frame_12)


        self.horizontalLayout_6.addWidget(self.frame_9)


        self.verticalLayout_4.addWidget(self.frame_8)

        self.stackedWidget.addWidget(self.mail)

        self.verticalLayout_5.addWidget(self.stackedWidget)


        self.horizontalLayout_3.addWidget(self.content_frame)


        self.content_layout.addWidget(self.content)

        self.btn_send_mail_2 = QPushButton(self.centralwidget)
        self.btn_send_mail_2.setObjectName(u"btn_send_mail_2")
        self.btn_send_mail_2.setGeometry(QRect(0, 800, 70, 70))
        self.btn_send_mail_2.setMinimumSize(QSize(0, 70))
        self.btn_send_mail_2.setMaximumSize(QSize(16777215, 70))
        self.btn_send_mail_2.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 0px solid;\n"
"}\n"
"")
        icon14 = QIcon()
        icon14.addFile(u":/icons/asset/help-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_send_mail_2.setIcon(icon14)
        self.btn_send_mail_2.setIconSize(QSize(40, 40))
        self.btn_send_mail_2.setCheckable(True)
        self.btn_send_mail_2.setFlat(True)
        dashboard.setCentralWidget(self.centralwidget)
#if QT_CONFIG(shortcut)
#endif // QT_CONFIG(shortcut)

        self.retranslateUi(dashboard)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(dashboard)
    # setupUi

    def retranslateUi(self, dashboard):
        dashboard.setWindowTitle(QCoreApplication.translate("dashboard", u"MainWindow", None))
        self.label.setText("")
        self.label_4.setText(QCoreApplication.translate("dashboard", u"iAttend", None))
        self.btn_maximize.setText("")
        self.btn_minimize.setText("")
        self.btn_close.setText("")
        self.btn_home.setText("")
        self.btn_search.setText("")
        self.btn_active_count.setText("")
        self.btn_send_mail.setText("")
        self.image.setText("")
        self.firstname.setText(QCoreApplication.translate("dashboard", u"Firstname", None))
        self.middlename.setText(QCoreApplication.translate("dashboard", u"Othername", None))
        self.lastname.setText(QCoreApplication.translate("dashboard", u"Lastname", None))
        self.refrence.setText(QCoreApplication.translate("dashboard", u"Reference", None))
        self.index.setText(QCoreApplication.translate("dashboard", u"Index", None))
        self.program.setText(QCoreApplication.translate("dashboard", u"Program", None))
        self.image_2.setText("")
        self.label_notification.setText(QCoreApplication.translate("dashboard", u"Notification", None))
        self.btn_connect_detect.setText(QCoreApplication.translate("dashboard", u"Connect", None))
        self.btn_disconnect.setText(QCoreApplication.translate("dashboard", u"Disconnect", None))
        self.firstname_23.setText(QCoreApplication.translate("dashboard", u"Camera", None))
        self.firstname_24.setText("")
        self.btn_clear_label.setText(QCoreApplication.translate("dashboard", u"Reset", None))
        self.btn_open_database.setText(QCoreApplication.translate("dashboard", u"Create table", None))
        self.firstname_25.setText("")
        self.btn_refresh.setText(QCoreApplication.translate("dashboard", u"Refresh", None))
        self.camera_view.setText("")
        self.label_14.setText(QCoreApplication.translate("dashboard", u"Image Enhancement", None))
        self.brightness_value.setText(QCoreApplication.translate("dashboard", u"0", None))
        self.brightness_label.setText(QCoreApplication.translate("dashboard", u"Brigthness", None))
        self.sharp_label.setText(QCoreApplication.translate("dashboard", u"Sharpness", None))
        self.sharp_value.setText(QCoreApplication.translate("dashboard", u"0", None))
        self.contrast_label.setText(QCoreApplication.translate("dashboard", u"Contrast", None))
        self.contrast_value.setText(QCoreApplication.translate("dashboard", u"0", None))
        self.label_18.setText(QCoreApplication.translate("dashboard", u"Camera Scan", None))
        self.scan_range_label.setText("")
        self.label_42.setText("")
        self.btn_scan_range.setText(QCoreApplication.translate("dashboard", u"Scan", None))
        self.scan_range.setPlaceholderText(QCoreApplication.translate("dashboard", u"Scan range ?", None))
        self.label_31.setText("")
        self.btn_active_load_data.setText(QCoreApplication.translate("dashboard", u"Load", None))
        self.active_count_filepath.setPlaceholderText(QCoreApplication.translate("dashboard", u"Filename?", None))
        self.btn_active_count_save.setText(QCoreApplication.translate("dashboard", u"Save", None))
        self.btn_load_refresh.setText(QCoreApplication.translate("dashboard", u"Refresh", None))
        ___qtablewidgetitem = self.tableWidget_count.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("dashboard", u"Name", None));
        ___qtablewidgetitem1 = self.tableWidget_count.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("dashboard", u"Index", None));
        ___qtablewidgetitem2 = self.tableWidget_count.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("dashboard", u"Reference", None));
        ___qtablewidgetitem3 = self.tableWidget_count.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("dashboard", u"Program", None));
        ___qtablewidgetitem4 = self.tableWidget_count.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("dashboard", u"Appearance", None));
        self.search_box.setPlaceholderText(QCoreApplication.translate("dashboard", u"Reference here?", None))
        self.label_29.setText("")
        self.btn_search_page.setText(QCoreApplication.translate("dashboard", u"Search", None))
        self.label_30.setText("")
        self.filename.setPlaceholderText(QCoreApplication.translate("dashboard", u"Filename?", None))
        self.btn_csv.setText(QCoreApplication.translate("dashboard", u"Export", None))
        self.btn_backup.setText(QCoreApplication.translate("dashboard", u"Backup", None))
        self.label_32.setText("")
        self.report_date.setDisplayFormat(QCoreApplication.translate("dashboard", u"yyyy-MM-dd", None))
        self.search_by_date.setText("")
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("dashboard", u"Name", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("dashboard", u"Index", None));
        ___qtablewidgetitem7 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("dashboard", u"Reference", None));
        ___qtablewidgetitem8 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("dashboard", u"Program", None));
        ___qtablewidgetitem9 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("dashboard", u"Date Stamp", None));
        ___qtablewidgetitem10 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("dashboard", u"Time Stamp", None));
        self.label_notification_2.setText("")
        self.label_notification_3.setText(QCoreApplication.translate("dashboard", u"Notification", None))
        self.student_data.setText("")
        self.student_data.setPlaceholderText(QCoreApplication.translate("dashboard", u"Filename?", None))
        self.btn_load_data.setText(QCoreApplication.translate("dashboard", u"Browse", None))
        self.btn_send_qr_mail.setText(QCoreApplication.translate("dashboard", u"Send mail", None))
        self.btn_sender_details.setText(QCoreApplication.translate("dashboard", u"Sender details", None))
        ___qtablewidgetitem11 = self.load_mail_data_table.horizontalHeaderItem(0)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("dashboard", u"Name", None));
        ___qtablewidgetitem12 = self.load_mail_data_table.horizontalHeaderItem(1)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("dashboard", u"Index", None));
        ___qtablewidgetitem13 = self.load_mail_data_table.horizontalHeaderItem(2)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("dashboard", u"Reference", None));
        ___qtablewidgetitem14 = self.load_mail_data_table.horizontalHeaderItem(3)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("dashboard", u"Program", None));
        ___qtablewidgetitem15 = self.load_mail_data_table.horizontalHeaderItem(4)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("dashboard", u"Email", None));
        self.btn_send_mail_2.setText("")
    # retranslateUi

