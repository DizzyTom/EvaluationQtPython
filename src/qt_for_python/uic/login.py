# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)
import resource_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(480, 640)
        icon = QIcon()
        icon.addFile(u":/images/images/\u8ba1\u7b97\u673a.png", QSize(), QIcon.Normal, QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setStyleSheet(u"")
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(24, 9, 24, 9)
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"QPushButton {\n"
"    background-color: #ffffff;\n"
"    border: 1px solid #dcdfe6;\n"
"    padding: 10px;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #ecf5ff;\n"
"    color: #409eff;\n"
"}\n"
"\n"
"QPushButton:pressed, QPushButton:checked {\n"
"    border: 1px solid #3a8ee6;\n"
"    color: #409eff;\n"
"}\n"
"\n"
"QLineEdit{\n"
"    font-size:13px;\n"
"    background:transparent;\n"
"    border:none;\n"
"    border-bottom:1px solid rgb(229, 229, 229);\n"
"}\n"
" \n"
"QLineEdit:hover{\n"
"    border-bottom:1px solid rgb(193,193, 193);\n"
"}\n"
" \n"
"QLineEdit:focus{\n"
"    border-bottom:1px solid rgb(18, 183, 245);\n"
"}")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(50, -1, 50, -1)
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.widget_2 = QWidget(self.widget)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.gridLayout = QGridLayout(self.widget_2)
        self.gridLayout.setSpacing(20)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.widget_2)
        self.label.setObjectName(u"label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        self.label.setMinimumSize(QSize(25, 25))
        self.label.setStyleSheet(u"image: url(:/images/images/\u7528\u6237.png);")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.port = QLineEdit(self.widget_2)
        self.port.setObjectName(u"port")

        self.gridLayout.addWidget(self.port, 3, 1, 1, 2)

        self.label_3 = QLabel(self.widget_2)
        self.label_3.setObjectName(u"label_3")
        sizePolicy1.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy1)
        self.label_3.setMinimumSize(QSize(25, 25))
        self.label_3.setStyleSheet(u"image: url(:/images/images/IP.png);")

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.label_4 = QLabel(self.widget_2)
        self.label_4.setObjectName(u"label_4")
        sizePolicy1.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy1)
        self.label_4.setMinimumSize(QSize(25, 25))
        self.label_4.setStyleSheet(u"image: url(:/images/images/\u7aef\u53e3\u914d\u7f6e.png);\n"
"border-width:2px;")

        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)

        self.name = QLineEdit(self.widget_2)
        self.name.setObjectName(u"name")
        self.name.setMaxLength(20)
        self.name.setFrame(True)

        self.gridLayout.addWidget(self.name, 0, 1, 1, 2)

        self.label_2 = QLabel(self.widget_2)
        self.label_2.setObjectName(u"label_2")
        sizePolicy1.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy1)
        self.label_2.setMinimumSize(QSize(25, 25))
        self.label_2.setStyleSheet(u"image: url(:/images/images/\u5bc6\u7801.png);\n"
"border-width:2px;")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.ip = QLineEdit(self.widget_2)
        self.ip.setObjectName(u"ip")

        self.gridLayout.addWidget(self.ip, 2, 1, 1, 2)

        self.password = QLineEdit(self.widget_2)
        self.password.setObjectName(u"password")
        self.password.setEchoMode(QLineEdit.Password)

        self.gridLayout.addWidget(self.password, 1, 1, 1, 2)


        self.verticalLayout.addWidget(self.widget_2)

        self.widget_3 = QWidget(self.widget)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setMinimumSize(QSize(0, 40))
        self.horizontalLayout_2 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.login = QPushButton(self.widget_3)
        self.login.setObjectName(u"login")

        self.horizontalLayout_2.addWidget(self.login)

        self.quit = QPushButton(self.widget_3)
        self.quit.setObjectName(u"quit")

        self.horizontalLayout_2.addWidget(self.quit)


        self.verticalLayout.addWidget(self.widget_3)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)


        self.horizontalLayout.addWidget(self.widget)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u767b\u5f55", None))
        self.label.setText("")
        self.port.setInputMask("")
        self.port.setPlaceholderText(QCoreApplication.translate("Form", u"\u7aef\u53e3\u53f7", None))
#if QT_CONFIG(whatsthis)
        self.label_3.setWhatsThis(QCoreApplication.translate("Form", u"<html><head/><body><p>\u8bf7\u8f93\u5165\u670d\u52a1\u5668\u7684IP\u5730\u5740</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.label_3.setText("")
#if QT_CONFIG(whatsthis)
        self.label_4.setWhatsThis(QCoreApplication.translate("Form", u"<html><head/><body><p>\u8bf7\u8f93\u5165\u8fde\u63a5\u670d\u52a1\u5668\u7684\u7aef\u53e3\u53f7</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.label_4.setText("")
        self.name.setPlaceholderText(QCoreApplication.translate("Form", u"\u7528\u6237\u540d", None))
        self.label_2.setText("")
        self.ip.setInputMask("")
        self.ip.setPlaceholderText(QCoreApplication.translate("Form", u"IP\u5730\u5740", None))
        self.password.setPlaceholderText(QCoreApplication.translate("Form", u"\u5bc6\u7801", None))
        self.login.setText(QCoreApplication.translate("Form", u"\u767b\u5f55", None))
        self.quit.setText(QCoreApplication.translate("Form", u"\u9000\u51fa", None))
    # retranslateUi

