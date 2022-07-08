from PySide6.QtWidgets import (
    QMainWindow, QMenu, QFileDialog, QTableWidgetItem, QMessageBox, QGraphicsPixmapItem,QGraphicsScene)
from PySide6.QtCore import QModelIndex,QDateTime
from PySide6.QtGui import QPixmap
from qt_for_python.uic.main import Ui_MainWindow
from utils import getFilesWithSubffix,tiff_force_8bit,webConnect,ClientRequests
import os
from PIL import Image
import requests
from .addTask import AddTaskDialog
from .modifyTask import ModifyTaskDialog

# Main Window Class


class MainWindow(QMainWindow):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setMenu()
        self.setTableWidgetFiles()
        self.setDatabaseTasks()
    # Operations for menu
    def setMenu(self):
        self.ui.mainArea.setCurrentIndex(0)
        self.setActions()
        # File Menu
        self.menuFile = QMenu()
        self.menuFile.addActions([
            self.ui.actionOpen,
            self.ui.actionOpenDatabase
        ])
        self.menuFile.addSeparator()
        self.menuFile.addActions([
            self.ui.actionPrintPreview,
            self.ui.actionPrintConfig
        ])
        self.menuFile.setFixedWidth(140)
        self.menuFile.setFixedHeight(200)
        with open('res/qss/menu.qss', 'r', encoding='utf-8') as f:
            style = f.read()
        self.menuFile.setStyleSheet(style)
        self.ui.pushButtonFile.setMenu(self.menuFile)
        # Config Menu
        self.menuConfig = QMenu()
        self.menuConfig.addActions([
            self.ui.actionCloudConnect
        ])
        self.menuConfig.setFixedWidth(140)
        self.menuConfig.setFixedHeight(200)
        self.menuConfig.setStyleSheet(style)
        self.ui.pushButtonConfig.setMenu(self.menuConfig)

    def setActions(self):
        self.ui.actionOpen.triggered.connect(lambda:self.openFiles())

    def openFiles(self,files=None):
        if files is None:
            directory = QFileDialog.getExistingDirectory(self, "选取文件夹", "./")
            if not os.path.exists(directory):
                return
            files = getFilesWithSubffix(directory, ['.png','.jpg','.mim','.bmp'])
        self.ui.tableWidgetFiles.clearContents()
        self.ui.tableWidgetFiles.setRowCount(len(files))
        for i in range(len(files)):
            path = files[i]
            self.ui.tableWidgetFiles.setItem(
                i, 0, QTableWidgetItem('.'.join(os.path.basename(path).split('.')[:-1])))
            self.ui.tableWidgetFiles.setItem(i, 1, QTableWidgetItem(path))
        self.ui.tableWidgetFiles.resizeColumnsToContents()
        self.ui.tableWidgetFiles.resizeRowsToContents()

    def setTableWidgetFiles(self):
        with open('res/qss/verticalScroll.qss', 'r') as f:
            vScrollStyle = f.read()
        self.ui.tableWidgetFiles.verticalScrollBar().setStyleSheet(vScrollStyle)
        with open('res/qss/horizontalScroll.qss', 'r') as f:
            hScrollStyle = f.read()
        self.ui.tableWidgetFiles.horizontalScrollBar().setStyleSheet(hScrollStyle)
        self.ui.tableWidgetFiles.resizeColumnsToContents()
        self.ui.tableWidgetFiles.resizeRowsToContents()
        self.ui.tableWidgetFiles.doubleClicked.connect(
            self.tableWidgetFilesDoubleClick)

    def tableWidgetFilesDoubleClick(self, index: QModelIndex):
        row = index.row()
        path = self.ui.tableWidgetFiles.item(row, 1).text()
        if not os.path.exists(path):
            QMessageBox(QMessageBox.Critical, '错误', '文件不存在').exec()
            return
        image=tiff_force_8bit(Image.open(path))
        self.ui.statePathNow.setText(path)
        self.ui.graphicsView.setImage(image)
    # Operations for Database
    def setDatabaseTasks(self):
        self.ui.timeCheckBox.toggled.connect(self.timeRangeEnable)
        self.ui.timeCheckBox.setChecked(True)
        self.ui.blurCheckBox.setChecked(True)
        self.ui.endTimeEdit.setDateTime(QDateTime.currentDateTime())
        
        self.addHeaderTasks()
        self.freshContentTasks()

        self.ui.addTask.clicked.connect(self.inputTask)
        self.ui.deleteTask.clicked.connect(self.deleteTask)
        self.ui.modifyTask.clicked.connect(self.changeTask)
        self.ui.searchTask.clicked.connect(self.freshContentTasks)

        self.ui.tableWidgetTasks.doubleClicked.connect(self.freshTaskInfo)

    def freshTaskInfo(self):
        task_row = self.ui.tableWidgetTasks.currentRow()
        _id = int(
            self.ui.tableWidgetTasks.item(
                task_row, self.tableHeaderTasks.index("id")
            ).text()
        )
        ret = requests.post(
            webConnect.getUrl(ClientRequests.searchFilms), data={"id": _id}
        ).json()
        if ret["ret"] == 1:
            self.ui.tableWidgetFilms.setRowCount(0)
            filePaths=[]
            for row in ret["res"]:
                # print(row)
                self.ui.tableWidgetFilms.setRowCount(self.ui.tableWidgetFilms.rowCount() + 1)
                for i, colName in enumerate(self.tableHeaderFilms):
                    # print(colName)
                    if colName is  None:
                        self.ui.tableWidgetFilms.setItem(
                            self.ui.tableWidgetFilms.rowCount() - 1,
                            i,
                            QTableWidgetItem(str(self.ui.tableWidgetFilms.rowCount())),
                        )
                    else:
                        cntt=row.get(colName, None)
                        cntt='' if cntt is None else str(cntt)
                        if colName=="FILMLJ":
                            filePaths.append(cntt)
                        self.ui.tableWidgetFilms.setItem(
                            self.ui.tableWidgetFilms.rowCount() - 1,
                            i,
                            QTableWidgetItem(cntt),
                        )
            self.ui.tableWidgetFilms.resizeColumnsToContents()
            self.ui.tableWidgetFilms.resizeRowsToContents()
            self.openFiles(files=filePaths)

    def addHeaderTasks(self):
        ret=requests.post(
            webConnect.getUrl(ClientRequests.getTaskTableHeaderNames)
        ).json()
        self.tableHeaderTasks = [None]
        self.tableHeaderTasksName = ['序号']
        if ret['ret']==1:
            for ans in ret['res']:
                self.tableHeaderTasks.append(ans[0])
                self.tableHeaderTasksName.append(ans[1])      
        
        self.ui.tableWidgetTasks.setColumnCount(len(self.tableHeaderTasks))
        self.ui.tableWidgetTasks.setHorizontalHeaderLabels(self.tableHeaderTasksName)
        # self.ui.tableWidgetTasks.setColumnHidden(self.tableHeaderTasks.index("id"),True)
        ret=requests.post(
            webConnect.getUrl(ClientRequests.getFilmTableHeaderNames)
        ).json()
        self.tableHeaderFilms = [None]
        self.tableHeaderFilmsName=['序号']
        if ret['ret']==1:
            for ans in ret['res']:
                self.tableHeaderFilms.append(ans[0])
                self.tableHeaderFilmsName.append(ans[1]) 
        self.ui.tableWidgetFilms.setColumnCount(len(self.tableHeaderFilms))
        self.ui.tableWidgetFilms.setHorizontalHeaderLabels(self.tableHeaderFilmsName)

    def freshContentTasks(self):
        # self.ui.tableWidgetTasks.clearContents()
        self.ui.tableWidgetTasks.setRowCount(0)
        # print(webConnect.getUrl(ClientRequests.taskManage))
        data = {}
        companyInput = self.ui.companyInput.text()
        if len(companyInput):
            data.setdefault("qyname", companyInput.encode("GBK"))
        taskNameInput = self.ui.taskNameInput.text()
        if len(taskNameInput):
            data.setdefault("taskname", taskNameInput.encode("GBK"))
        taskNumInput = self.ui.taskNumInfo.text()
        if len(taskNameInput):
            data.setdefault("tasknum", taskNumInput.encode("GBK"))
        if self.ui.blurCheckBox.isChecked():
            data.setdefault("BlurQuery", True)
        if self.ui.timeCheckBox.isChecked():
            data.setdefault("QueryAll", True)
        else:
            starttime = self.ui.startTimeEdit.dateTime().toPython()
            endtime = self.ui.endTimeEdit.dateTime().toPython()
            data.setdefault("starttime", starttime.strftime("%Y-%m-%d %H:%M:%S"))
            data.setdefault("endtime", endtime.strftime("%Y-%m-%d %H:%M:%S"))
        ret = requests.post(
            webConnect.getUrl(ClientRequests.searchTask), data=data
        ).json()
        if ret["ret"] == 1:
            result = ret.get("res", None)
            if result is not None:
                for result_row in result:
                    rowCount = self.ui.tableWidgetTasks.rowCount()
                    self.ui.tableWidgetTasks.setRowCount(rowCount + 1)
                    for i, tableHeader in enumerate(self.tableHeaderTasks):
                        colVal=result_row.get(tableHeader)
                        if colVal is None:
                            colVal=''
                        if tableHeader is None:
                            self.ui.tableWidgetTasks.setItem(
                                rowCount, i, QTableWidgetItem(str(rowCount + 1))
                            )
                        else:
                            self.ui.tableWidgetTasks.setItem(
                                rowCount,
                                i,
                                QTableWidgetItem(str(colVal)),
                            )
        self.ui.tableWidgetTasks.resizeColumnsToContents()
        self.ui.tableWidgetTasks.resizeRowsToContents()

    def timeRangeEnable(self, state):
        if state:
            self.ui.timeRangeWidget.setEnabled(False)
        else:
            self.ui.timeRangeWidget.setEnabled(True)

    def inputTask(self):
        dlg = AddTaskDialog()
        dlg.accepted.connect(self.freshContentTasks)
        dlg.exec()

    def deleteTask(self):
        contents = self.ui.tableWidgetTasks.selectedItems()
        rowList = []
        for item in contents:
            if item.row() in rowList:
                continue
            rowList.append(item.row())
        rowList = sorted(
            rowList,
            key=lambda x: int(
                self.ui.tableWidgetTasks.item(x, self.tableHeaderTasks.index(None)).text()
            ),
            reverse=True,
        )
        for row in rowList:
            _id = self.ui.tableWidgetTasks.item(row, self.tableHeaderTasks.index("id")).text()
            ret = requests.post(
                webConnect.getUrl(ClientRequests.deleteTask), data={"id": _id}
            ).json()
            if ret["ret"] == 1:
                self.ui.tableWidgetTasks.removeRow(row)

        self.freshContentTasks()

    def changeTask(self):
        contents = self.ui.tableWidgetTasks.selectedItems()
        rowList = []
        for item in contents:
            if item.row() in rowList:
                continue
            rowList.append(item.row())
        if len(rowList) != 1:
            QMessageBox.warning(self, "提示", "请选择一行数据修改")
            return
        
        row = rowList[0]
        _id = self.ui.tableWidgetTasks.item(row, self.tableHeaderTasks.index("id")).text()
        dlg = ModifyTaskDialog(id=int(_id))
        dlg.accepted.connect(self.freshContentTasks)
        dlg.exec()
        # requests.post(webConnect.getUrl(ClientRequests.changeTask),data=data).json()