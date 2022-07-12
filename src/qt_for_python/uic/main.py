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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QSplitter,
    QStackedWidget, QTabWidget, QTableWidgetItem, QToolButton,
    QVBoxLayout, QWidget)

from utils.utils_qt.filmInfo import FilmInfo
from utils.utils_qt.imageViewer import ImageViewer
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
        self.centralwidget.setStyleSheet(u"")
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
        self.menubar.setStyleSheet(u"QWidget{\n"
"background-color:#164E86;\n"
"}\n"
"QPushButton{\n"
"	background-color: transparent;\n"
"	color:#FFFFFF;\n"
"}\n"
"QPushButton:hover{\n"
"	font-weight:bold;\n"
"	font-size:12pt;\n"
"}\n"
"QPushButton[select=true]{\n"
"	font-weight:bold;\n"
"	font-size:12pt;\n"
"}\n"
"")
        self.horizontalLayout = QHBoxLayout(self.menubar)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.startbutton = QPushButton(self.menubar)
        self.startbutton.setObjectName(u"startbutton")
        font = QFont()
        font.setPointSize(10)
        self.startbutton.setFont(font)
        self.startbutton.setCheckable(False)

        self.horizontalLayout.addWidget(self.startbutton)

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
        self.tools.setStyleSheet(u"QWidget{\n"
"background-color: #FFFFFF;\n"
"}\n"
"QStackedWidget{\n"
"background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(240, 240, 240, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"QToolButton {\n"
"    background-color: #ffffff;\n"
"    border: none;\n"
"}\n"
"\n"
"QToolButton:hover {\n"
"    background-color: #ecf5ff;\n"
"    color: #409eff;\n"
"}\n"
"\n"
"QToolButton:pressed, QToolButton:checked {\n"
"    color: #409eff;\n"
"}")
        self.startpage = QWidget()
        self.startpage.setObjectName(u"startpage")
        self.startpage.setStyleSheet(u"#startpage{\n"
"border-bottom:1px solid black;\n"
"}\n"
"QWidget.QFrame{\n"
"	border-right:1px solid black;\n"
"}\n"
"QLabel{\n"
"	background-color:transparent;\n"
"	border-top:1px solid black;\n"
"}")
        self.horizontalLayout_8 = QHBoxLayout(self.startpage)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 2)
        self.frame = QFrame(self.startpage)
        self.frame.setObjectName(u"frame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy1)
        self.frame.setMinimumSize(QSize(0, 0))
        self.frame.setStyleSheet(u"")
        self.gridLayout_4 = QGridLayout(self.frame)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(9, 0, 9, 0)
        self.widget = QWidget(self.frame)
        self.widget.setObjectName(u"widget")
        sizePolicy1.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy1)
        self.widget.setStyleSheet(u"")
        self.horizontalLayout_3 = QHBoxLayout(self.widget)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.taskManage = QToolButton(self.widget)
        self.taskManage.setObjectName(u"taskManage")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.taskManage.sizePolicy().hasHeightForWidth())
        self.taskManage.setSizePolicy(sizePolicy2)
        self.taskManage.setMaximumSize(QSize(100, 16777215))
        self.taskManage.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u":/images/images/\u4efb\u52a1\u7ba1\u7406.png", QSize(), QIcon.Normal, QIcon.Off)
        self.taskManage.setIcon(icon1)
        self.taskManage.setIconSize(QSize(25, 25))
        self.taskManage.setAutoRepeat(False)
        self.taskManage.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.horizontalLayout_3.addWidget(self.taskManage)


        self.gridLayout_4.addWidget(self.widget, 0, 0, 1, 1)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 20))
        font1 = QFont()
        font1.setPointSize(8)
        self.label.setFont(font1)
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label, 1, 0, 1, 1)


        self.horizontalLayout_8.addWidget(self.frame)

        self.frame_5 = QFrame(self.startpage)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy1.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy1)
        self.frame_5.setMinimumSize(QSize(0, 0))
        self.frame_5.setStyleSheet(u"")
        self.gridLayout_5 = QGridLayout(self.frame_5)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(9, 0, 9, 0)
        self.widget_7 = QWidget(self.frame_5)
        self.widget_7.setObjectName(u"widget_7")
        sizePolicy1.setHeightForWidth(self.widget_7.sizePolicy().hasHeightForWidth())
        self.widget_7.setSizePolicy(sizePolicy1)
        self.widget_7.setStyleSheet(u"")
        self.gridLayout = QGridLayout(self.widget_7)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setVerticalSpacing(2)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.taskManage_5 = QToolButton(self.widget_7)
        self.taskManage_5.setObjectName(u"taskManage_5")
        sizePolicy.setHeightForWidth(self.taskManage_5.sizePolicy().hasHeightForWidth())
        self.taskManage_5.setSizePolicy(sizePolicy)
        self.taskManage_5.setMaximumSize(QSize(16777215, 16777215))
        self.taskManage_5.setStyleSheet(u"")
        icon2 = QIcon()
        icon2.addFile(u":/images/images/\u4f2a\u8272\u5f69\u589e\u5f3a\u8d44\u6e90 25.png", QSize(), QIcon.Normal, QIcon.Off)
        self.taskManage_5.setIcon(icon2)
        self.taskManage_5.setIconSize(QSize(20, 20))
        self.taskManage_5.setAutoRepeat(False)
        self.taskManage_5.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        self.gridLayout.addWidget(self.taskManage_5, 0, 0, 1, 1)

        self.toolButton_3 = QToolButton(self.widget_7)
        self.toolButton_3.setObjectName(u"toolButton_3")
        sizePolicy.setHeightForWidth(self.toolButton_3.sizePolicy().hasHeightForWidth())
        self.toolButton_3.setSizePolicy(sizePolicy)
        icon3 = QIcon()
        icon3.addFile(u":/images/images/\u4eae\u5ea6\u8c03\u8282.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_3.setIcon(icon3)
        self.toolButton_3.setIconSize(QSize(20, 20))
        self.toolButton_3.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        self.gridLayout.addWidget(self.toolButton_3, 1, 0, 1, 1)

        self.toolButton_4 = QToolButton(self.widget_7)
        self.toolButton_4.setObjectName(u"toolButton_4")
        sizePolicy.setHeightForWidth(self.toolButton_4.sizePolicy().hasHeightForWidth())
        self.toolButton_4.setSizePolicy(sizePolicy)
        icon4 = QIcon()
        icon4.addFile(u":/images/images/\u7070\u5ea6\u66f2\u7ebf\u589e\u5f3a\u8d44\u6e90 26.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_4.setIcon(icon4)
        self.toolButton_4.setIconSize(QSize(16, 16))
        self.toolButton_4.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        self.gridLayout.addWidget(self.toolButton_4, 2, 0, 1, 1)


        self.gridLayout_5.addWidget(self.widget_7, 0, 0, 1, 1)

        self.label_5 = QLabel(self.frame_5)
        self.label_5.setObjectName(u"label_5")
        sizePolicy2.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy2)
        self.label_5.setMaximumSize(QSize(16777215, 20))
        font2 = QFont()
        font2.setPointSize(9)
        self.label_5.setFont(font2)
        self.label_5.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.label_5, 1, 0, 1, 1)


        self.horizontalLayout_8.addWidget(self.frame_5)

        self.frame_2 = QFrame(self.startpage)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy1.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy1)
        self.frame_2.setMinimumSize(QSize(0, 0))
        self.frame_2.setStyleSheet(u"")
        self.gridLayout_6 = QGridLayout(self.frame_2)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(9, 0, 9, 0)
        self.widget_2 = QWidget(self.frame_2)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy1.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy1)
        self.horizontalLayout_4 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.taskManage_2 = QToolButton(self.widget_2)
        self.taskManage_2.setObjectName(u"taskManage_2")
        sizePolicy1.setHeightForWidth(self.taskManage_2.sizePolicy().hasHeightForWidth())
        self.taskManage_2.setSizePolicy(sizePolicy1)
        self.taskManage_2.setMaximumSize(QSize(50, 16777215))
        self.taskManage_2.setStyleSheet(u"")
        icon5 = QIcon()
        icon5.addFile(u":/images/images/\u4efb\u52a1\u83b7\u53d6\u8d44\u6e90 1.png", QSize(), QIcon.Normal, QIcon.Off)
        self.taskManage_2.setIcon(icon5)
        self.taskManage_2.setIconSize(QSize(25, 25))
        self.taskManage_2.setAutoRepeat(False)
        self.taskManage_2.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.horizontalLayout_4.addWidget(self.taskManage_2)


        self.gridLayout_6.addWidget(self.widget_2, 0, 0, 1, 1)

        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(16777215, 20))
        self.label_2.setFont(font2)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.label_2, 1, 0, 1, 1)


        self.horizontalLayout_8.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.startpage)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy1.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy1)
        self.frame_3.setMinimumSize(QSize(0, 0))
        self.frame_3.setStyleSheet(u"")
        self.gridLayout_7 = QGridLayout(self.frame_3)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(9, 0, 9, 0)
        self.widget_3 = QWidget(self.frame_3)
        self.widget_3.setObjectName(u"widget_3")
        sizePolicy1.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy1)
        self.horizontalLayout_5 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_5.setSpacing(2)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.taskManage_3 = QToolButton(self.widget_3)
        self.taskManage_3.setObjectName(u"taskManage_3")
        sizePolicy1.setHeightForWidth(self.taskManage_3.sizePolicy().hasHeightForWidth())
        self.taskManage_3.setSizePolicy(sizePolicy1)
        self.taskManage_3.setMaximumSize(QSize(50, 16777215))
        self.taskManage_3.setStyleSheet(u"")
        icon6 = QIcon()
        icon6.addFile(u":/images/images/\u8bb0\u5f55.png", QSize(), QIcon.Normal, QIcon.Off)
        self.taskManage_3.setIcon(icon6)
        self.taskManage_3.setIconSize(QSize(25, 25))
        self.taskManage_3.setAutoRepeat(False)
        self.taskManage_3.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.horizontalLayout_5.addWidget(self.taskManage_3)

        self.toolButton = QToolButton(self.widget_3)
        self.toolButton.setObjectName(u"toolButton")
        sizePolicy1.setHeightForWidth(self.toolButton.sizePolicy().hasHeightForWidth())
        self.toolButton.setSizePolicy(sizePolicy1)
        icon7 = QIcon()
        icon7.addFile(u":/images/images/\u591a\u8bb0\u5f55.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton.setIcon(icon7)
        self.toolButton.setIconSize(QSize(23, 25))
        self.toolButton.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.horizontalLayout_5.addWidget(self.toolButton)


        self.gridLayout_7.addWidget(self.widget_3, 0, 0, 1, 1)

        self.label_3 = QLabel(self.frame_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(16777215, 20))
        self.label_3.setFont(font2)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.gridLayout_7.addWidget(self.label_3, 1, 0, 1, 1)


        self.horizontalLayout_8.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.startpage)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy1.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy1)
        self.frame_4.setMinimumSize(QSize(0, 0))
        self.frame_4.setStyleSheet(u"")
        self.gridLayout_8 = QGridLayout(self.frame_4)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(9, 0, 9, 0)
        self.widget_6 = QWidget(self.frame_4)
        self.widget_6.setObjectName(u"widget_6")
        sizePolicy1.setHeightForWidth(self.widget_6.sizePolicy().hasHeightForWidth())
        self.widget_6.setSizePolicy(sizePolicy1)
        self.horizontalLayout_6 = QHBoxLayout(self.widget_6)
        self.horizontalLayout_6.setSpacing(2)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.taskManage_4 = QToolButton(self.widget_6)
        self.taskManage_4.setObjectName(u"taskManage_4")
        sizePolicy1.setHeightForWidth(self.taskManage_4.sizePolicy().hasHeightForWidth())
        self.taskManage_4.setSizePolicy(sizePolicy1)
        self.taskManage_4.setMaximumSize(QSize(50, 16777215))
        self.taskManage_4.setStyleSheet(u"")
        icon8 = QIcon()
        icon8.addFile(u":/images/images/\u4e91\u7aef.png", QSize(), QIcon.Normal, QIcon.Off)
        self.taskManage_4.setIcon(icon8)
        self.taskManage_4.setIconSize(QSize(25, 25))
        self.taskManage_4.setAutoRepeat(False)
        self.taskManage_4.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.horizontalLayout_6.addWidget(self.taskManage_4)

        self.toolButton_2 = QToolButton(self.widget_6)
        self.toolButton_2.setObjectName(u"toolButton_2")
        sizePolicy1.setHeightForWidth(self.toolButton_2.sizePolicy().hasHeightForWidth())
        self.toolButton_2.setSizePolicy(sizePolicy1)
        icon9 = QIcon()
        icon9.addFile(u":/images/images/\u8bc4\u4ef7.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_2.setIcon(icon9)
        self.toolButton_2.setIconSize(QSize(25, 25))
        self.toolButton_2.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.horizontalLayout_6.addWidget(self.toolButton_2)


        self.gridLayout_8.addWidget(self.widget_6, 0, 0, 1, 1)

        self.label_4 = QLabel(self.frame_4)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(16777215, 20))
        self.label_4.setFont(font2)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.gridLayout_8.addWidget(self.label_4, 1, 0, 1, 1)


        self.horizontalLayout_8.addWidget(self.frame_4)

        self.horizontalSpacer_2 = QSpacerItem(1217, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_2)

        self.tools.addWidget(self.startpage)
        self.viewpage = QWidget()
        self.viewpage.setObjectName(u"viewpage")
        self.tools.addWidget(self.viewpage)
        self.helppage = QWidget()
        self.helppage.setObjectName(u"helppage")
        self.tools.addWidget(self.helppage)

        self.verticalLayout.addWidget(self.tools)

        self.main = QWidget(self.centralwidget)
        self.main.setObjectName(u"main")
        self.main.setStyleSheet(u"QWidget.QWidget{\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"QTabBar::tab{\n"
"	background-color: rgba(85, 170, 255, 60);\n"
"	color:#FFFFFF;\n"
"}\n"
"QTabBar::tab:selected,QTabBar::tab:hover{\n"
"	background-color: #FFFFFF;\n"
"	color:#000000;\n"
"}\n"
"QTabWidget{\n"
"border:none;\n"
"}\n"
"QTableWidget\n"
"{\n"
"	border:none;\n"
"    background:rgb(255, 255, 255);\n"
"}\n"
"QTableWidget::item\n"
"{\n"
"    color:rgb(0,0,0);\n"
"    background: #FFFFFF;\n"
"    text-align:center;\n"
"}\n"
"QTableWidget::item:hover\n"
"{\n"
"    color:#FFFFFF;\n"
"    background:  rgb(22, 78, 134);\n"
"}\n"
"QTableWidget::item:selected\n"
"{\n"
"  color:#FFFFFF;\n"
"    background:  rgb(22, 78, 134);\n"
"}\n"
"QHeaderView::section,QTableCornerButton:section\n"
"{ \n"
"    text-align:center;\n"
"    padding:3px; \n"
"    margin:0px; \n"
"    color:#FFFFFF; \n"
"    border:1px solid #242424; \n"
"    border-left-width:0px; \n"
"    border-right-width:1px; \n"
"    border-top-width:0px;\n"
"     border-bottom-width:1px"
                        "; \n"
"    background:rgb(22, 78, 134);\n"
" }\n"
"QHeaderView::section:selected\n"
"{ \n"
"    color:#FFFFFF; \n"
"    border:1px solid #FFFFFF; \n"
" }\n"
"QScrollBar:vertical{ \n"
"    width:8px;  \n"
"    border-style:flat;\n"
"    border-radius: 4px;\n"
"    border:0px;\n"
"     background:rgb(85, 255, 255);\n"
"} \n"
"QScrollBar::handle:vertical{ \n"
"    background: rgba(255,255,255,0.50);\n"
"    border-radius: 4px;\n"
"    width:8px; \n"
"    min-height:91px; \n"
"    border-style:flat;\n"
"}\n"
"QScrollBar::handle:vertical::hover{ \n"
"    background: rgba(255,255,255,0.10);\n"
"    border-radius: 4px;\n"
"    width:8px; \n"
"}\n"
"QScrollBar::handle:vertical::pressed{ \n"
"    background: rgba(255,255,255,0.10);\n"
"    border-radius:4px;\n"
"    width:8px; \n"
"}\n"
"QScrollBar::sub-page:vertical {\n"
"    background: #FFFFFF;\n"
"border-style:flat;\n"
"}\n"
"QScrollBar::add-page:vertical {\n"
"   background: #FFFFFF;\n"
"border-style:flat;\n"
"}\n"
"QScrollBar::add-line:vertical{\n"
"   background"
                        ": #FFFFFF;\n"
"}\n"
"QScrollBar::sub-line:vertical {\n"
"   background: #FFFFFF;\n"
"}\n"
"QScrollBar:horizontal{ \n"
"    height:8px;  \n"
"    border-style:flat;\n"
"    border-radius: 4px;\n"
"    border:0px;\n"
"background: rgb(85, 255, 255);\n"
"} \n"
"QScrollBar::handle:horizontal{ \n"
"    background: rgba(255,255,255,0.50);\n"
"    border-radius: 4px;\n"
"    height:8px; \n"
"    min-width:91px; \n"
"    border-style:flat;\n"
"}\n"
"QScrollBar::handle:horizontal::hover{ \n"
"    background: rgba(255,255,255,0.10);\n"
"    border-radius: 4px;\n"
"    height:8px; \n"
"}\n"
"QScrollBar::handle:horizontal::pressed{ \n"
"    background: rgba(255,255,255,0.10);\n"
"    border-radius:4px;\n"
"    height:8px; \n"
"}\n"
"QScrollBar::sub-page:horizontal {\n"
"    background: #FFFFFF;\n"
"    border-style:flat;\n"
"}\n"
"QScrollBar::add-page:horizontal {\n"
"   background: #FFFFFF;\n"
"    border-style:flat;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"   background: #FFFFFF;\n"
"}\n"
"QScrollBar::add-line:hor"
                        "izontal{\n"
"   background: #FFFFFF;\n"
"}")
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
        self.leftInfo = QTabWidget(self.mainSplitter)
        self.leftInfo.setObjectName(u"leftInfo")
        self.leftInfo.setMinimumSize(QSize(300, 0))
        self.leftInfo.setStyleSheet(u"QPushButton {\n"
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
"}")
        self.leftInfoPage = QWidget()
        self.leftInfoPage.setObjectName(u"leftInfoPage")
        self.gridLayout_2 = QGridLayout(self.leftInfoPage)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.tableWidgetFiles = FilmInfo(self.leftInfoPage)
        self.tableWidgetFiles.setObjectName(u"tableWidgetFiles")
        self.tableWidgetFiles.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidgetFiles.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidgetFiles.horizontalHeader().setStretchLastSection(True)
        self.tableWidgetFiles.verticalHeader().setVisible(False)

        self.gridLayout_2.addWidget(self.tableWidgetFiles, 2, 0, 1, 3)

        self.widget_4 = QWidget(self.leftInfoPage)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setMinimumSize(QSize(0, 100))
        self.gridLayout_9 = QGridLayout(self.widget_4)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.label_6 = QLabel(self.widget_4)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(50, 16777215))

        self.gridLayout_9.addWidget(self.label_6, 0, 0, 1, 1)

        self.taskName = QLabel(self.widget_4)
        self.taskName.setObjectName(u"taskName")

        self.gridLayout_9.addWidget(self.taskName, 0, 1, 1, 1)

        self.label_7 = QLabel(self.widget_4)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMaximumSize(QSize(50, 16777215))

        self.gridLayout_9.addWidget(self.label_7, 1, 0, 1, 1)

        self.label_8 = QLabel(self.widget_4)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMaximumSize(QSize(50, 16777215))

        self.gridLayout_9.addWidget(self.label_8, 2, 0, 1, 1)

        self.taskNum = QLabel(self.widget_4)
        self.taskNum.setObjectName(u"taskNum")

        self.gridLayout_9.addWidget(self.taskNum, 2, 1, 1, 1)

        self.label_9 = QLabel(self.widget_4)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMaximumSize(QSize(50, 16777215))

        self.gridLayout_9.addWidget(self.label_9, 3, 0, 1, 1)

        self.createTime = QLabel(self.widget_4)
        self.createTime.setObjectName(u"createTime")

        self.gridLayout_9.addWidget(self.createTime, 3, 1, 1, 1)

        self.companyName = QLabel(self.widget_4)
        self.companyName.setObjectName(u"companyName")

        self.gridLayout_9.addWidget(self.companyName, 1, 1, 1, 1)


        self.gridLayout_2.addWidget(self.widget_4, 0, 0, 1, 3)

        self.addFilm = QPushButton(self.leftInfoPage)
        self.addFilm.setObjectName(u"addFilm")

        self.gridLayout_2.addWidget(self.addFilm, 1, 0, 1, 1)

        self.delFilm = QPushButton(self.leftInfoPage)
        self.delFilm.setObjectName(u"delFilm")

        self.gridLayout_2.addWidget(self.delFilm, 1, 1, 1, 1)

        self.syncFilm = QPushButton(self.leftInfoPage)
        self.syncFilm.setObjectName(u"syncFilm")

        self.gridLayout_2.addWidget(self.syncFilm, 1, 2, 1, 1)

        self.leftInfo.addTab(self.leftInfoPage, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.leftInfo.addTab(self.tab, "")
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
        self.tabWidget_5 = QTabWidget(self.imageSplitter)
        self.tabWidget_5.setObjectName(u"tabWidget_5")
        self.tabWidget_5.setMinimumSize(QSize(0, 400))
        self.tabWidget_5Page1 = QWidget()
        self.tabWidget_5Page1.setObjectName(u"tabWidget_5Page1")
        self.gridLayout_3 = QGridLayout(self.tabWidget_5Page1)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.image = ImageViewer(self.tabWidget_5Page1)
        self.image.setObjectName(u"image")
        self.image.setStyleSheet(u"border:none;")

        self.gridLayout_3.addWidget(self.image, 0, 0, 1, 1)

        self.tabWidget_5.addTab(self.tabWidget_5Page1, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tabWidget_5.addTab(self.tab_2, "")
        self.imageSplitter.addWidget(self.tabWidget_5)

        self.verticalLayout_2.addWidget(self.imageSplitter)

        self.mainSplitter.addWidget(self.imageInfo)

        self.horizontalLayout_2.addWidget(self.mainSplitter)


        self.verticalLayout.addWidget(self.main)

        self.statusbar = QWidget(self.centralwidget)
        self.statusbar.setObjectName(u"statusbar")
        self.statusbar.setMinimumSize(QSize(0, 20))
        self.statusbar.setMaximumSize(QSize(16777215, 20))
        self.statusbar.setStyleSheet(u"QWidget{\n"
"background-color:#164E86;\n"
"}")

        self.verticalLayout.addWidget(self.statusbar)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.leftInfo.setCurrentIndex(0)
        self.tabWidget_5.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u8ba1\u7b97\u673a\u8f85\u52a9\u8bc4\u7247\u7cfb\u7edf", None))
        self.startbutton.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb", None))
        self.viewbutton.setText(QCoreApplication.translate("MainWindow", u"\u89c6\u56fe", None))
        self.helpbutton.setText(QCoreApplication.translate("MainWindow", u"\u5e2e\u52a9", None))
        self.taskManage.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00\u4efb\u52a1", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u4efb\u52a1\u7ba1\u7406", None))
        self.taskManage_5.setText(QCoreApplication.translate("MainWindow", u"\u4f2a\u5f69\u8272\u53d8\u6362", None))
        self.toolButton_3.setText(QCoreApplication.translate("MainWindow", u"\u4eae\u5ea6\u8c03\u8282", None))
        self.toolButton_4.setText(QCoreApplication.translate("MainWindow", u"\u7070\u5ea6\u503c\u8c03\u8282", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u56fe\u50cf\u5904\u7406", None))
        self.taskManage_2.setText(QCoreApplication.translate("MainWindow", u"\u591a\u6e90\u878d\u5408", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u7efc\u5408\u8bc4\u4ef7", None))
        self.taskManage_3.setText(QCoreApplication.translate("MainWindow", u"\u5355\u5f20\u8bb0\u5f55", None))
        self.toolButton.setText(QCoreApplication.translate("MainWindow", u"\u591a\u5f20\u8bb0\u5f55", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u8bb0\u5f55\u751f\u6210", None))
        self.taskManage_4.setText(QCoreApplication.translate("MainWindow", u"\u4e91\u7aef\u914d\u7f6e", None))
        self.toolButton_2.setText(QCoreApplication.translate("MainWindow", u"\u8bc4\u5b9a\u914d\u7f6e", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u7cfb\u7edf\u914d\u7f6e", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u4efb\u52a1\u540d\u79f0", None))
        self.taskName.setText("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u5355\u4f4d\u540d\u79f0", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u4efb\u52a1\u7f16\u53f7", None))
        self.taskNum.setText("")
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u521b\u5efa\u65e5\u671f", None))
        self.createTime.setText("")
        self.companyName.setText("")
        self.addFilm.setText(QCoreApplication.translate("MainWindow", u"\u6dfb\u52a0\u5e95\u7247", None))
        self.delFilm.setText(QCoreApplication.translate("MainWindow", u"\u5220\u9664\u5e95\u7247", None))
        self.syncFilm.setText(QCoreApplication.translate("MainWindow", u"\u540c\u6b65\u5e95\u7247", None))
        self.leftInfo.setTabText(self.leftInfo.indexOf(self.leftInfoPage), QCoreApplication.translate("MainWindow", u"\u5e95\u7247\u4fe1\u606f", None))
        self.leftInfo.setTabText(self.leftInfo.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"\u8bc4\u4ef7\u4fe1\u606f", None))
        self.tabWidget_5.setTabText(self.tabWidget_5.indexOf(self.tabWidget_5Page1), QCoreApplication.translate("MainWindow", u"\u56fe\u50cf\u754c\u9762", None))
        self.tabWidget_5.setTabText(self.tabWidget_5.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"\u7b80\u56fe\u754c\u9762", None))
    # retranslateUi

