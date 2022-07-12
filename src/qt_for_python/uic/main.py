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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QSplitter, QStackedWidget, QToolButton,
    QVBoxLayout, QWidget)
import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1280, 960)
        MainWindow.setMinimumSize(QSize(1280, 960))
        icon = QIcon()
        icon.addFile(u":/images/images/\u8ba1\u7b97\u673a.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(0, 0))
        self.centralwidget.setStyleSheet(u"#centralwidget{\n"
"background-color: #FFFFFF;\n"
"}\n"
"#toolPages{\n"
"	background-color:	qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(250, 250, 250, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"	border-radius:8px;\n"
"}\n"
"#menubar{\n"
"background-color:#164E86;\n"
"}\n"
"#menubar QPushButton{\n"
"	background-color: transparent;\n"
"	color:#FFFFFF;\n"
"}\n"
"#menubar QPushButton:hover{\n"
"	font-weight:bold;\n"
"	font-size:12pt;\n"
"}\n"
"#menubar QPushButton[select=true]{\n"
"	font-weight:bold;\n"
"	font-size:12pt;\n"
"}\n"
"#statusbar{\n"
"background-color:#164E86;\n"
"}\n"
"")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.menubar = QWidget(self.centralwidget)
        self.menubar.setObjectName(u"menubar")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.menubar.sizePolicy().hasHeightForWidth())
        self.menubar.setSizePolicy(sizePolicy)
        self.menubar.setMinimumSize(QSize(0, 30))
        self.menubar.setStyleSheet(u"")
        self.horizontalLayout = QHBoxLayout(self.menubar)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.taskbutton = QPushButton(self.menubar)
        self.taskbutton.setObjectName(u"taskbutton")
        font = QFont()
        font.setPointSize(10)
        self.taskbutton.setFont(font)
        self.taskbutton.setCheckable(False)

        self.horizontalLayout.addWidget(self.taskbutton)

        self.judgebutton = QPushButton(self.menubar)
        self.judgebutton.setObjectName(u"judgebutton")
        self.judgebutton.setFont(font)
        self.judgebutton.setCheckable(False)

        self.horizontalLayout.addWidget(self.judgebutton)

        self.recordbutton = QPushButton(self.menubar)
        self.recordbutton.setObjectName(u"recordbutton")
        self.recordbutton.setFont(font)
        self.recordbutton.setCheckable(False)

        self.horizontalLayout.addWidget(self.recordbutton)

        self.configbutton = QPushButton(self.menubar)
        self.configbutton.setObjectName(u"configbutton")
        self.configbutton.setFont(font)
        self.configbutton.setCheckable(False)

        self.horizontalLayout.addWidget(self.configbutton)

        self.viewbutton = QPushButton(self.menubar)
        self.viewbutton.setObjectName(u"viewbutton")
        self.viewbutton.setFont(font)
        self.viewbutton.setCheckable(False)

        self.horizontalLayout.addWidget(self.viewbutton)

        self.helpbutton = QPushButton(self.menubar)
        self.helpbutton.setObjectName(u"helpbutton")
        self.helpbutton.setFont(font)
        self.helpbutton.setCheckable(False)

        self.horizontalLayout.addWidget(self.helpbutton)

        self.horizontalSpacer = QSpacerItem(347, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout.addWidget(self.menubar)

        self.tools = QStackedWidget(self.centralwidget)
        self.tools.setObjectName(u"tools")
        self.tools.setMaximumSize(QSize(16777215, 80))
        self.tools.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(240, 240, 240, 255), stop:1 rgba(255, 255, 255, 255));")
        self.taskpage = QWidget()
        self.taskpage.setObjectName(u"taskpage")
        self.taskpage.setStyleSheet(u"QToolButton{\n"
"border:none;\n"
"}\n"
"QLabel{\n"
"	background-color:transparent;\n"
"}")
        self.gridLayout = QGridLayout(self.taskpage)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 2, 0, 2)
        self.frame = QFrame(self.taskpage)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(120, 0))
        self.frame.setStyleSheet(u"QWidget.QFrame{\n"
"border-right:1px solid black;\n"
"}")
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(9, 0, 9, 0)
        self.widget = QWidget(self.frame)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout_3 = QHBoxLayout(self.widget)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.taskManage = QToolButton(self.widget)
        self.taskManage.setObjectName(u"taskManage")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.taskManage.sizePolicy().hasHeightForWidth())
        self.taskManage.setSizePolicy(sizePolicy1)
        self.taskManage.setMaximumSize(QSize(50, 16777215))
        self.taskManage.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u":/images/images/\u6253\u5f00.png", QSize(), QIcon.Normal, QIcon.Off)
        self.taskManage.setIcon(icon1)
        self.taskManage.setIconSize(QSize(25, 25))
        self.taskManage.setAutoRepeat(False)
        self.taskManage.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.horizontalLayout_3.addWidget(self.taskManage)


        self.verticalLayout_3.addWidget(self.widget)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 20))
        font1 = QFont()
        font1.setPointSize(8)
        self.label.setFont(font1)

        self.verticalLayout_3.addWidget(self.label, 0, Qt.AlignHCenter)


        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(1217, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 0, 1, 1, 1)

        self.tools.addWidget(self.taskpage)
        self.judgepage = QWidget()
        self.judgepage.setObjectName(u"judgepage")
        self.tools.addWidget(self.judgepage)
        self.recordpage = QWidget()
        self.recordpage.setObjectName(u"recordpage")
        self.tools.addWidget(self.recordpage)
        self.configpage = QWidget()
        self.configpage.setObjectName(u"configpage")
        self.tools.addWidget(self.configpage)
        self.viewpage = QWidget()
        self.viewpage.setObjectName(u"viewpage")
        self.tools.addWidget(self.viewpage)
        self.helppage = QWidget()
        self.helppage.setObjectName(u"helppage")
        self.tools.addWidget(self.helppage)

        self.verticalLayout.addWidget(self.tools)

        self.main = QWidget(self.centralwidget)
        self.main.setObjectName(u"main")
        self.horizontalLayout_2 = QHBoxLayout(self.main)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.mainSplitter = QSplitter(self.main)
        self.mainSplitter.setObjectName(u"mainSplitter")
        self.mainSplitter.setMinimumSize(QSize(200, 200))
        self.mainSplitter.setOrientation(Qt.Horizontal)
        self.mainSplitter.setOpaqueResize(True)
        self.mainSplitter.setHandleWidth(5)
        self.leftInfo = QWidget(self.mainSplitter)
        self.leftInfo.setObjectName(u"leftInfo")
        self.leftInfo.setMinimumSize(QSize(300, 0))
        self.gridLayout_2 = QGridLayout(self.leftInfo)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.mainSplitter.addWidget(self.leftInfo)
        self.imageInfo = QWidget(self.mainSplitter)
        self.imageInfo.setObjectName(u"imageInfo")
        self.imageInfo.setMinimumSize(QSize(0, 0))
        self.verticalLayout_2 = QVBoxLayout(self.imageInfo)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.imageSplitter = QSplitter(self.imageInfo)
        self.imageSplitter.setObjectName(u"imageSplitter")
        self.imageSplitter.setMinimumSize(QSize(400, 0))
        self.imageSplitter.setOrientation(Qt.Vertical)
        self.widget_4 = QWidget(self.imageSplitter)
        self.widget_4.setObjectName(u"widget_4")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.widget_4.sizePolicy().hasHeightForWidth())
        self.widget_4.setSizePolicy(sizePolicy2)
        self.widget_4.setMinimumSize(QSize(0, 250))
        self.imageSplitter.addWidget(self.widget_4)
        self.widget_5 = QWidget(self.imageSplitter)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setMinimumSize(QSize(0, 400))
        self.gridLayout_3 = QGridLayout(self.widget_5)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.imageSplitter.addWidget(self.widget_5)

        self.verticalLayout_2.addWidget(self.imageSplitter)

        self.mainSplitter.addWidget(self.imageInfo)
        self.rightIno = QWidget(self.mainSplitter)
        self.rightIno.setObjectName(u"rightIno")
        self.rightIno.setMinimumSize(QSize(300, 0))
        self.mainSplitter.addWidget(self.rightIno)

        self.horizontalLayout_2.addWidget(self.mainSplitter)


        self.verticalLayout.addWidget(self.main)

        self.statusbar = QWidget(self.centralwidget)
        self.statusbar.setObjectName(u"statusbar")
        self.statusbar.setMinimumSize(QSize(0, 20))
        self.statusbar.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout.addWidget(self.statusbar)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u8ba1\u7b97\u673a\u8f85\u52a9\u8bc4\u7247\u7cfb\u7edf", None))
        self.taskbutton.setText(QCoreApplication.translate("MainWindow", u"\u4efb\u52a1", None))
        self.judgebutton.setText(QCoreApplication.translate("MainWindow", u"\u8bc4\u4ef7", None))
        self.recordbutton.setText(QCoreApplication.translate("MainWindow", u"\u8bb0\u5f55", None))
        self.configbutton.setText(QCoreApplication.translate("MainWindow", u"\u914d\u7f6e", None))
        self.viewbutton.setText(QCoreApplication.translate("MainWindow", u"\u89c6\u56fe", None))
        self.helpbutton.setText(QCoreApplication.translate("MainWindow", u"\u5e2e\u52a9", None))
        self.taskManage.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00\u4efb\u52a1", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u4efb\u52a1\u7ba1\u7406", None))
    # retranslateUi

