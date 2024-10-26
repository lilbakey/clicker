# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6 import QtCore
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDateTimeEdit, QHBoxLayout, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)
import res_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(500, 390)
        MainWindow.setMinimumSize(QSize(0, 0))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.record_button = QPushButton(self.centralwidget)
        self.record_button.setObjectName(u"record_button")
        self.record_button.setMinimumSize(QSize(480, 100))
        self.record_button.setStyleSheet(u"QPushButton {\n"
"font-size:20px;\n"
"background-color: rgb(255, 255, 255);\n"
"border: 2px solid rgb(0, 0, 0);\n"
"border-radius: 7px;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"background-color: rgb(224, 238, 249);\n"
"}\n"
"\n"
"QPushButton::pressed {\n"
"background-color: rgba(224, 238, 249, 70);\n"
"}")
        icon = QIcon()
        icon.addFile(u":/icon/icons/radio_button_checked_FILL0_wght400_GRAD0_opsz48.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.record_button.setIcon(icon)
        self.record_button.setIconSize(QSize(25, 25))

        self.verticalLayout.addWidget(self.record_button)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.time_edit = QDateTimeEdit(self.centralwidget)
        self.time_edit.setObjectName(u"time_edit")
        self.time_edit.setMinimumSize(QSize(70, 50))
        self.time_edit.setStyleSheet(u"QDateTimeEdit\n"
"{\n"
"font-size: 20px;\n"
"border : 2px solid black;\n"
"background-color : white;\n"
"}\n"
"\n"
"QDateTimeEdit::up-arrow\n"
"{\n"
"width: 2px;\n"
"height: 2px;\n"
"}\n"
"QDateTimeEdit::down-arrow\n"
"{\n"
"width: 2px;\n"
"height: 2px;\n"
"}")

        self.horizontalLayout.addWidget(self.time_edit)

        self.save_time_button = QPushButton(self.centralwidget)
        self.save_time_button.setObjectName(u"save_time_button")
        self.save_time_button.setMinimumSize(QSize(50, 50))
        self.save_time_button.setStyleSheet(u"QPushButton {\n"
"font-size:20px;\n"
"background-color: rgb(255, 255, 255);\n"
"border: 2px solid rgb(0, 0, 0);\n"
"border-radius: 7px;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"background-color: rgb(224, 238, 249);\n"
"}\n"
"\n"
"QPushButton::pressed {\n"
"background-color: rgba(224, 238, 249, 70);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/icon/icons/save_FILL0_wght400_GRAD0_opsz48.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.save_time_button.setIcon(icon1)
        self.save_time_button.setIconSize(QSize(25, 25))

        self.horizontalLayout.addWidget(self.save_time_button)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.start_button = QPushButton(self.centralwidget)
        self.start_button.setObjectName(u"start_button")
        self.start_button.setMinimumSize(QSize(300, 100))
        self.start_button.setStyleSheet(u"QPushButton {\n"
"font-size:20px;\n"
"background-color: rgb(255, 255, 255);\n"
"border: 2px solid rgb(0, 0, 0);\n"
"border-radius: 7px;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"background-color: rgb(224, 238, 249);\n"
"}\n"
"\n"
"QPushButton::pressed {\n"
"background-color: rgba(224, 238, 249, 70);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/icon/icons/start_FILL0_wght400_GRAD0_opsz48.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.start_button.setIcon(icon2)
        self.start_button.setIconSize(QSize(25, 25))

        self.verticalLayout.addWidget(self.start_button)

        self.status_info = QLineEdit(self.centralwidget)
        self.status_info.setReadOnly(True)
        self.status_info.setAlignment(QtCore.Qt.AlignCenter)
        self.status_info.setObjectName(u"status_info")
        self.status_info.setMinimumSize(QSize(300, 100))
        self.status_info.setStyleSheet(u"QLineEdit {\n"
"font-size: 17px;\n"
"border: 2px solid rgb(0, 0, 0);\n"
"border-radius: 7px;\n"
"}")

        self.verticalLayout.addWidget(self.status_info)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Clicker", None))
        self.record_button.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043f\u0443\u0441\u0442\u0438\u0442\u044c \u0437\u0430\u043f\u0438\u0441\u044c", None))
        self.save_time_button.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u0432\u0440\u0435\u043c\u044f", None))
        self.start_button.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043f\u0443\u0441\u0442\u0438\u0442\u044c \u043a\u043b\u0438\u043a\u0435\u0440", None))
        self.status_info.setText("")
    # retranslateUi

