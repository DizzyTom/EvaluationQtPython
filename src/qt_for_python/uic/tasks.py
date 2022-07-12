# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tasks.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractSpinBox, QApplication, QCheckBox,
    QDateTimeEdit, QDialog, QGridLayout, QHeaderView,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QTableWidget, QTableWidgetItem, QWidget)
import resource_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(591, 549)
        icon = QIcon()
        icon.addFile(u":/images/images/\u8ba1\u7b97\u673a.png", QSize(), QIcon.Normal, QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setStyleSheet(u"#Dialog{\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton {\n"
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
"}\n"
".QDateTimeEdit\n"
"{\n"
"    min-height:24px;\n"
"    max-height:24px;\n"
"    border-radius:2px;\n"
"    border:1px solid #cccccc;\n"
"}\n"
"\n"
".QDateTimeEdit:hover,.QDateTimeEdit:focus\n"
"{\n"
"    border-radius:2px;\n"
"    border:1px solid #0f6dbe;\n"
"}\n"
"\n"
".QDateTimeEdit::dro"
                        "p-down\n"
"{\n"
"    border:none;\n"
"    width:20px;\n"
"	\n"
"}\n"
".QDateTimeEdit::down-arrow {\n"
"    border-image:url(:/images/images/DownArrow.png);\n"
"}\n"
"\n"
"\n"
"")
        self.gridLayout_5 = QGridLayout(Dialog)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.conditionWidget = QWidget(Dialog)
        self.conditionWidget.setObjectName(u"conditionWidget")
        self.gridLayout = QGridLayout(self.conditionWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.conditionWidget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_4 = QLabel(self.conditionWidget)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)

        self.companyInput = QLineEdit(self.conditionWidget)
        self.companyInput.setObjectName(u"companyInput")

        self.gridLayout.addWidget(self.companyInput, 1, 1, 1, 1)

        self.label_5 = QLabel(self.conditionWidget)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)

        self.taskNameInput = QLineEdit(self.conditionWidget)
        self.taskNameInput.setObjectName(u"taskNameInput")

        self.gridLayout.addWidget(self.taskNameInput, 2, 1, 1, 1)

        self.label_6 = QLabel(self.conditionWidget)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 3, 0, 1, 1)

        self.taskNumInfo = QLineEdit(self.conditionWidget)
        self.taskNumInfo.setObjectName(u"taskNumInfo")

        self.gridLayout.addWidget(self.taskNumInfo, 3, 1, 1, 1)


        self.gridLayout_5.addWidget(self.conditionWidget, 2, 0, 1, 1)

        self.setWidget = QWidget(Dialog)
        self.setWidget.setObjectName(u"setWidget")
        self.gridLayout_2 = QGridLayout(self.setWidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_2 = QLabel(self.setWidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)

        self.blurCheckBox = QCheckBox(self.setWidget)
        self.blurCheckBox.setObjectName(u"blurCheckBox")

        self.gridLayout_2.addWidget(self.blurCheckBox, 1, 0, 1, 1)

        self.timeCheckBox = QCheckBox(self.setWidget)
        self.timeCheckBox.setObjectName(u"timeCheckBox")

        self.gridLayout_2.addWidget(self.timeCheckBox, 2, 0, 1, 1)


        self.gridLayout_5.addWidget(self.setWidget, 2, 1, 1, 1)

        self.timeRangeWidget = QWidget(Dialog)
        self.timeRangeWidget.setObjectName(u"timeRangeWidget")
        self.gridLayout_3 = QGridLayout(self.timeRangeWidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_3 = QLabel(self.timeRangeWidget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_3.addWidget(self.label_3, 0, 0, 1, 2)

        self.label_7 = QLabel(self.timeRangeWidget)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_3.addWidget(self.label_7, 1, 0, 1, 1)

        self.startTimeEdit = QDateTimeEdit(self.timeRangeWidget)
        self.startTimeEdit.setObjectName(u"startTimeEdit")
        self.startTimeEdit.setButtonSymbols(QAbstractSpinBox.UpDownArrows)
        self.startTimeEdit.setDateTime(QDateTime(QDate(2020, 1, 1), QTime(0, 0, 0)))
        self.startTimeEdit.setDate(QDate(2020, 1, 1))
        self.startTimeEdit.setCalendarPopup(True)

        self.gridLayout_3.addWidget(self.startTimeEdit, 1, 1, 1, 1)

        self.label_8 = QLabel(self.timeRangeWidget)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_3.addWidget(self.label_8, 2, 0, 1, 1)

        self.endTimeEdit = QDateTimeEdit(self.timeRangeWidget)
        self.endTimeEdit.setObjectName(u"endTimeEdit")
        self.endTimeEdit.setButtonSymbols(QAbstractSpinBox.UpDownArrows)
        self.endTimeEdit.setDateTime(QDateTime(QDate(2020, 1, 1), QTime(0, 0, 0)))
        self.endTimeEdit.setCalendarPopup(True)

        self.gridLayout_3.addWidget(self.endTimeEdit, 2, 1, 1, 1)


        self.gridLayout_5.addWidget(self.timeRangeWidget, 2, 2, 1, 1)

        self.tableWidget = QTableWidget(Dialog)
        if (self.tableWidget.columnCount() < 10):
            self.tableWidget.setColumnCount(10)
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
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        if (self.tableWidget.rowCount() < 14):
            self.tableWidget.setRowCount(14)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(10, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(11, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(12, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(13, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.tableWidget.setItem(0, 0, __qtablewidgetitem24)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setStyleSheet(u"QTableWidget\n"
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
"     border-bottom-width:1px; \n"
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
"     background:rgb(85, "
                        "255, 255);\n"
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
"   background: #FFFFFF;\n"
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
"    backgr"
                        "ound: rgba(255,255,255,0.50);\n"
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
"QScrollBar::add-line:horizontal{\n"
"   background: #FFFFFF;\n"
"}")
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)

        self.gridLayout_5.addWidget(self.tableWidget, 0, 0, 1, 3)

        self.widget = QWidget(Dialog)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"")
        self.gridLayout_4 = QGridLayout(self.widget)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.addTask = QPushButton(self.widget)
        self.addTask.setObjectName(u"addTask")
        self.addTask.setFocusPolicy(Qt.NoFocus)

        self.gridLayout_4.addWidget(self.addTask, 0, 0, 1, 1)

        self.deleteTask = QPushButton(self.widget)
        self.deleteTask.setObjectName(u"deleteTask")
        self.deleteTask.setFocusPolicy(Qt.NoFocus)

        self.gridLayout_4.addWidget(self.deleteTask, 0, 1, 1, 1)

        self.modifyTask = QPushButton(self.widget)
        self.modifyTask.setObjectName(u"modifyTask")
        self.modifyTask.setFocusPolicy(Qt.NoFocus)

        self.gridLayout_4.addWidget(self.modifyTask, 0, 2, 1, 1)

        self.searchTask = QPushButton(self.widget)
        self.searchTask.setObjectName(u"searchTask")
        self.searchTask.setFocusPolicy(Qt.NoFocus)

        self.gridLayout_4.addWidget(self.searchTask, 0, 3, 1, 1)


        self.gridLayout_5.addWidget(self.widget, 1, 0, 1, 3)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u4efb\u52a1\u7ba1\u7406", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u67e5\u8be2\u6761\u4ef6", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"\u5355\u4f4d\u540d\u79f0", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"\u4efb\u52a1\u540d\u79f0", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"\u4efb\u52a1\u7f16\u53f7", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u67e5\u8be2\u8bbe\u7f6e", None))
        self.blurCheckBox.setText(QCoreApplication.translate("Dialog", u"\u6a21\u7cca\u67e5\u8be2", None))
        self.timeCheckBox.setText(QCoreApplication.translate("Dialog", u"\u65e0\u65f6\u95f4\u6761\u4ef6\u9650\u5236", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"\u67e5\u8be2\u65f6\u95f4\u8303\u56f4", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"\u8d77\u59cb\u65f6\u95f4", None))
        self.label_8.setText(QCoreApplication.translate("Dialog", u"\u7ec8\u6b62\u65f6\u95f4", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Dialog", u"\u65b0\u5efa\u5217", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Dialog", u"\u65b0\u5efa\u5217", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Dialog", u"\u65b0\u5efa\u5217", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Dialog", u"\u65b0\u5efa\u5217", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Dialog", u"\u65b0\u5efa\u5217", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Dialog", u"\u65b0\u5efa\u5217", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Dialog", u"\u65b0\u5efa\u5217", None));
        ___qtablewidgetitem7 = self.tableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Dialog", u"\u65b0\u5efa\u5217", None));
        ___qtablewidgetitem8 = self.tableWidget.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("Dialog", u"\u65b0\u5efa\u5217", None));
        ___qtablewidgetitem9 = self.tableWidget.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("Dialog", u"\u65b0\u5efa\u5217", None));
        ___qtablewidgetitem10 = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("Dialog", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem11 = self.tableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("Dialog", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem12 = self.tableWidget.verticalHeaderItem(2)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("Dialog", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem13 = self.tableWidget.verticalHeaderItem(3)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("Dialog", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem14 = self.tableWidget.verticalHeaderItem(4)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("Dialog", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem15 = self.tableWidget.verticalHeaderItem(5)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("Dialog", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem16 = self.tableWidget.verticalHeaderItem(6)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("Dialog", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem17 = self.tableWidget.verticalHeaderItem(7)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("Dialog", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem18 = self.tableWidget.verticalHeaderItem(8)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("Dialog", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem19 = self.tableWidget.verticalHeaderItem(9)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("Dialog", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem20 = self.tableWidget.verticalHeaderItem(10)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("Dialog", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem21 = self.tableWidget.verticalHeaderItem(11)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("Dialog", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem22 = self.tableWidget.verticalHeaderItem(12)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("Dialog", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem23 = self.tableWidget.verticalHeaderItem(13)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("Dialog", u"\u65b0\u5efa\u884c", None));

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        ___qtablewidgetitem24 = self.tableWidget.item(0, 0)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("Dialog", u"ceshi ", None));
        self.tableWidget.setSortingEnabled(__sortingEnabled)

        self.addTask.setText(QCoreApplication.translate("Dialog", u"\u6dfb\u52a0\u4efb\u52a1", None))
        self.deleteTask.setText(QCoreApplication.translate("Dialog", u"\u5220\u9664\u4efb\u52a1", None))
        self.modifyTask.setText(QCoreApplication.translate("Dialog", u"\u4fee\u6539\u4efb\u52a1", None))
        self.searchTask.setText(QCoreApplication.translate("Dialog", u"\u67e5\u8be2\u4efb\u52a1", None))
    # retranslateUi

