# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGraphicsView,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QListWidget, QListWidgetItem, QMainWindow,
    QPushButton, QScrollArea, QSizePolicy, QSpacerItem,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)
import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1680, 1002)
        MainWindow.setMinimumSize(QSize(0, 20))
        icon = QIcon()
        icon.addFile(u":/icons/res/icons/\u8ba1\u7b97\u673a.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(1)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.menubar = QWidget(self.centralwidget)
        self.menubar.setObjectName(u"menubar")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.menubar.sizePolicy().hasHeightForWidth())
        self.menubar.setSizePolicy(sizePolicy)
        self.menubar.setMinimumSize(QSize(0, 20))
        self.menubar.setMaximumSize(QSize(16777215, 20))
        self.menubar.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.horizontalLayout = QHBoxLayout(self.menubar)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButton = QPushButton(self.menubar)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy1)
        self.pushButton.setMinimumSize(QSize(80, 0))
        self.pushButton.setMaximumSize(QSize(80, 16777215))
        self.pushButton.setStyleSheet(u"border:none")

        self.horizontalLayout.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.menubar)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy1.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy1)
        self.pushButton_2.setMinimumSize(QSize(80, 0))
        self.pushButton_2.setMaximumSize(QSize(80, 16777215))
        self.pushButton_2.setStyleSheet(u"border:none")

        self.horizontalLayout.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.menubar)
        self.pushButton_3.setObjectName(u"pushButton_3")
        sizePolicy1.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy1)
        self.pushButton_3.setMinimumSize(QSize(80, 0))
        self.pushButton_3.setMaximumSize(QSize(80, 16777215))
        self.pushButton_3.setStyleSheet(u"border:none")

        self.horizontalLayout.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(self.menubar)
        self.pushButton_4.setObjectName(u"pushButton_4")
        sizePolicy1.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy1)
        self.pushButton_4.setMinimumSize(QSize(80, 0))
        self.pushButton_4.setMaximumSize(QSize(80, 16777215))
        self.pushButton_4.setStyleSheet(u"border:none")

        self.horizontalLayout.addWidget(self.pushButton_4)

        self.pushButton_5 = QPushButton(self.menubar)
        self.pushButton_5.setObjectName(u"pushButton_5")
        sizePolicy1.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy1)
        self.pushButton_5.setMinimumSize(QSize(80, 0))
        self.pushButton_5.setMaximumSize(QSize(80, 16777215))
        self.pushButton_5.setStyleSheet(u"border:none")

        self.horizontalLayout.addWidget(self.pushButton_5)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout.addWidget(self.menubar)

        self.toolbar = QWidget(self.centralwidget)
        self.toolbar.setObjectName(u"toolbar")
        self.toolbar.setMinimumSize(QSize(0, 142))
        self.toolbar.setMaximumSize(QSize(16777215, 142))
        self.toolbar.setStyleSheet(u"QWidget{background-color: rgb(245, 245, 245);}\n"
"QFrame{background-color: rgb(255, 255, 255);border:none;}\n"
"")
        self.horizontalLayout_2 = QHBoxLayout(self.toolbar)
        self.horizontalLayout_2.setSpacing(2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 24)
        self.frame = QFrame(self.toolbar)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(106, 0))
        self.frame.setMaximumSize(QSize(106, 16777215))
        self.frame.setStyleSheet(u"QLabel{\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"QLabel:hover{\n"
"	background-color: rgb(255, 255, 127);\n"
"}\n"
"QWidget{\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.widget_7 = QWidget(self.frame)
        self.widget_7.setObjectName(u"widget_7")
        self.gridLayout_4 = QGridLayout(self.widget_7)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.widget_7)
        self.label_5.setObjectName(u"label_5")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy2)
        self.label_5.setMinimumSize(QSize(0, 35))
        self.label_5.setStyleSheet(u"image: url(:/icons/res/icons/\u91cd\u590d\u7247\u68c0\u7d22.png);")
        self.label_5.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_5, 0, 0, 1, 1)

        self.label_4 = QLabel(self.widget_7)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(16777215, 30))
        font = QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setAlignment(Qt.AlignCenter)
        self.label_4.setWordWrap(True)

        self.gridLayout_4.addWidget(self.label_4, 1, 0, 1, 1)


        self.gridLayout_2.addWidget(self.widget_7, 0, 1, 1, 1)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 20))
        self.label.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label, 1, 0, 1, 2)

        self.widget_6 = QWidget(self.frame)
        self.widget_6.setObjectName(u"widget_6")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.widget_6.sizePolicy().hasHeightForWidth())
        self.widget_6.setSizePolicy(sizePolicy3)
        self.widget_6.setMinimumSize(QSize(53, 0))
        self.widget_6.setMaximumSize(QSize(53, 16777215))
        self.widget_6.setStyleSheet(u"")
        self.gridLayout_3 = QGridLayout(self.widget_6)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.widget_6)
        self.label_2.setObjectName(u"label_2")
        sizePolicy2.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy2)
        self.label_2.setMinimumSize(QSize(0, 35))
        self.label_2.setStyleSheet(u"image: url(:/icons/res/icons/\u6587\u5b57\u8bc6\u522b\u8d44\u6e90 29.png);")
        self.label_2.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_2, 0, 0, 1, 1)

        self.label_3 = QLabel(self.widget_6)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(16777215, 30))
        self.label_3.setFont(font)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_3, 1, 0, 1, 1)


        self.gridLayout_2.addWidget(self.widget_6, 0, 0, 1, 1)


        self.horizontalLayout_2.addWidget(self.frame)

        self.frame_3 = QFrame(self.toolbar)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMaximumSize(QSize(298, 16777215))
        self.frame_3.setStyleSheet(u"QLabel{\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"QLabel:hover{\n"
"	background-color: rgb(255, 255, 127);\n"
"}\n"
"QWidget{\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_9 = QGridLayout(self.frame_3)
        self.gridLayout_9.setSpacing(0)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setContentsMargins(0, 0, 0, 0)
        self.widget_8 = QWidget(self.frame_3)
        self.widget_8.setObjectName(u"widget_8")
        sizePolicy3.setHeightForWidth(self.widget_8.sizePolicy().hasHeightForWidth())
        self.widget_8.setSizePolicy(sizePolicy3)
        self.widget_8.setMinimumSize(QSize(53, 0))
        self.widget_8.setMaximumSize(QSize(53, 16777215))
        self.gridLayout_5 = QGridLayout(self.widget_8)
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.widget_8)
        self.label_7.setObjectName(u"label_7")
        sizePolicy2.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy2)
        self.label_7.setMinimumSize(QSize(0, 35))
        self.label_7.setStyleSheet(u"image: url(:/icons/res/icons/\u70b9\u51fb.png);")
        self.label_7.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.label_7, 0, 0, 1, 1)

        self.label_8 = QLabel(self.widget_8)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMaximumSize(QSize(16777215, 30))
        self.label_8.setFont(font)
        self.label_8.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.label_8, 1, 0, 1, 1)


        self.gridLayout_9.addWidget(self.widget_8, 0, 0, 1, 1)

        self.widget_11 = QWidget(self.frame_3)
        self.widget_11.setObjectName(u"widget_11")
        sizePolicy3.setHeightForWidth(self.widget_11.sizePolicy().hasHeightForWidth())
        self.widget_11.setSizePolicy(sizePolicy3)
        self.widget_11.setMinimumSize(QSize(53, 0))
        self.widget_11.setMaximumSize(QSize(53, 16777215))
        self.gridLayout_8 = QGridLayout(self.widget_11)
        self.gridLayout_8.setSpacing(0)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label_13 = QLabel(self.widget_11)
        self.label_13.setObjectName(u"label_13")
        sizePolicy2.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy2)
        self.label_13.setMinimumSize(QSize(0, 35))
        self.label_13.setStyleSheet(u"image: url(:/icons/res/icons/\u653e\u5927\u8d44\u6e90 2.png);")
        self.label_13.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)

        self.gridLayout_8.addWidget(self.label_13, 0, 0, 1, 1)

        self.label_14 = QLabel(self.widget_11)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMaximumSize(QSize(16777215, 30))
        self.label_14.setFont(font)
        self.label_14.setAlignment(Qt.AlignCenter)

        self.gridLayout_8.addWidget(self.label_14, 1, 0, 1, 1)


        self.gridLayout_9.addWidget(self.widget_11, 0, 3, 1, 1)

        self.widget_10 = QWidget(self.frame_3)
        self.widget_10.setObjectName(u"widget_10")
        sizePolicy3.setHeightForWidth(self.widget_10.sizePolicy().hasHeightForWidth())
        self.widget_10.setSizePolicy(sizePolicy3)
        self.widget_10.setMinimumSize(QSize(53, 0))
        self.widget_10.setMaximumSize(QSize(53, 16777215))
        self.gridLayout_7 = QGridLayout(self.widget_10)
        self.gridLayout_7.setSpacing(0)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_11 = QLabel(self.widget_10)
        self.label_11.setObjectName(u"label_11")
        sizePolicy2.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy2)
        self.label_11.setMinimumSize(QSize(0, 35))
        self.label_11.setStyleSheet(u"image: url(:/icons/res/icons/\u5de6\u53f3\u7ffb\u8f6c\u8d44\u6e90 7.png);")
        self.label_11.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)

        self.gridLayout_7.addWidget(self.label_11, 0, 0, 1, 1)

        self.label_12 = QLabel(self.widget_10)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMaximumSize(QSize(16777215, 30))
        self.label_12.setFont(font)
        self.label_12.setAlignment(Qt.AlignCenter)

        self.gridLayout_7.addWidget(self.label_12, 1, 0, 1, 1)


        self.gridLayout_9.addWidget(self.widget_10, 0, 2, 1, 1)

        self.widget_9 = QWidget(self.frame_3)
        self.widget_9.setObjectName(u"widget_9")
        sizePolicy3.setHeightForWidth(self.widget_9.sizePolicy().hasHeightForWidth())
        self.widget_9.setSizePolicy(sizePolicy3)
        self.widget_9.setMinimumSize(QSize(53, 0))
        self.widget_9.setMaximumSize(QSize(53, 16777215))
        self.gridLayout_6 = QGridLayout(self.widget_9)
        self.gridLayout_6.setSpacing(0)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_9 = QLabel(self.widget_9)
        self.label_9.setObjectName(u"label_9")
        sizePolicy2.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy2)
        self.label_9.setMinimumSize(QSize(0, 35))
        self.label_9.setStyleSheet(u"image: url(:/icons/res/icons/\u79fb\u52a8\u8d44\u6e90 14.png);")
        self.label_9.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)

        self.gridLayout_6.addWidget(self.label_9, 0, 0, 1, 1)

        self.label_10 = QLabel(self.widget_9)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMaximumSize(QSize(16777215, 30))
        self.label_10.setFont(font)
        self.label_10.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.label_10, 1, 0, 1, 1)


        self.gridLayout_9.addWidget(self.widget_9, 0, 1, 1, 1)

        self.widget_12 = QWidget(self.frame_3)
        self.widget_12.setObjectName(u"widget_12")
        self.gridLayout_10 = QGridLayout(self.widget_12)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.label_15 = QLabel(self.widget_12)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMaximumSize(QSize(20, 20))
        self.label_15.setStyleSheet(u"image: url(:/icons/res/icons/\u539f\u56fe\u5927\u5c0f\u8d44\u6e90 4.png);")

        self.gridLayout_10.addWidget(self.label_15, 0, 0, 1, 1)

        self.label_16 = QLabel(self.widget_12)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout_10.addWidget(self.label_16, 0, 1, 1, 1)

        self.label_17 = QLabel(self.widget_12)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setMaximumSize(QSize(20, 20))
        self.label_17.setStyleSheet(u"image: url(:/icons/res/icons/\u9002\u5e94\u5c4f\u5e55\u8d44\u6e90 5.png);")

        self.gridLayout_10.addWidget(self.label_17, 1, 0, 1, 1)

        self.label_18 = QLabel(self.widget_12)
        self.label_18.setObjectName(u"label_18")

        self.gridLayout_10.addWidget(self.label_18, 1, 1, 1, 1)


        self.gridLayout_9.addWidget(self.widget_12, 0, 4, 1, 1)

        self.label_6 = QLabel(self.frame_3)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(16777215, 20))
        self.label_6.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.gridLayout_9.addWidget(self.label_6, 1, 0, 1, 5)


        self.horizontalLayout_2.addWidget(self.frame_3)

        self.frame_13 = QFrame(self.toolbar)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setMinimumSize(QSize(225, 0))
        self.frame_13.setMaximumSize(QSize(225, 16777215))
        self.frame_13.setStyleSheet(u"QLabel{\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"QLabel:hover{\n"
"	background-color: rgb(255, 255, 127);\n"
"}\n"
"QWidget{\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.gridLayout_13 = QGridLayout(self.frame_13)
        self.gridLayout_13.setSpacing(0)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.gridLayout_13.setContentsMargins(0, 0, 0, 0)
        self.widget_14 = QWidget(self.frame_13)
        self.widget_14.setObjectName(u"widget_14")
        sizePolicy3.setHeightForWidth(self.widget_14.sizePolicy().hasHeightForWidth())
        self.widget_14.setSizePolicy(sizePolicy3)
        self.widget_14.setMinimumSize(QSize(53, 0))
        self.widget_14.setMaximumSize(QSize(53, 16777215))
        self.gridLayout_11 = QGridLayout(self.widget_14)
        self.gridLayout_11.setSpacing(0)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.gridLayout_11.setContentsMargins(0, 0, 0, 0)
        self.label_19 = QLabel(self.widget_14)
        self.label_19.setObjectName(u"label_19")
        sizePolicy2.setHeightForWidth(self.label_19.sizePolicy().hasHeightForWidth())
        self.label_19.setSizePolicy(sizePolicy2)
        self.label_19.setMinimumSize(QSize(0, 35))
        self.label_19.setStyleSheet(u"image: url(:/icons/res/icons/\u4e00\u952e\u589e\u5f3a\u8d44\u6e90 24.png);")
        self.label_19.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)

        self.gridLayout_11.addWidget(self.label_19, 0, 0, 1, 1)

        self.label_20 = QLabel(self.widget_14)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setMaximumSize(QSize(16777215, 30))
        self.label_20.setFont(font)
        self.label_20.setAlignment(Qt.AlignCenter)

        self.gridLayout_11.addWidget(self.label_20, 1, 0, 1, 1)


        self.gridLayout_13.addWidget(self.widget_14, 0, 0, 1, 1)

        self.widget_15 = QWidget(self.frame_13)
        self.widget_15.setObjectName(u"widget_15")
        self.gridLayout_12 = QGridLayout(self.widget_15)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.label_22 = QLabel(self.widget_15)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setMaximumSize(QSize(20, 20))
        self.label_22.setStyleSheet(u"image: url(:/icons/res/icons/\u4f2a\u8272\u5f69\u589e\u5f3a\u8d44\u6e90 25.png);")

        self.gridLayout_12.addWidget(self.label_22, 0, 0, 1, 1)

        self.label_23 = QLabel(self.widget_15)
        self.label_23.setObjectName(u"label_23")

        self.gridLayout_12.addWidget(self.label_23, 0, 1, 1, 1)

        self.label_29 = QLabel(self.widget_15)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setMaximumSize(QSize(20, 20))
        self.label_29.setStyleSheet(u"image: url(:/icons/res/icons/\u6062\u590d\u539f\u59cb\u66f2\u7ebf\u8d44\u6e90 27.png);")

        self.gridLayout_12.addWidget(self.label_29, 0, 2, 1, 1)

        self.label_28 = QLabel(self.widget_15)
        self.label_28.setObjectName(u"label_28")

        self.gridLayout_12.addWidget(self.label_28, 0, 3, 1, 1)

        self.label_24 = QLabel(self.widget_15)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setMaximumSize(QSize(20, 20))
        self.label_24.setStyleSheet(u"image: url(:/icons/res/icons/\u7070\u5ea6\u66f2\u7ebf\u589e\u5f3a\u8d44\u6e90 26.png);")

        self.gridLayout_12.addWidget(self.label_24, 1, 0, 1, 1)

        self.label_25 = QLabel(self.widget_15)
        self.label_25.setObjectName(u"label_25")

        self.gridLayout_12.addWidget(self.label_25, 1, 1, 1, 1)

        self.label_27 = QLabel(self.widget_15)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setMaximumSize(QSize(20, 20))
        self.label_27.setStyleSheet(u"image: url(:/icons/res/icons/\u5c40\u90e8\u589e\u5f3a\u8d44\u6e90 28.png);")

        self.gridLayout_12.addWidget(self.label_27, 2, 0, 1, 1)

        self.label_26 = QLabel(self.widget_15)
        self.label_26.setObjectName(u"label_26")

        self.gridLayout_12.addWidget(self.label_26, 2, 1, 1, 1)


        self.gridLayout_13.addWidget(self.widget_15, 0, 1, 1, 1)

        self.label_21 = QLabel(self.frame_13)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setMaximumSize(QSize(16777215, 20))
        self.label_21.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_21.setAlignment(Qt.AlignCenter)

        self.gridLayout_13.addWidget(self.label_21, 1, 0, 1, 2)


        self.horizontalLayout_2.addWidget(self.frame_13)

        self.frame_2 = QFrame(self.toolbar)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_2.addWidget(self.frame_2)


        self.verticalLayout.addWidget(self.toolbar)

        self.mainArea = QWidget(self.centralwidget)
        self.mainArea.setObjectName(u"mainArea")
        self.mainArea.setStyleSheet(u"QWidget{background-color: rgb(245, 245, 245);}\n"
"QFrame{\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.gridLayout = QGridLayout(self.mainArea)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.widget_4 = QWidget(self.mainArea)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setMinimumSize(QSize(0, 470))
        self.widget_4.setMaximumSize(QSize(16777215, 470))
        self.gridLayout_19 = QGridLayout(self.widget_4)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.graphicsView = QGraphicsView(self.widget_4)
        self.graphicsView.setObjectName(u"graphicsView")
        self.graphicsView.setMinimumSize(QSize(0, 470))
        self.graphicsView.setMaximumSize(QSize(16777215, 470))
        self.graphicsView.setStyleSheet(u"background-color:transparent;\n"
"border:none;")

        self.gridLayout_19.addWidget(self.graphicsView, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.widget_4, 1, 1, 1, 2)

        self.frame_21 = QFrame(self.mainArea)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setMinimumSize(QSize(330, 316))
        self.frame_21.setMaximumSize(QSize(330, 316))
        self.gridLayout_14 = QGridLayout(self.frame_21)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.label_30 = QLabel(self.frame_21)
        self.label_30.setObjectName(u"label_30")

        self.gridLayout_14.addWidget(self.label_30, 0, 0, 1, 1)

        self.lineEdit = QLineEdit(self.frame_21)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(138, 0))
        self.lineEdit.setStyleSheet(u"QLineEdit{\n"
"background:transparent;\n"
"border-color:rgb(0, 0, 0);\n"
"border-style:solid;\n"
"border-top-width:0px;\n"
"border-right-width:0px;\n"
"border-bottom-width:1px;\n"
"border-left-width:0px;\n"
"}\n"
"")

        self.gridLayout_14.addWidget(self.lineEdit, 0, 1, 1, 1)

        self.pushButton_6 = QPushButton(self.frame_21)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setMinimumSize(QSize(60, 26))
        self.pushButton_6.setStyleSheet(u"border-radius:10px;\n"
"background-color: rgb(22, 155, 213);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_14.addWidget(self.pushButton_6, 0, 2, 1, 1)

        self.listWidget = QListWidget(self.frame_21)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setMinimumSize(QSize(0, 240))
        self.listWidget.setMaximumSize(QSize(16777215, 240))
        self.listWidget.setStyleSheet(u"background-color: rgb(245, 245, 245);\n"
"border:none;")

        self.gridLayout_14.addWidget(self.listWidget, 1, 0, 1, 3)


        self.gridLayout.addWidget(self.frame_21, 0, 0, 1, 1)

        self.frame_31 = QFrame(self.mainArea)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setMinimumSize(QSize(910, 316))
        self.frame_31.setMaximumSize(QSize(910, 316))

        self.gridLayout.addWidget(self.frame_31, 0, 1, 1, 1)

        self.frame1 = QFrame(self.mainArea)
        self.frame1.setObjectName(u"frame1")
        self.frame1.setMinimumSize(QSize(330, 470))
        self.frame1.setMaximumSize(QSize(330, 470))
        self.gridLayout_15 = QGridLayout(self.frame1)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.label_31 = QLabel(self.frame1)
        self.label_31.setObjectName(u"label_31")

        self.gridLayout_15.addWidget(self.label_31, 0, 0, 1, 1)

        self.comboBox = QComboBox(self.frame1)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setStyleSheet(u"QComboBox{\n"
"background:transparent;\n"
"border-color:rgb(0, 0, 0);\n"
"border-style:solid;\n"
"border-top-width:0px;\n"
"border-right-width:0px;\n"
"border-bottom-width:1px;\n"
"border-left-width:0px;\n"
"}\n"
"")

        self.gridLayout_15.addWidget(self.comboBox, 7, 1, 1, 2)

        self.lineEdit_3 = QLineEdit(self.frame1)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setMinimumSize(QSize(138, 0))
        self.lineEdit_3.setStyleSheet(u"QLineEdit{\n"
"background:transparent;\n"
"border-color:rgb(0, 0, 0);\n"
"border-style:solid;\n"
"border-top-width:0px;\n"
"border-right-width:0px;\n"
"border-bottom-width:1px;\n"
"border-left-width:0px;\n"
"}\n"
"")

        self.gridLayout_15.addWidget(self.lineEdit_3, 1, 2, 1, 1)

        self.lineEdit_5 = QLineEdit(self.frame1)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setMinimumSize(QSize(138, 0))
        self.lineEdit_5.setStyleSheet(u"QLineEdit{\n"
"background:transparent;\n"
"border-color:rgb(0, 0, 0);\n"
"border-style:solid;\n"
"border-top-width:0px;\n"
"border-right-width:0px;\n"
"border-bottom-width:1px;\n"
"border-left-width:0px;\n"
"}\n"
"")

        self.gridLayout_15.addWidget(self.lineEdit_5, 3, 2, 1, 1)

        self.label_33 = QLabel(self.frame1)
        self.label_33.setObjectName(u"label_33")

        self.gridLayout_15.addWidget(self.label_33, 2, 0, 1, 1)

        self.label_39 = QLabel(self.frame1)
        self.label_39.setObjectName(u"label_39")

        self.gridLayout_15.addWidget(self.label_39, 7, 0, 1, 1)

        self.label_32 = QLabel(self.frame1)
        self.label_32.setObjectName(u"label_32")

        self.gridLayout_15.addWidget(self.label_32, 1, 0, 1, 2)

        self.label_41 = QLabel(self.frame1)
        self.label_41.setObjectName(u"label_41")

        self.gridLayout_15.addWidget(self.label_41, 5, 0, 1, 1)

        self.label_40 = QLabel(self.frame1)
        self.label_40.setObjectName(u"label_40")

        self.gridLayout_15.addWidget(self.label_40, 8, 0, 1, 1)

        self.label_34 = QLabel(self.frame1)
        self.label_34.setObjectName(u"label_34")

        self.gridLayout_15.addWidget(self.label_34, 3, 0, 1, 1)

        self.lineEdit_2 = QLineEdit(self.frame1)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMinimumSize(QSize(138, 0))
        self.lineEdit_2.setStyleSheet(u"QLineEdit{\n"
"background:transparent;\n"
"border-color:rgb(0, 0, 0);\n"
"border-style:solid;\n"
"border-top-width:0px;\n"
"border-right-width:0px;\n"
"border-bottom-width:1px;\n"
"border-left-width:0px;\n"
"}\n"
"")

        self.gridLayout_15.addWidget(self.lineEdit_2, 0, 2, 1, 1)

        self.scrollArea = QScrollArea(self.frame1)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"border:none;\n"
"background-color: rgb(245, 245, 245);")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 312, 232))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_15.addWidget(self.scrollArea, 6, 0, 1, 3)

        self.lineEdit_4 = QLineEdit(self.frame1)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setMinimumSize(QSize(138, 0))
        self.lineEdit_4.setStyleSheet(u"QLineEdit{\n"
"background:transparent;\n"
"border-color:rgb(0, 0, 0);\n"
"border-style:solid;\n"
"border-top-width:0px;\n"
"border-right-width:0px;\n"
"border-bottom-width:1px;\n"
"border-left-width:0px;\n"
"}\n"
"")

        self.gridLayout_15.addWidget(self.lineEdit_4, 2, 2, 1, 1)

        self.comboBox_2 = QComboBox(self.frame1)
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setStyleSheet(u"QComboBox{\n"
"background:transparent;\n"
"border-color:rgb(0, 0, 0);\n"
"border-style:solid;\n"
"border-top-width:0px;\n"
"border-right-width:0px;\n"
"border-bottom-width:1px;\n"
"border-left-width:0px;\n"
"}\n"
"")

        self.gridLayout_15.addWidget(self.comboBox_2, 8, 1, 1, 2)

        self.widget = QWidget(self.frame1)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(0, 30))
        self.widget.setStyleSheet(u"background-color: transparent;")
        self.gridLayout_16 = QGridLayout(self.widget)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.pushButton_7 = QPushButton(self.widget)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setMinimumSize(QSize(120, 28))
        self.pushButton_7.setMaximumSize(QSize(120, 28))
        self.pushButton_7.setStyleSheet(u"border-radius:10px;\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(22, 155, 213);")

        self.gridLayout_16.addWidget(self.pushButton_7, 0, 0, 1, 1)

        self.pushButton_8 = QPushButton(self.widget)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setMinimumSize(QSize(120, 26))
        self.pushButton_8.setMaximumSize(QSize(120, 16777215))
        self.pushButton_8.setStyleSheet(u"border-radius:10px;\n"
"background-color: rgb(206, 206, 206);\n"
"")

        self.gridLayout_16.addWidget(self.pushButton_8, 0, 1, 1, 1)


        self.gridLayout_15.addWidget(self.widget, 4, 0, 1, 3)


        self.gridLayout.addWidget(self.frame1, 1, 0, 1, 1)

        self.frame_5 = QFrame(self.mainArea)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(0, 316))
        self.frame_5.setMaximumSize(QSize(16777215, 316))
        self.gridLayout_18 = QGridLayout(self.frame_5)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.gridLayout_18.setContentsMargins(0, 0, 0, 0)
        self.label_43 = QLabel(self.frame_5)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setMinimumSize(QSize(0, 24))
        self.label_43.setAlignment(Qt.AlignCenter)

        self.gridLayout_18.addWidget(self.label_43, 3, 0, 1, 1)

        self.comboBox_6 = QComboBox(self.frame_5)
        self.comboBox_6.setObjectName(u"comboBox_6")
        self.comboBox_6.setStyleSheet(u"QComboBox{\n"
"background:transparent;\n"
"border-color:rgb(0, 0, 0);\n"
"border-style:solid;\n"
"border-top-width:0px;\n"
"border-right-width:0px;\n"
"border-bottom-width:1px;\n"
"border-left-width:0px;\n"
"}\n"
"")

        self.gridLayout_18.addWidget(self.comboBox_6, 5, 1, 1, 2)

        self.comboBox_3 = QComboBox(self.frame_5)
        self.comboBox_3.setObjectName(u"comboBox_3")
        self.comboBox_3.setStyleSheet(u"QComboBox{\n"
"background:transparent;\n"
"border-color:rgb(0, 0, 0);\n"
"border-style:solid;\n"
"border-top-width:0px;\n"
"border-right-width:0px;\n"
"border-bottom-width:1px;\n"
"border-left-width:0px;\n"
"}\n"
"")

        self.gridLayout_18.addWidget(self.comboBox_3, 2, 1, 1, 3)

        self.comboBox_4 = QComboBox(self.frame_5)
        self.comboBox_4.setObjectName(u"comboBox_4")
        self.comboBox_4.setStyleSheet(u"QComboBox{\n"
"background:transparent;\n"
"border-color:rgb(0, 0, 0);\n"
"border-style:solid;\n"
"border-top-width:0px;\n"
"border-right-width:0px;\n"
"border-bottom-width:1px;\n"
"border-left-width:0px;\n"
"}\n"
"")

        self.gridLayout_18.addWidget(self.comboBox_4, 3, 1, 1, 3)

        self.label_46 = QLabel(self.frame_5)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setMinimumSize(QSize(0, 24))
        self.label_46.setAlignment(Qt.AlignCenter)

        self.gridLayout_18.addWidget(self.label_46, 5, 3, 1, 1)

        self.pushButton_14 = QPushButton(self.frame_5)
        self.pushButton_14.setObjectName(u"pushButton_14")
        self.pushButton_14.setMinimumSize(QSize(60, 26))
        self.pushButton_14.setStyleSheet(u"border-radius:10px;\n"
"background-color: rgb(22, 155, 213);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_18.addWidget(self.pushButton_14, 2, 4, 1, 1)

        self.comboBox_5 = QComboBox(self.frame_5)
        self.comboBox_5.setObjectName(u"comboBox_5")
        self.comboBox_5.setStyleSheet(u"QComboBox{\n"
"background:transparent;\n"
"border-color:rgb(0, 0, 0);\n"
"border-style:solid;\n"
"border-top-width:0px;\n"
"border-right-width:0px;\n"
"border-bottom-width:1px;\n"
"border-left-width:0px;\n"
"}\n"
"")

        self.gridLayout_18.addWidget(self.comboBox_5, 4, 1, 1, 4)

        self.label_44 = QLabel(self.frame_5)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setMinimumSize(QSize(0, 24))
        self.label_44.setAlignment(Qt.AlignCenter)

        self.gridLayout_18.addWidget(self.label_44, 4, 0, 1, 1)

        self.widget_2 = QWidget(self.frame_5)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setStyleSheet(u"background-color:transparent;")
        self.gridLayout_17 = QGridLayout(self.widget_2)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.pushButton_11 = QPushButton(self.widget_2)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setMinimumSize(QSize(120, 28))
        self.pushButton_11.setMaximumSize(QSize(120, 28))
        self.pushButton_11.setStyleSheet(u"border-radius:10px;\n"
"background-color: rgb(22, 155, 213);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_17.addWidget(self.pushButton_11, 0, 0, 1, 1)

        self.pushButton_12 = QPushButton(self.widget_2)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setMinimumSize(QSize(120, 28))
        self.pushButton_12.setMaximumSize(QSize(120, 28))
        self.pushButton_12.setStyleSheet(u"border-radius:10px;\n"
"background-color: rgb(22, 155, 213);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_17.addWidget(self.pushButton_12, 0, 1, 1, 1)

        self.pushButton_13 = QPushButton(self.widget_2)
        self.pushButton_13.setObjectName(u"pushButton_13")
        self.pushButton_13.setMinimumSize(QSize(120, 28))
        self.pushButton_13.setMaximumSize(QSize(120, 28))
        self.pushButton_13.setStyleSheet(u"border-radius:10px;\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(22, 155, 213);")

        self.gridLayout_17.addWidget(self.pushButton_13, 0, 2, 1, 1)


        self.gridLayout_18.addWidget(self.widget_2, 0, 0, 1, 5)

        self.label_45 = QLabel(self.frame_5)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setMinimumSize(QSize(0, 24))
        self.label_45.setAlignment(Qt.AlignCenter)

        self.gridLayout_18.addWidget(self.label_45, 5, 0, 1, 1)

        self.label_42 = QLabel(self.frame_5)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setMinimumSize(QSize(0, 24))
        self.label_42.setAlignment(Qt.AlignCenter)

        self.gridLayout_18.addWidget(self.label_42, 2, 0, 1, 1)

        self.pushButton_15 = QPushButton(self.frame_5)
        self.pushButton_15.setObjectName(u"pushButton_15")
        self.pushButton_15.setMinimumSize(QSize(60, 26))
        self.pushButton_15.setStyleSheet(u"border-radius:10px;\n"
"background-color: rgb(22, 155, 213);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_18.addWidget(self.pushButton_15, 3, 4, 1, 1)

        self.comboBox_7 = QComboBox(self.frame_5)
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.setObjectName(u"comboBox_7")
        self.comboBox_7.setStyleSheet(u"QComboBox{\n"
"background:transparent;\n"
"border-color:rgb(0, 0, 0);\n"
"border-style:solid;\n"
"border-top-width:0px;\n"
"border-right-width:0px;\n"
"border-bottom-width:1px;\n"
"border-left-width:0px;\n"
"}\n"
"")

        self.gridLayout_18.addWidget(self.comboBox_7, 5, 4, 1, 1)

        self.tableWidget = QTableWidget(self.frame_5)
        if (self.tableWidget.columnCount() < 6):
            self.tableWidget.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setStyleSheet(u"QTableWidget{\n"
"border:none;\n"
"}\n"
"/*\u8868\u5934*/\n"
"QHeaderView::section{\n"
"text-align:center;\n"
"padding:3px;\n"
"margin:0px;\n"
"color:rgb(0, 0, 0);\n"
"border:1px solid #242424;\n"
"border-left-width:0;\n"
"}\n"
"/*\u8868\u53f3\u4fa7\u7684\u6ed1\u6761*/\n"
"QScrollBar:horizental{\n"
"background:#484848;\n"
"padding:0px;\n"
"border-radius:6px;\n"
"max-width:12px;\n"
"}\n"
"\n"
"/*\u6ed1\u5757*/\n"
"QScrollBar::handle:horizental{\n"
"background:#CCCCCC;\n"
"}\n"
"\n"
"\n"
"/*\u8868\u53f3\u4fa7\u7684\u6ed1\u6761*/\n"
"QScrollBar:vertical{\n"
"background:#484848;\n"
"padding:0px;\n"
"border-radius:6px;\n"
"max-width:12px;\n"
"}\n"
"\n"
"/*\u6ed1\u5757*/\n"
"QScrollBar::handle:vertical{\n"
"background:#CCCCCC;\n"
"}\n"
"/*\n"
"\u6ed1\u5757\u60ac\u6d6e\uff0c\u6309\u4e0b*/\n"
"QScrollBar::handle:hover:vertical,QScrollBar::handle:pressed:vertical{\n"
"background:#A7A7A7;\n"
"}\n"
"/*\n"
"\u6ed1\u5757\u5df2\u7ecf\u5212\u8fc7\u7684\u533a\u57df*/\n"
"QScrollBar::sub-page:vertical{\n"
"background:444444;\n"
""
                        "}\n"
"\n"
"/*\n"
"\u6ed1\u5757\u8fd8\u6ca1\u6709\u5212\u8fc7\u7684\u533a\u57df*/\n"
"QScrollBar::add-page:vertical{\n"
"background:5B5B5B;\n"
"}\n"
"\n"
"/*\u9875\u9762\u4e0b\u79fb\u7684\u6309\u94ae*/\n"
"QScrollBar::add-line:vertical{\n"
"background:none;\n"
"}\n"
"/*\u9875\u9762\u4e0a\u79fb\u7684\u6309\u94ae*/\n"
"QScrollBar::sub-line:vertical{\n"
"background:none;\n"
"}\n"
"")
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setSortingEnabled(True)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.verticalHeader().setVisible(False)

        self.gridLayout_18.addWidget(self.tableWidget, 1, 0, 1, 5)


        self.gridLayout.addWidget(self.frame_5, 0, 2, 1, 1)


        self.verticalLayout.addWidget(self.mainArea)

        self.statebar = QWidget(self.centralwidget)
        self.statebar.setObjectName(u"statebar")
        sizePolicy2.setHeightForWidth(self.statebar.sizePolicy().hasHeightForWidth())
        self.statebar.setSizePolicy(sizePolicy2)
        self.statebar.setMinimumSize(QSize(0, 30))
        self.statebar.setStyleSheet(u"background-color: rgb(22, 78, 134);")

        self.verticalLayout.addWidget(self.statebar)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u8bc4\u7247", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u914d\u7f6e", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"\u5de5\u5177", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"\u89c6\u56fe", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"\u5e2e\u52a9", None))
        self.label_5.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u91cd\u590d\u7247\u68c0\u7d22", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u81ea\u52a8\u8bc6\u522b", None))
        self.label_2.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u6587\u5b57\u8bc6\u522b", None))
        self.label_7.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u70b9\u51fb", None))
        self.label_13.setText("")
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"\u653e\u5927", None))
        self.label_11.setText("")
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"\u6c34\u5e73\u7ffb\u8f6c", None))
        self.label_9.setText("")
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u5e73\u79fb", None))
        self.label_15.setText("")
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"\u539f\u59cb\u5927\u5c0f", None))
        self.label_17.setText("")
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"\u9002\u5408\u5c4f\u5e55", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u89c6\u56fe\u64cd\u4f5c", None))
        self.label_19.setText("")
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"\u81ea\u52a8\u8c03\u6574", None))
        self.label_22.setText("")
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"\u8272\u5f69\u8c03\u6574", None))
        self.label_29.setText("")
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"\u539f\u59cb\u56fe\u50cf", None))
        self.label_24.setText("")
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"\u7070\u5ea6\u66f2\u7ebf", None))
        self.label_27.setText("")
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"\u5c40\u90e8\u8c03\u6574", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"\u56fe\u50cf\u589e\u5f3a", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6\u4f4d\u7f6e", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"\u4ea7\u54c1\u7f16\u53f7", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"\u90e8\u4f4d\u7f16\u53f7", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"\u6267\u884c\u6807\u51c6", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"\u710a\u63a5\u63a5\u5934\u7f16\u53f7", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"\u5e95\u7247\u4fe1\u606f", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"\u62cd\u6444\u7ea7\u522b", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"\u900f\u7167\u65e5\u671f", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"\u5e95\u7247\u7b49\u7ea7", None))
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"\u6807\u8bb0\u9f50\u5168", None))
        self.pushButton_14.setText(QCoreApplication.translate("MainWindow", u"\u91cd\u7f6e", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"\u7f3a\u9677\u6027\u8d28", None))
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"\u7f3a\u9677\u68c0\u6d4b", None))
        self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u"\u7f3a\u9677\u81ea\u52a8\u5b9a\u4f4d", None))
        self.pushButton_13.setText(QCoreApplication.translate("MainWindow", u"\u7f3a\u9677\u624b\u52a8\u5b9a\u4f4d", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"\u8bc4\u7247\u5907\u6ce8", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"\u8bc4\u5b9a\u6807\u51c6", None))
        self.pushButton_15.setText(QCoreApplication.translate("MainWindow", u"\u8bc4\u5b9a", None))
        self.comboBox_7.setItemText(0, QCoreApplication.translate("MainWindow", u"\u5426", None))
        self.comboBox_7.setItemText(1, QCoreApplication.translate("MainWindow", u"\u662f", None))

        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u7f16\u53f7", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u7c7b\u578b", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u5bbd\u5ea6", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"\u957f\u5ea6", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"\u5b9a\u91cf", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"\u5904\u7406", None));
    # retranslateUi

