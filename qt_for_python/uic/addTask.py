# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'addTask.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QGridLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 138)
        self.gridLayout_2 = QGridLayout(Dialog)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.widget = QWidget(Dialog)
        self.widget.setObjectName(u"widget")
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.companyName = QLineEdit(self.widget)
        self.companyName.setObjectName(u"companyName")

        self.gridLayout.addWidget(self.companyName, 0, 1, 1, 1)

        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.taskName = QLineEdit(self.widget)
        self.taskName.setObjectName(u"taskName")

        self.gridLayout.addWidget(self.taskName, 1, 1, 1, 1)

        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.taskNum = QLineEdit(self.widget)
        self.taskNum.setObjectName(u"taskNum")

        self.gridLayout.addWidget(self.taskNum, 2, 1, 1, 1)

        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)

        self.note = QLineEdit(self.widget)
        self.note.setObjectName(u"note")

        self.gridLayout.addWidget(self.note, 3, 1, 1, 1)


        self.gridLayout_2.addWidget(self.widget, 0, 0, 1, 1)

        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.yesBtn = QPushButton(self.frame)
        self.yesBtn.setObjectName(u"yesBtn")

        self.gridLayout_3.addWidget(self.yesBtn, 0, 0, 1, 1)

        self.quitBtn = QPushButton(self.frame)
        self.quitBtn.setObjectName(u"quitBtn")

        self.gridLayout_3.addWidget(self.quitBtn, 1, 0, 1, 1)


        self.gridLayout_2.addWidget(self.frame, 0, 1, 1, 1)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u6dfb\u52a0\u4efb\u52a1", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u5355\u4f4d\u540d\u79f0", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u4efb\u52a1\u540d\u79f0", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"\u4efb\u52a1\u7f16\u53f7", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"\u5907\u6ce8", None))
        self.yesBtn.setText(QCoreApplication.translate("Dialog", u"\u786e\u5b9a", None))
        self.quitBtn.setText(QCoreApplication.translate("Dialog", u"\u53d6\u6d88", None))
    # retranslateUi

