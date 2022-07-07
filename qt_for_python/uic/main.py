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
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCheckBox, QComboBox,
    QDateTimeEdit, QFrame, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QPushButton, QScrollArea, QSizePolicy, QSpacerItem,
    QTabWidget, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

from utils import ImageViewer
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
        self.actionOpen = QAction(MainWindow)
        self.actionOpen.setObjectName(u"actionOpen")
        icon1 = QIcon()
        icon1.addFile(u":/icons/res/icons/\u6253\u5f00.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionOpen.setIcon(icon1)
        self.actionOpenDatabase = QAction(MainWindow)
        self.actionOpenDatabase.setObjectName(u"actionOpenDatabase")
        self.actionPrintPreview = QAction(MainWindow)
        self.actionPrintPreview.setObjectName(u"actionPrintPreview")
        self.actionPrintConfig = QAction(MainWindow)
        self.actionPrintConfig.setObjectName(u"actionPrintConfig")
        self.actionCloudConnect = QAction(MainWindow)
        self.actionCloudConnect.setObjectName(u"actionCloudConnect")
        icon2 = QIcon()
        icon2.addFile(u":/icons/res/icons/\u4e91\u7aef.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionCloudConnect.setIcon(icon2)
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
        self.menubar.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"")
        self.horizontalLayout = QHBoxLayout(self.menubar)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButtonFile = QPushButton(self.menubar)
        self.pushButtonFile.setObjectName(u"pushButtonFile")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButtonFile.sizePolicy().hasHeightForWidth())
        self.pushButtonFile.setSizePolicy(sizePolicy1)
        self.pushButtonFile.setMinimumSize(QSize(80, 0))
        self.pushButtonFile.setMaximumSize(QSize(80, 16777215))
        self.pushButtonFile.setStyleSheet(u"QPushButton{\n"
"border:none;\n"
"}\n"
"QPushButton::menu-indicator{\n"
"image:none;\n"
"}")

        self.horizontalLayout.addWidget(self.pushButtonFile)

        self.pushButtonConfig = QPushButton(self.menubar)
        self.pushButtonConfig.setObjectName(u"pushButtonConfig")
        sizePolicy1.setHeightForWidth(self.pushButtonConfig.sizePolicy().hasHeightForWidth())
        self.pushButtonConfig.setSizePolicy(sizePolicy1)
        self.pushButtonConfig.setMinimumSize(QSize(80, 0))
        self.pushButtonConfig.setMaximumSize(QSize(80, 16777215))
        self.pushButtonConfig.setStyleSheet(u"QPushButton{\n"
"border:none;\n"
"}\n"
"QPushButton::menu-indicator{\n"
"image:none;\n"
"}")

        self.horizontalLayout.addWidget(self.pushButtonConfig)

        self.pushButtonTools = QPushButton(self.menubar)
        self.pushButtonTools.setObjectName(u"pushButtonTools")
        sizePolicy1.setHeightForWidth(self.pushButtonTools.sizePolicy().hasHeightForWidth())
        self.pushButtonTools.setSizePolicy(sizePolicy1)
        self.pushButtonTools.setMinimumSize(QSize(80, 0))
        self.pushButtonTools.setMaximumSize(QSize(80, 16777215))
        self.pushButtonTools.setStyleSheet(u"QPushButton{\n"
"border:none;\n"
"}\n"
"QPushButton::menu-indicator{\n"
"image:none;\n"
"}")

        self.horizontalLayout.addWidget(self.pushButtonTools)

        self.pushButtonView = QPushButton(self.menubar)
        self.pushButtonView.setObjectName(u"pushButtonView")
        sizePolicy1.setHeightForWidth(self.pushButtonView.sizePolicy().hasHeightForWidth())
        self.pushButtonView.setSizePolicy(sizePolicy1)
        self.pushButtonView.setMinimumSize(QSize(80, 0))
        self.pushButtonView.setMaximumSize(QSize(80, 16777215))
        self.pushButtonView.setStyleSheet(u"QPushButton{\n"
"border:none;\n"
"}\n"
"QPushButton::menu-indicator{\n"
"image:none;\n"
"}")

        self.horizontalLayout.addWidget(self.pushButtonView)

        self.pushButtonHelp = QPushButton(self.menubar)
        self.pushButtonHelp.setObjectName(u"pushButtonHelp")
        sizePolicy1.setHeightForWidth(self.pushButtonHelp.sizePolicy().hasHeightForWidth())
        self.pushButtonHelp.setSizePolicy(sizePolicy1)
        self.pushButtonHelp.setMinimumSize(QSize(80, 0))
        self.pushButtonHelp.setMaximumSize(QSize(80, 16777215))
        self.pushButtonHelp.setStyleSheet(u"QPushButton{\n"
"border:none;\n"
"}\n"
"QPushButton::menu-indicator{\n"
"image:none;\n"
"}")

        self.horizontalLayout.addWidget(self.pushButtonHelp)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout.addWidget(self.menubar)

        self.toolbar = QWidget(self.centralwidget)
        self.toolbar.setObjectName(u"toolbar")
        self.toolbar.setMinimumSize(QSize(0, 120))
        self.toolbar.setMaximumSize(QSize(16777215, 120))
        self.toolbar.setStyleSheet(u"QWidget{background-color: rgb(245, 245, 245);}\n"
"QFrame{background-color: rgb(255, 255, 255);border:none;}\n"
"")
        self.horizontalLayout_2 = QHBoxLayout(self.toolbar)
        self.horizontalLayout_2.setSpacing(2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
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
        self.frame_3.setMinimumSize(QSize(100, 0))
        self.frame_3.setMaximumSize(QSize(100, 16777215))
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
        self.widget_12 = QWidget(self.frame_3)
        self.widget_12.setObjectName(u"widget_12")
        self.gridLayout_10 = QGridLayout(self.widget_12)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_10.setHorizontalSpacing(6)
        self.gridLayout_10.setContentsMargins(-1, 0, 0, 0)
        self.label_16 = QLabel(self.widget_12)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setAlignment(Qt.AlignCenter)

        self.gridLayout_10.addWidget(self.label_16, 0, 1, 1, 1)

        self.label_15 = QLabel(self.widget_12)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMinimumSize(QSize(20, 20))
        self.label_15.setMaximumSize(QSize(20, 20))
        self.label_15.setStyleSheet(u"image: url(:/icons/res/icons/\u539f\u56fe\u5927\u5c0f\u8d44\u6e90 4.png);")

        self.gridLayout_10.addWidget(self.label_15, 0, 0, 1, 1)

        self.label_11 = QLabel(self.widget_12)
        self.label_11.setObjectName(u"label_11")
        sizePolicy2.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy2)
        self.label_11.setMinimumSize(QSize(20, 20))
        self.label_11.setStyleSheet(u"image: url(:/icons/res/icons/\u5de6\u53f3\u7ffb\u8f6c\u8d44\u6e90 7.png);")
        self.label_11.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)

        self.gridLayout_10.addWidget(self.label_11, 2, 0, 1, 1)

        self.label_12 = QLabel(self.widget_12)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMaximumSize(QSize(16777215, 30))
        self.label_12.setFont(font)
        self.label_12.setAlignment(Qt.AlignCenter)

        self.gridLayout_10.addWidget(self.label_12, 2, 1, 1, 1)

        self.label_29 = QLabel(self.widget_12)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setMaximumSize(QSize(20, 20))
        self.label_29.setStyleSheet(u"image: url(:/icons/res/icons/\u6062\u590d\u539f\u59cb\u66f2\u7ebf\u8d44\u6e90 27.png);")

        self.gridLayout_10.addWidget(self.label_29, 1, 0, 1, 1)

        self.label_28 = QLabel(self.widget_12)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setAlignment(Qt.AlignCenter)

        self.gridLayout_10.addWidget(self.label_28, 1, 1, 1, 1)


        self.gridLayout_9.addWidget(self.widget_12, 0, 1, 1, 1)

        self.label_6 = QLabel(self.frame_3)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(16777215, 20))
        self.label_6.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.gridLayout_9.addWidget(self.label_6, 1, 1, 1, 1)


        self.horizontalLayout_2.addWidget(self.frame_3)

        self.frame_13 = QFrame(self.toolbar)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setMinimumSize(QSize(0, 0))
        self.frame_13.setMaximumSize(QSize(150, 16777215))
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
        self.label_23.setAlignment(Qt.AlignCenter)

        self.gridLayout_12.addWidget(self.label_23, 0, 1, 1, 1)

        self.label_24 = QLabel(self.widget_15)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setMaximumSize(QSize(20, 20))
        self.label_24.setStyleSheet(u"image: url(:/icons/res/icons/\u7070\u5ea6\u66f2\u7ebf\u589e\u5f3a\u8d44\u6e90 26.png);")

        self.gridLayout_12.addWidget(self.label_24, 1, 0, 1, 1)

        self.label_25 = QLabel(self.widget_15)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setAlignment(Qt.AlignCenter)

        self.gridLayout_12.addWidget(self.label_25, 1, 1, 1, 1)

        self.label_27 = QLabel(self.widget_15)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setMaximumSize(QSize(20, 20))
        self.label_27.setStyleSheet(u"image: url(:/icons/res/icons/\u5c40\u90e8\u589e\u5f3a\u8d44\u6e90 28.png);")

        self.gridLayout_12.addWidget(self.label_27, 2, 0, 1, 1)

        self.label_26 = QLabel(self.widget_15)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setAlignment(Qt.AlignCenter)

        self.gridLayout_12.addWidget(self.label_26, 2, 1, 1, 1)


        self.gridLayout_13.addWidget(self.widget_15, 0, 1, 1, 1)

        self.label_21 = QLabel(self.frame_13)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setMaximumSize(QSize(16777215, 20))
        self.label_21.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_21.setAlignment(Qt.AlignCenter)

        self.gridLayout_13.addWidget(self.label_21, 1, 0, 1, 2)


        self.horizontalLayout_2.addWidget(self.frame_13)

        self.frame_7 = QFrame(self.toolbar)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMaximumSize(QSize(120, 16777215))
        self.frame_7.setStyleSheet(u"QLabel{\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"QLabel:hover{\n"
"	background-color: rgb(255, 255, 127);\n"
"}\n"
"QWidget{\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_7)
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.widget_2 = QWidget(self.frame_7)
        self.widget_2.setObjectName(u"widget_2")
        self.gridLayout_6 = QGridLayout(self.widget_2)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.label_49 = QLabel(self.widget_2)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setMaximumSize(QSize(20, 20))
        self.label_49.setStyleSheet(u"image: url(:/icons/res/icons/\u4f2a\u8272\u5f69\u589e\u5f3a\u8d44\u6e90 25.png);")

        self.gridLayout_6.addWidget(self.label_49, 0, 0, 1, 1)

        self.label_37 = QLabel(self.widget_2)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.label_37, 0, 1, 1, 1)

        self.label_38 = QLabel(self.widget_2)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setMaximumSize(QSize(20, 20))
        self.label_38.setStyleSheet(u"image: url(:/icons/res/icons/\u7070\u5ea6\u66f2\u7ebf\u589e\u5f3a\u8d44\u6e90 26.png);")

        self.gridLayout_6.addWidget(self.label_38, 1, 0, 1, 1)

        self.label_48 = QLabel(self.widget_2)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.label_48, 1, 1, 1, 1)

        self.label_47 = QLabel(self.widget_2)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setMaximumSize(QSize(20, 20))
        self.label_47.setStyleSheet(u"image: url(:/icons/res/icons/\u5c40\u90e8\u589e\u5f3a\u8d44\u6e90 28.png);")

        self.gridLayout_6.addWidget(self.label_47, 2, 0, 1, 1)

        self.label_36 = QLabel(self.widget_2)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.label_36, 2, 1, 1, 1)


        self.gridLayout_5.addWidget(self.widget_2, 0, 0, 1, 2)

        self.label_35 = QLabel(self.frame_7)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setMaximumSize(QSize(16777215, 20))
        self.label_35.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_35.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.label_35, 1, 0, 1, 2)


        self.horizontalLayout_2.addWidget(self.frame_7)

        self.frame_2 = QFrame(self.toolbar)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_20 = QGridLayout(self.frame_2)
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.label_30 = QLabel(self.frame_2)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setStyleSheet(u"image: url(:/icons/res/icons/logo.png);\n"
"background-color: rgb(22, 78, 134);")

        self.gridLayout_20.addWidget(self.label_30, 0, 0, 1, 1)


        self.horizontalLayout_2.addWidget(self.frame_2)


        self.verticalLayout.addWidget(self.toolbar)

        self.mainArea = QTabWidget(self.centralwidget)
        self.mainArea.setObjectName(u"mainArea")
        self.mainArea.setMinimumSize(QSize(20, 20))
        self.mainArea.setStyleSheet(u"QWidget{background-color: rgb(245, 245, 245);}\n"
"QFrame{\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"QTabWidget::pane{\n"
"	border:none;\n"
"}\n"
"\n"
"QTabWidget::tab-bar {\n"
"    left: 1px;\n"
"}\n"
"QTabBar::tab {\n"
"    background: #FFFFFF;\n"
"	color:#169BD5;\n"
"    border: 2px;\n"
"    border-top-left-radius: 20px;\n"
"    border-top-right-radius: 20px;\n"
"    min-width: 200px;\n"
"	min-height: 20px;\n"
"    padding: 2px;\n"
"}\n"
"QTabBar::tab:selected{\n"
"    background-color: #169BD5;\n"
"	color:#FFFFFF;\n"
"}\n"
"\n"
"\n"
"")
        self.pageStart = QWidget()
        self.pageStart.setObjectName(u"pageStart")
        self.horizontalLayout_3 = QHBoxLayout(self.pageStart)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.frame_10 = QFrame(self.pageStart)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_3.addWidget(self.frame_10)

        self.mainArea.addTab(self.pageStart, "")
        self.pageDatabase = QWidget()
        self.pageDatabase.setObjectName(u"pageDatabase")
        self.gridLayout_7 = QGridLayout(self.pageDatabase)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.frame_8 = QFrame(self.pageDatabase)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMaximumSize(QSize(16777215, 16777215))
        self.frame_8.setStyleSheet(u"QTableWidget{\n"
"border:none;\n"
"}\n"
"/*\u8868\u5934*/\n"
"QHeaderView::section{\n"
"text-align:center;\n"
"padding:3px;\n"
"margin:0px;\n"
"color:rgb(0, 0, 0);\n"
"border:0px;\n"
"border-left-width:0;\n"
"}\n"
"/*QTableView \u5de6\u4e0a\u89d2\u6837\u5f0f*/\n"
"QTableView QTableCornerButton::section {\n"
"padding:3px;\n"
"margin:0px;\n"
"color:rgb(0, 0, 0);\n"
"border:0px;\n"
"border-left-width:0;\n"
"}\n"
"\n"
"QScrollBar::vertical {\n"
"background:transparent;\n"
"width:8px;\n"
"border:0px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"background:#6eb1f0;\n"
"width:8px;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"background:none;\n"
"border:none;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"background:none;\n"
"border:none;\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical {\n"
"background:transparent;\n"
"border:none;\n"
"}\n"
"\n"
"QScrollBar::sub-page:vertical {\n"
"background:transparent;\n"
"border:none;\n"
"}\n"
"\n"
"")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.gridLayout_24 = QGridLayout(self.frame_8)
        self.gridLayout_24.setObjectName(u"gridLayout_24")
        self.tableWidgetTasks = QTableWidget(self.frame_8)
        self.tableWidgetTasks.setObjectName(u"tableWidgetTasks")
        self.tableWidgetTasks.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidgetTasks.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidgetTasks.verticalHeader().setVisible(False)

        self.gridLayout_24.addWidget(self.tableWidgetTasks, 0, 0, 1, 3)

        self.widget_3 = QWidget(self.frame_8)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setMinimumSize(QSize(0, 40))
        self.widget_3.setStyleSheet(u"QPushButton{\n"
"border-radius:20px;\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(22, 155, 213);\n"
"}\n"
"QPushButton:hover{\n"
"color:rgb(255,255,255);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgb(206, 206, 206);\n"
"}")
        self.gridLayout_17 = QGridLayout(self.widget_3)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.gridLayout_17.setHorizontalSpacing(12)
        self.gridLayout_17.setVerticalSpacing(0)
        self.gridLayout_17.setContentsMargins(0, 0, 0, 0)
        self.addTask = QPushButton(self.widget_3)
        self.addTask.setObjectName(u"addTask")
        sizePolicy.setHeightForWidth(self.addTask.sizePolicy().hasHeightForWidth())
        self.addTask.setSizePolicy(sizePolicy)
        self.addTask.setFocusPolicy(Qt.NoFocus)

        self.gridLayout_17.addWidget(self.addTask, 0, 0, 1, 1)

        self.deleteTask = QPushButton(self.widget_3)
        self.deleteTask.setObjectName(u"deleteTask")
        sizePolicy.setHeightForWidth(self.deleteTask.sizePolicy().hasHeightForWidth())
        self.deleteTask.setSizePolicy(sizePolicy)
        self.deleteTask.setFocusPolicy(Qt.NoFocus)

        self.gridLayout_17.addWidget(self.deleteTask, 0, 1, 1, 1)

        self.modifyTask = QPushButton(self.widget_3)
        self.modifyTask.setObjectName(u"modifyTask")
        sizePolicy.setHeightForWidth(self.modifyTask.sizePolicy().hasHeightForWidth())
        self.modifyTask.setSizePolicy(sizePolicy)
        self.modifyTask.setFocusPolicy(Qt.NoFocus)

        self.gridLayout_17.addWidget(self.modifyTask, 0, 2, 1, 1)

        self.searchTask = QPushButton(self.widget_3)
        self.searchTask.setObjectName(u"searchTask")
        sizePolicy.setHeightForWidth(self.searchTask.sizePolicy().hasHeightForWidth())
        self.searchTask.setSizePolicy(sizePolicy)
        self.searchTask.setFocusPolicy(Qt.NoFocus)
        self.searchTask.setStyleSheet(u"")

        self.gridLayout_17.addWidget(self.searchTask, 0, 3, 1, 1)


        self.gridLayout_24.addWidget(self.widget_3, 1, 0, 1, 3)

        self.setWidget = QWidget(self.frame_8)
        self.setWidget.setObjectName(u"setWidget")
        self.setWidget.setStyleSheet(u"background-color: transparent;")
        self.gridLayout_22 = QGridLayout(self.setWidget)
        self.gridLayout_22.setObjectName(u"gridLayout_22")
        self.label_10 = QLabel(self.setWidget)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_22.addWidget(self.label_10, 0, 0, 1, 1)

        self.blurCheckBox = QCheckBox(self.setWidget)
        self.blurCheckBox.setObjectName(u"blurCheckBox")

        self.gridLayout_22.addWidget(self.blurCheckBox, 1, 0, 1, 1)

        self.timeCheckBox = QCheckBox(self.setWidget)
        self.timeCheckBox.setObjectName(u"timeCheckBox")

        self.gridLayout_22.addWidget(self.timeCheckBox, 2, 0, 1, 1)


        self.gridLayout_24.addWidget(self.setWidget, 2, 1, 1, 1)

        self.timeRangeWidget = QWidget(self.frame_8)
        self.timeRangeWidget.setObjectName(u"timeRangeWidget")
        self.timeRangeWidget.setStyleSheet(u"background-color: transparent;")
        self.gridLayout_8 = QGridLayout(self.timeRangeWidget)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.label_7 = QLabel(self.timeRangeWidget)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_8.addWidget(self.label_7, 0, 0, 1, 2)

        self.label_8 = QLabel(self.timeRangeWidget)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_8.addWidget(self.label_8, 1, 0, 1, 1)

        self.startTimeEdit = QDateTimeEdit(self.timeRangeWidget)
        self.startTimeEdit.setObjectName(u"startTimeEdit")
        sizePolicy.setHeightForWidth(self.startTimeEdit.sizePolicy().hasHeightForWidth())
        self.startTimeEdit.setSizePolicy(sizePolicy)
        self.startTimeEdit.setStyleSheet(u"background-color:rgb(85, 170, 255);")
        self.startTimeEdit.setDateTime(QDateTime(QDate(2020, 1, 1), QTime(0, 0, 0)))
        self.startTimeEdit.setDate(QDate(2020, 1, 1))
        self.startTimeEdit.setCalendarPopup(True)

        self.gridLayout_8.addWidget(self.startTimeEdit, 1, 1, 1, 1)

        self.label_9 = QLabel(self.timeRangeWidget)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_8.addWidget(self.label_9, 2, 0, 1, 1)

        self.endTimeEdit = QDateTimeEdit(self.timeRangeWidget)
        self.endTimeEdit.setObjectName(u"endTimeEdit")
        sizePolicy.setHeightForWidth(self.endTimeEdit.sizePolicy().hasHeightForWidth())
        self.endTimeEdit.setSizePolicy(sizePolicy)
        self.endTimeEdit.setStyleSheet(u"background-color:rgb(85, 170, 255);")
        self.endTimeEdit.setDateTime(QDateTime(QDate(2020, 1, 1), QTime(0, 0, 0)))
        self.endTimeEdit.setCalendarPopup(True)

        self.gridLayout_8.addWidget(self.endTimeEdit, 2, 1, 1, 1)


        self.gridLayout_24.addWidget(self.timeRangeWidget, 2, 2, 1, 1)

        self.conditionFrame = QFrame(self.frame_8)
        self.conditionFrame.setObjectName(u"conditionFrame")
        self.conditionFrame.setStyleSheet(u"background-color: transparent;")
        self.gridLayout_23 = QGridLayout(self.conditionFrame)
        self.gridLayout_23.setObjectName(u"gridLayout_23")
        self.label_13 = QLabel(self.conditionFrame)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_23.addWidget(self.label_13, 0, 0, 1, 1)

        self.label_14 = QLabel(self.conditionFrame)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout_23.addWidget(self.label_14, 1, 0, 1, 1)

        self.companyInput = QLineEdit(self.conditionFrame)
        self.companyInput.setObjectName(u"companyInput")
        self.companyInput.setStyleSheet(u"QLineEdit{\n"
"border-color:rgb(0, 0, 0);\n"
"border-style:solid;\n"
"border-top-width:0px;\n"
"border-right-width:0px;\n"
"border-bottom-width:2px;\n"
"border-left-width:0px;\n"
"}")

        self.gridLayout_23.addWidget(self.companyInput, 1, 1, 1, 1)

        self.label_17 = QLabel(self.conditionFrame)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout_23.addWidget(self.label_17, 2, 0, 1, 1)

        self.taskNameInput = QLineEdit(self.conditionFrame)
        self.taskNameInput.setObjectName(u"taskNameInput")
        self.taskNameInput.setStyleSheet(u"QLineEdit{\n"
"border-color:rgb(0, 0, 0);\n"
"border-style:solid;\n"
"border-top-width:0px;\n"
"border-right-width:0px;\n"
"border-bottom-width:2px;\n"
"border-left-width:0px;\n"
"}")

        self.gridLayout_23.addWidget(self.taskNameInput, 2, 1, 1, 1)

        self.label_18 = QLabel(self.conditionFrame)
        self.label_18.setObjectName(u"label_18")

        self.gridLayout_23.addWidget(self.label_18, 3, 0, 1, 1)

        self.taskNumInfo = QLineEdit(self.conditionFrame)
        self.taskNumInfo.setObjectName(u"taskNumInfo")
        self.taskNumInfo.setStyleSheet(u"QLineEdit{\n"
"border-color:rgb(0, 0, 0);\n"
"border-style:solid;\n"
"border-top-width:0px;\n"
"border-right-width:0px;\n"
"border-bottom-width:2px;\n"
"border-left-width:0px;\n"
"}")

        self.gridLayout_23.addWidget(self.taskNumInfo, 3, 1, 1, 1)


        self.gridLayout_24.addWidget(self.conditionFrame, 2, 0, 1, 1)


        self.gridLayout_7.addWidget(self.frame_8, 0, 0, 1, 1)

        self.frame_9 = QFrame(self.pageDatabase)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setStyleSheet(u"QTableWidget{\n"
"border:none;\n"
"}\n"
"/*\u8868\u5934*/\n"
"QHeaderView::section{\n"
"text-align:center;\n"
"padding:3px;\n"
"margin:0px;\n"
"color:rgb(0, 0, 0);\n"
"border:0px;\n"
"border-left-width:0;\n"
"}\n"
"/*QTableView \u5de6\u4e0a\u89d2\u6837\u5f0f*/\n"
"QTableView QTableCornerButton::section {\n"
"padding:3px;\n"
"margin:0px;\n"
"color:rgb(0, 0, 0);\n"
"border:0px;\n"
"border-left-width:0;\n"
"}\n"
"\n"
"QScrollBar::vertical {\n"
"background:transparent;\n"
"width:8px;\n"
"border:0px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"background:#6eb1f0;\n"
"width:8px;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"background:none;\n"
"border:none;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"background:none;\n"
"border:none;\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical {\n"
"background:transparent;\n"
"border:none;\n"
"}\n"
"\n"
"QScrollBar::sub-page:vertical {\n"
"background:transparent;\n"
"border:none;\n"
"}\n"
"QLineEdit{\n"
"background:transparent;\n"
"}\n"
"")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.gridLayout_26 = QGridLayout(self.frame_9)
        self.gridLayout_26.setObjectName(u"gridLayout_26")
        self.tableWidgetFilms = QTableWidget(self.frame_9)
        self.tableWidgetFilms.setObjectName(u"tableWidgetFilms")
        self.tableWidgetFilms.setStyleSheet(u"")
        self.tableWidgetFilms.verticalHeader().setVisible(False)

        self.gridLayout_26.addWidget(self.tableWidgetFilms, 0, 0, 1, 2)

        self.widget_5 = QWidget(self.frame_9)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setMinimumSize(QSize(0, 40))
        self.widget_5.setStyleSheet(u"QPushButton{\n"
"border-radius:20px;\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(22, 155, 213);\n"
"}\n"
"QPushButton:hover{\n"
"color:rgb(255,255,255);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgb(206, 206, 206);\n"
"}")
        self.gridLayout_25 = QGridLayout(self.widget_5)
        self.gridLayout_25.setObjectName(u"gridLayout_25")
        self.gridLayout_25.setHorizontalSpacing(6)
        self.gridLayout_25.setVerticalSpacing(0)
        self.gridLayout_25.setContentsMargins(0, 0, 0, 0)
        self.addFilm = QPushButton(self.widget_5)
        self.addFilm.setObjectName(u"addFilm")
        sizePolicy.setHeightForWidth(self.addFilm.sizePolicy().hasHeightForWidth())
        self.addFilm.setSizePolicy(sizePolicy)
        self.addFilm.setFocusPolicy(Qt.NoFocus)

        self.gridLayout_25.addWidget(self.addFilm, 0, 0, 1, 1)

        self.deleteFilm = QPushButton(self.widget_5)
        self.deleteFilm.setObjectName(u"deleteFilm")
        sizePolicy.setHeightForWidth(self.deleteFilm.sizePolicy().hasHeightForWidth())
        self.deleteFilm.setSizePolicy(sizePolicy)
        self.deleteFilm.setFocusPolicy(Qt.NoFocus)

        self.gridLayout_25.addWidget(self.deleteFilm, 0, 1, 1, 1)

        self.modifyFilm = QPushButton(self.widget_5)
        self.modifyFilm.setObjectName(u"modifyFilm")
        sizePolicy.setHeightForWidth(self.modifyFilm.sizePolicy().hasHeightForWidth())
        self.modifyFilm.setSizePolicy(sizePolicy)
        self.modifyFilm.setFocusPolicy(Qt.NoFocus)

        self.gridLayout_25.addWidget(self.modifyFilm, 0, 2, 1, 1)

        self.syncFilm = QPushButton(self.widget_5)
        self.syncFilm.setObjectName(u"syncFilm")
        sizePolicy.setHeightForWidth(self.syncFilm.sizePolicy().hasHeightForWidth())
        self.syncFilm.setSizePolicy(sizePolicy)
        self.syncFilm.setFocusPolicy(Qt.NoFocus)
        self.syncFilm.setStyleSheet(u"")

        self.gridLayout_25.addWidget(self.syncFilm, 0, 4, 1, 1)

        self.searchFilm = QPushButton(self.widget_5)
        self.searchFilm.setObjectName(u"searchFilm")
        sizePolicy.setHeightForWidth(self.searchFilm.sizePolicy().hasHeightForWidth())
        self.searchFilm.setSizePolicy(sizePolicy)
        self.searchFilm.setFocusPolicy(Qt.NoFocus)
        self.searchFilm.setStyleSheet(u"")

        self.gridLayout_25.addWidget(self.searchFilm, 0, 3, 1, 1)


        self.gridLayout_26.addWidget(self.widget_5, 1, 0, 1, 2)

        self.companyInput_2 = QLineEdit(self.frame_9)
        self.companyInput_2.setObjectName(u"companyInput_2")
        self.companyInput_2.setStyleSheet(u"QLineEdit{\n"
"border-color:rgb(0, 0, 0);\n"
"border-style:solid;\n"
"border-top-width:0px;\n"
"border-right-width:0px;\n"
"border-bottom-width:2px;\n"
"border-left-width:0px;\n"
"}")

        self.gridLayout_26.addWidget(self.companyInput_2, 2, 1, 1, 1)

        self.label_50 = QLabel(self.frame_9)
        self.label_50.setObjectName(u"label_50")

        self.gridLayout_26.addWidget(self.label_50, 2, 0, 1, 1)


        self.gridLayout_7.addWidget(self.frame_9, 0, 1, 1, 1)

        self.mainArea.addTab(self.pageDatabase, "")
        self.pageViewImage = QWidget()
        self.pageViewImage.setObjectName(u"pageViewImage")
        self.gridLayout = QGridLayout(self.pageViewImage)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame_21 = QFrame(self.pageViewImage)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setMinimumSize(QSize(330, 0))
        self.frame_21.setMaximumSize(QSize(600, 16777215))
        self.frame_21.setStyleSheet(u"")
        self.gridLayout_14 = QGridLayout(self.frame_21)
        self.gridLayout_14.setSpacing(0)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.gridLayout_14.setContentsMargins(0, 0, 0, 0)
        self.tableWidgetFiles = QTableWidget(self.frame_21)
        if (self.tableWidgetFiles.columnCount() < 2):
            self.tableWidgetFiles.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidgetFiles.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidgetFiles.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        if (self.tableWidgetFiles.rowCount() < 1):
            self.tableWidgetFiles.setRowCount(1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidgetFiles.setVerticalHeaderItem(0, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidgetFiles.setItem(0, 0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidgetFiles.setItem(0, 1, __qtablewidgetitem4)
        self.tableWidgetFiles.setObjectName(u"tableWidgetFiles")
        sizePolicy.setHeightForWidth(self.tableWidgetFiles.sizePolicy().hasHeightForWidth())
        self.tableWidgetFiles.setSizePolicy(sizePolicy)
        self.tableWidgetFiles.setMinimumSize(QSize(600, 0))
        self.tableWidgetFiles.setMaximumSize(QSize(16777215, 16777215))
        self.tableWidgetFiles.setStyleSheet(u"QTableWidget{\n"
"border:none;\n"
"}\n"
"/*\u8868\u5934*/\n"
"QHeaderView::section{\n"
"text-align:center;\n"
"padding:3px;\n"
"margin:0px;\n"
"color:rgb(0, 0, 0);\n"
"border:0px;\n"
"border-left-width:0;\n"
"}\n"
"/*QTableView \u5de6\u4e0a\u89d2\u6837\u5f0f*/\n"
"QTableView QTableCornerButton::section {\n"
"padding:3px;\n"
"margin:0px;\n"
"color:rgb(0, 0, 0);\n"
"border:0px;\n"
"border-left-width:0;\n"
"}\n"
"\n"
"QScrollBar::vertical {\n"
"background:transparent;\n"
"width:8px;\n"
"border:0px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"background:#6eb1f0;\n"
"width:8px;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"background:none;\n"
"border:none;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"background:none;\n"
"border:none;\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical {\n"
"background:transparent;\n"
"border:none;\n"
"}\n"
"\n"
"QScrollBar::sub-page:vertical {\n"
"background:transparent;\n"
"border:none;\n"
"}\n"
"")
        self.tableWidgetFiles.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidgetFiles.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidgetFiles.setSortingEnabled(True)
        self.tableWidgetFiles.horizontalHeader().setStretchLastSection(False)
        self.tableWidgetFiles.verticalHeader().setStretchLastSection(False)

        self.gridLayout_14.addWidget(self.tableWidgetFiles, 0, 0, 1, 2)


        self.gridLayout.addWidget(self.frame_21, 0, 0, 1, 1)

        self.widget_4 = QWidget(self.pageViewImage)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setMinimumSize(QSize(0, 470))
        self.widget_4.setMaximumSize(QSize(16777215, 16777215))
        self.widget_4.setStyleSheet(u"background-color: #169BD5;")
        self.gridLayout_19 = QGridLayout(self.widget_4)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.gridLayout_19.setHorizontalSpacing(3)
        self.gridLayout_19.setVerticalSpacing(6)
        self.gridLayout_19.setContentsMargins(3, 3, 3, 3)
        self.graphicsView = ImageViewer(self.widget_4)
        self.graphicsView.setObjectName(u"graphicsView")
        self.graphicsView.setMinimumSize(QSize(0, 470))
        self.graphicsView.setMaximumSize(QSize(16777215, 16777215))
        self.graphicsView.setStyleSheet(u"background-color:rgb(255, 255, 255);\n"
"border:none;")

        self.gridLayout_19.addWidget(self.graphicsView, 1, 0, 1, 1)

        self.frame_6 = QFrame(self.widget_4)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMinimumSize(QSize(0, 316))
        self.frame_6.setMaximumSize(QSize(16777215, 16777215))
        self.frame_6.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_19.addWidget(self.frame_6, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.widget_4, 0, 1, 1, 1)

        self.mainArea.addTab(self.pageViewImage, "")
        self.pageDefect = QWidget()
        self.pageDefect.setObjectName(u"pageDefect")
        self.gridLayout_21 = QGridLayout(self.pageDefect)
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.frame_4 = QFrame(self.pageDefect)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(330, 0))
        self.frame_4.setMaximumSize(QSize(330, 16777215))
        self.gridLayout_15 = QGridLayout(self.frame_4)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.label_31 = QLabel(self.frame_4)
        self.label_31.setObjectName(u"label_31")

        self.gridLayout_15.addWidget(self.label_31, 0, 0, 1, 1)

        self.comboBox = QComboBox(self.frame_4)
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

        self.lineEdit_3 = QLineEdit(self.frame_4)
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

        self.lineEdit_5 = QLineEdit(self.frame_4)
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

        self.label_33 = QLabel(self.frame_4)
        self.label_33.setObjectName(u"label_33")

        self.gridLayout_15.addWidget(self.label_33, 2, 0, 1, 1)

        self.label_39 = QLabel(self.frame_4)
        self.label_39.setObjectName(u"label_39")

        self.gridLayout_15.addWidget(self.label_39, 7, 0, 1, 1)

        self.label_32 = QLabel(self.frame_4)
        self.label_32.setObjectName(u"label_32")

        self.gridLayout_15.addWidget(self.label_32, 1, 0, 1, 2)

        self.label_41 = QLabel(self.frame_4)
        self.label_41.setObjectName(u"label_41")

        self.gridLayout_15.addWidget(self.label_41, 5, 0, 1, 1)

        self.label_40 = QLabel(self.frame_4)
        self.label_40.setObjectName(u"label_40")

        self.gridLayout_15.addWidget(self.label_40, 8, 0, 1, 1)

        self.label_34 = QLabel(self.frame_4)
        self.label_34.setObjectName(u"label_34")

        self.gridLayout_15.addWidget(self.label_34, 3, 0, 1, 1)

        self.lineEdit_2 = QLineEdit(self.frame_4)
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

        self.scrollArea = QScrollArea(self.frame_4)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"border:none;\n"
"background-color: rgb(245, 245, 245);")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 312, 549))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_15.addWidget(self.scrollArea, 6, 0, 1, 3)

        self.lineEdit_4 = QLineEdit(self.frame_4)
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

        self.comboBox_2 = QComboBox(self.frame_4)
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

        self.widget = QWidget(self.frame_4)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(0, 30))
        self.widget.setStyleSheet(u"background-color: transparent;")
        self.gridLayout_16 = QGridLayout(self.widget)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.pushButton_7 = QPushButton(self.widget)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setMinimumSize(QSize(120, 28))
        self.pushButton_7.setMaximumSize(QSize(120, 28))
        self.pushButton_7.setStyleSheet(u"QPushButton{\n"
"border-radius:10px;\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(22, 155, 213);\n"
"}\n"
"QPushButton:hover{\n"
"color:rgb(255,255,255);\n"
"}\n"
"QPushButton:pressed{\n"
"border-radius:10px;\n"
"background-color: rgb(206, 206, 206);\n"
"}")

        self.gridLayout_16.addWidget(self.pushButton_7, 0, 0, 1, 1)

        self.pushButton_8 = QPushButton(self.widget)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setMinimumSize(QSize(120, 26))
        self.pushButton_8.setMaximumSize(QSize(120, 16777215))
        self.pushButton_8.setStyleSheet(u"QPushButton{\n"
"border-radius:10px;\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(22, 155, 213);\n"
"}\n"
"QPushButton:hover{\n"
"color:rgb(255,255,255);\n"
"}\n"
"QPushButton:pressed{\n"
"border-radius:10px;\n"
"background-color: rgb(206, 206, 206);\n"
"}")

        self.gridLayout_16.addWidget(self.pushButton_8, 0, 1, 1, 1)


        self.gridLayout_15.addWidget(self.widget, 4, 0, 1, 3)


        self.gridLayout_21.addWidget(self.frame_4, 0, 0, 2, 1)

        self.frame_5 = QFrame(self.pageDefect)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(0, 0))
        self.frame_5.setMaximumSize(QSize(16777215, 16777215))
        self.gridLayout_18 = QGridLayout(self.frame_5)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.gridLayout_18.setContentsMargins(0, 0, 0, 0)
        self.label_45 = QLabel(self.frame_5)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setMinimumSize(QSize(0, 24))
        self.label_45.setAlignment(Qt.AlignCenter)

        self.gridLayout_18.addWidget(self.label_45, 4, 0, 1, 1)

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

        self.gridLayout_18.addWidget(self.comboBox_4, 2, 1, 1, 3)

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

        self.gridLayout_18.addWidget(self.comboBox_6, 4, 1, 1, 2)

        self.pushButton_14 = QPushButton(self.frame_5)
        self.pushButton_14.setObjectName(u"pushButton_14")
        self.pushButton_14.setMinimumSize(QSize(60, 26))
        self.pushButton_14.setStyleSheet(u"border-radius:10px;\n"
"background-color: rgb(22, 155, 213);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_18.addWidget(self.pushButton_14, 1, 4, 1, 1)

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

        self.gridLayout_18.addWidget(self.comboBox_5, 3, 1, 1, 4)

        self.label_44 = QLabel(self.frame_5)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setMinimumSize(QSize(0, 24))
        self.label_44.setAlignment(Qt.AlignCenter)

        self.gridLayout_18.addWidget(self.label_44, 3, 0, 1, 1)

        self.tableWidget = QTableWidget(self.frame_5)
        if (self.tableWidget.columnCount() < 6):
            self.tableWidget.setColumnCount(6)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem10)
        if (self.tableWidget.rowCount() < 1):
            self.tableWidget.setRowCount(1)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem11)
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
"border:0px;\n"
"border-left-width:0;\n"
"}\n"
"/*QTableView \u5de6\u4e0a\u89d2\u6837\u5f0f*/\n"
"QTableView QTableCornerButton::section {\n"
"padding:3px;\n"
"margin:0px;\n"
"color:rgb(0, 0, 0);\n"
"border:0px;\n"
"border-left-width:0;\n"
"}\n"
"QListWidget{\n"
"background-color:#2F2F2F;\n"
"color:white;\n"
"border:none;\n"
"}\n"
"\n"
"QScrollBar::vertical {\n"
"background:transparent;\n"
"width:8px;\n"
"border:0px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"background:#6eb1f0;\n"
"width:8px;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"background:none;\n"
"border:none;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"background:none;\n"
"border:none;\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical {\n"
"background:transparent;\n"
"border:none;\n"
"}\n"
"\n"
"QScrollBar::sub-page:vertical {\n"
"background:transparent;\n"
"border:none;"
                        "\n"
"}\n"
"")
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setSortingEnabled(True)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.verticalHeader().setVisible(True)

        self.gridLayout_18.addWidget(self.tableWidget, 0, 0, 1, 5)

        self.pushButton_15 = QPushButton(self.frame_5)
        self.pushButton_15.setObjectName(u"pushButton_15")
        self.pushButton_15.setMinimumSize(QSize(60, 26))
        self.pushButton_15.setStyleSheet(u"border-radius:10px;\n"
"background-color: rgb(22, 155, 213);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_18.addWidget(self.pushButton_15, 2, 4, 1, 1)

        self.label_43 = QLabel(self.frame_5)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setMinimumSize(QSize(0, 24))
        self.label_43.setAlignment(Qt.AlignCenter)

        self.gridLayout_18.addWidget(self.label_43, 2, 0, 1, 1)

        self.label_46 = QLabel(self.frame_5)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setMinimumSize(QSize(0, 24))
        self.label_46.setAlignment(Qt.AlignCenter)

        self.gridLayout_18.addWidget(self.label_46, 4, 3, 1, 1)

        self.label_42 = QLabel(self.frame_5)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setMinimumSize(QSize(0, 24))
        self.label_42.setAlignment(Qt.AlignCenter)

        self.gridLayout_18.addWidget(self.label_42, 1, 0, 1, 1)

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

        self.gridLayout_18.addWidget(self.comboBox_3, 1, 1, 1, 3)

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

        self.gridLayout_18.addWidget(self.comboBox_7, 4, 4, 1, 1)


        self.gridLayout_21.addWidget(self.frame_5, 0, 1, 1, 1)

        self.mainArea.addTab(self.pageDefect, "")

        self.verticalLayout.addWidget(self.mainArea)

        self.statebar = QWidget(self.centralwidget)
        self.statebar.setObjectName(u"statebar")
        sizePolicy2.setHeightForWidth(self.statebar.sizePolicy().hasHeightForWidth())
        self.statebar.setSizePolicy(sizePolicy2)
        self.statebar.setMinimumSize(QSize(0, 30))
        self.statebar.setStyleSheet(u"background-color: rgb(22, 78, 134);\n"
"color:#FFFFFF;")
        self.gridLayout_27 = QGridLayout(self.statebar)
        self.gridLayout_27.setSpacing(0)
        self.gridLayout_27.setObjectName(u"gridLayout_27")
        self.gridLayout_27.setContentsMargins(0, 0, 0, 0)
        self.statePathNow = QLabel(self.statebar)
        self.statePathNow.setObjectName(u"statePathNow")

        self.gridLayout_27.addWidget(self.statePathNow, 0, 1, 1, 1)

        self.label_52 = QLabel(self.statebar)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setMaximumSize(QSize(80, 16777215))

        self.gridLayout_27.addWidget(self.label_52, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.statebar)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.mainArea.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u8bc4\u7247", None))
        self.actionOpen.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00", None))
        self.actionOpenDatabase.setText(QCoreApplication.translate("MainWindow", u"\u4ece\u6570\u636e\u5e93\u6253\u5f00", None))
        self.actionPrintPreview.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5370\u9884\u89c8", None))
        self.actionPrintConfig.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5370\u8bbe\u7f6e", None))
        self.actionCloudConnect.setText(QCoreApplication.translate("MainWindow", u"\u4e91\u7aef\u8fde\u63a5", None))
        self.pushButtonFile.setText(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6", None))
        self.pushButtonConfig.setText(QCoreApplication.translate("MainWindow", u"\u914d\u7f6e", None))
        self.pushButtonTools.setText(QCoreApplication.translate("MainWindow", u"\u5de5\u5177", None))
        self.pushButtonView.setText(QCoreApplication.translate("MainWindow", u"\u89c6\u56fe", None))
        self.pushButtonHelp.setText(QCoreApplication.translate("MainWindow", u"\u5e2e\u52a9", None))
        self.label_5.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u91cd\u590d\u7247\u68c0\u7d22", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u81ea\u52a8\u8bc6\u522b", None))
        self.label_2.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u6587\u5b57\u8bc6\u522b", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"\u539f\u59cb\u5927\u5c0f", None))
        self.label_15.setText("")
        self.label_11.setText("")
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"\u6c34\u5e73\u7ffb\u8f6c", None))
        self.label_29.setText("")
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"\u539f\u59cb\u56fe\u50cf", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u89c6\u56fe\u64cd\u4f5c", None))
        self.label_19.setText("")
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"\u81ea\u52a8\u8c03\u6574", None))
        self.label_22.setText("")
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"\u8272\u5f69\u8c03\u6574", None))
        self.label_24.setText("")
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"\u7070\u5ea6\u66f2\u7ebf", None))
        self.label_27.setText("")
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"\u5c40\u90e8\u8c03\u6574", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"\u56fe\u50cf\u589e\u5f3a", None))
        self.label_49.setText("")
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"\u7f3a\u9677\u68c0\u6d4b", None))
        self.label_38.setText("")
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"\u7f3a\u9677\u81ea\u52a8\u5b9a\u4f4d", None))
        self.label_47.setText("")
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"\u7f3a\u9677\u624b\u52a8\u5b9a\u4f4d", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"\u7f3a\u9677\u8bc6\u522b", None))
        self.label_30.setText("")
        self.mainArea.setTabText(self.mainArea.indexOf(self.pageStart), QCoreApplication.translate("MainWindow", u"\u5f00\u59cb", None))
        self.addTask.setText(QCoreApplication.translate("MainWindow", u"\u6dfb\u52a0\u4efb\u52a1", None))
        self.deleteTask.setText(QCoreApplication.translate("MainWindow", u"\u5220\u9664\u4efb\u52a1", None))
        self.modifyTask.setText(QCoreApplication.translate("MainWindow", u"\u4fee\u6539\u4efb\u52a1", None))
        self.searchTask.setText(QCoreApplication.translate("MainWindow", u"\u67e5\u8be2\u4efb\u52a1", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u67e5\u8be2\u8bbe\u7f6e", None))
        self.blurCheckBox.setText(QCoreApplication.translate("MainWindow", u"\u6a21\u7cca\u67e5\u8be2", None))
        self.timeCheckBox.setText(QCoreApplication.translate("MainWindow", u"\u65e0\u65f6\u95f4\u6761\u4ef6\u9650\u5236", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u67e5\u8be2\u65f6\u95f4\u8303\u56f4", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u8d77\u59cb\u65f6\u95f4", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u7ec8\u6b62\u65f6\u95f4", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"\u67e5\u8be2\u6761\u4ef6", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"\u5355\u4f4d\u540d\u79f0", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"\u4efb\u52a1\u540d\u79f0", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"\u4efb\u52a1\u7f16\u53f7", None))
        self.addFilm.setText(QCoreApplication.translate("MainWindow", u"\u6dfb\u52a0\u5e95\u7247", None))
        self.deleteFilm.setText(QCoreApplication.translate("MainWindow", u"\u5220\u9664\u5e95\u7247", None))
        self.modifyFilm.setText(QCoreApplication.translate("MainWindow", u"\u4fee\u6539\u5e95\u7247", None))
        self.syncFilm.setText(QCoreApplication.translate("MainWindow", u"\u540c\u6b65\u5e95\u7247", None))
        self.searchFilm.setText(QCoreApplication.translate("MainWindow", u"\u67e5\u8be2\u5e95\u7247", None))
        self.label_50.setText(QCoreApplication.translate("MainWindow", u"\u67e5\u8be2\u6761\u4ef6", None))
        self.mainArea.setTabText(self.mainArea.indexOf(self.pageDatabase), QCoreApplication.translate("MainWindow", u"\u6570\u636e\u5e93", None))
        ___qtablewidgetitem = self.tableWidgetFiles.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u540d\u79f0", None));
        ___qtablewidgetitem1 = self.tableWidgetFiles.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u8def\u5f84", None));
        ___qtablewidgetitem2 = self.tableWidgetFiles.verticalHeaderItem(0)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"1", None));

        __sortingEnabled = self.tableWidgetFiles.isSortingEnabled()
        self.tableWidgetFiles.setSortingEnabled(False)
        ___qtablewidgetitem3 = self.tableWidgetFiles.item(0, 0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"picture_name", None));
        ___qtablewidgetitem4 = self.tableWidgetFiles.item(0, 1)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"X:/xxxx/xxxx/xxxxxx/picture_name.mim", None));
        self.tableWidgetFiles.setSortingEnabled(__sortingEnabled)

        self.mainArea.setTabText(self.mainArea.indexOf(self.pageViewImage), QCoreApplication.translate("MainWindow", u"\u56fe\u50cf\u67e5\u770b", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"\u4ea7\u54c1\u7f16\u53f7", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"\u90e8\u4f4d\u7f16\u53f7", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"\u6267\u884c\u6807\u51c6", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"\u710a\u63a5\u63a5\u5934\u7f16\u53f7", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"\u5e95\u7247\u4fe1\u606f", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"\u62cd\u6444\u7ea7\u522b", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"\u900f\u7167\u65e5\u671f", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"\u8bc4\u7247\u5907\u6ce8", None))
        self.pushButton_14.setText(QCoreApplication.translate("MainWindow", u"\u91cd\u7f6e", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"\u7f3a\u9677\u6027\u8d28", None))
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"\u7f16\u53f7", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"\u7c7b\u578b", None));
        ___qtablewidgetitem7 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"\u5bbd\u5ea6", None));
        ___qtablewidgetitem8 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"\u957f\u5ea6", None));
        ___qtablewidgetitem9 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"\u5b9a\u91cf", None));
        ___qtablewidgetitem10 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"\u5904\u7406", None));
        ___qtablewidgetitem11 = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"1", None));
        self.pushButton_15.setText(QCoreApplication.translate("MainWindow", u"\u8bc4\u5b9a", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"\u5e95\u7247\u7b49\u7ea7", None))
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"\u6807\u8bb0\u9f50\u5168", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"\u8bc4\u5b9a\u6807\u51c6", None))
        self.comboBox_7.setItemText(0, QCoreApplication.translate("MainWindow", u"\u5426", None))
        self.comboBox_7.setItemText(1, QCoreApplication.translate("MainWindow", u"\u662f", None))

        self.mainArea.setTabText(self.mainArea.indexOf(self.pageDefect), QCoreApplication.translate("MainWindow", u"\u7f3a\u9677\u4fe1\u606f", None))
        self.statePathNow.setText("")
        self.label_52.setText(QCoreApplication.translate("MainWindow", u"\u5f53\u524d\u56fe\u50cf\u8def\u5f84", None))
    # retranslateUi

