from PySide6.QtWidgets import QDialog, QTableWidgetItem,QLineEdit,QPushButton
from PySide6.QtCore import QDateTime,Signal
from qt_for_python.uic.tasks import Ui_Dialog as Main_Dialog
from qt_for_python.uic.addTask import Ui_Dialog as Sub_Dialog
import requests
import datetime

from utils.utils_qt.utils_qt import MyMessageBox
from .utils import webConnect,Const


class AddTaskDialog(QDialog):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.ui=Sub_Dialog()
        self.ui.setupUi(self)
        self.ui.yesBtn.clicked.connect(self.addTask)
        self.ui.companyName.textChanged.connect(self.checkEdit)
        self.ui.taskName.textChanged.connect(self.checkEdit)
        self.ui.taskNum.textChanged.connect(self.checkEdit)

    def checkEdit(self):
        obj:QLineEdit=self.sender()
        if obj.text()=='':
            obj.setStyleSheet("QLineEdit{border:1px solid red }")
        else:
            obj.setStyleSheet("QLineEdit{border:1px solid gray border-radius:1px}")

    def addTask(self):
        companyName=self.ui.companyName.text()
        taskName=self.ui.taskName.text()
        taskNum=self.ui.taskNum.text()
        createTime=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        data={
            'qyname':companyName.encode("GBK"),
            'taskname':taskName.encode("GBK"),
            'tasknum':taskNum.encode("GBK"),
            'note':self.ui.note.text().encode("GBK"),
            'createtime':createTime.encode("GBK")

        }
        if len(companyName) and len(taskName) and len(taskNum):
            ret=requests.post(webConnect.getUrl(Const.addTask_url),data=data).json()
            if ret['ret']==1:
                self.accept()
            else:
                box=MyMessageBox(self)
                box.setIcon(MyMessageBox.Warning)
                box.setWindowTitle("错误")
                box.setText(ret["msg"])
                box.exec()
                self.reject()
        else:
            box=MyMessageBox(self)
            box.setIcon(MyMessageBox.Warning)
            box.setWindowTitle("提示")
            box.setText("信息未完整填充")
            box.exec()
class ModifyTaskDialog(QDialog):
    def __init__(self,id:int,parent=None):
        super().__init__(parent)
        self.ui=Sub_Dialog()
        self.ui.setupUi(self)
        self.setWindowTitle("修改任务")
        ret=requests.post(webConnect.getUrl(Const.getTaskInfo_url),data={"id":id}).json()
        res=ret["res"]
        self.id=id
        self.ui.companyName.setText(res.get("QYNAME",None))
        self.ui.taskName.setText(res.get("TASKNAME",None))
        self.ui.taskNum.setText(res.get("TASKNUM",None))
        self.ui.yesBtn.clicked.connect(self.accept)
        self.ui.companyName.textChanged.connect(self.checkEdit)
        self.ui.taskName.textChanged.connect(self.checkEdit)
        self.ui.taskNum.textChanged.connect(self.checkEdit)
    def checkEdit(self):
        obj:QLineEdit=self.sender()
        if obj.text()=='':
            obj.setStyleSheet("QLineEdit{border:1px solid red }")
        else:
            obj.setStyleSheet("QLineEdit{border:1px solid gray border-radius:1px}")
    def accept(self):
        data={
            'id':self.id,
            'qyname':self.ui.companyName.text().encode("GBK"),
            'taskname':self.ui.taskName.text().encode("GBK"),
            'tasknum':self.ui.taskNum.text().encode("GBK"),
            'note':self.ui.note.text().encode("GBK")
        }
        # print(data)
        requests.post(webConnect.getUrl(Const.changeTask_url),data=data)
        return super().accept()
class TasksWindow(QDialog):
    sendSignal=Signal(str,str,str)
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Main_Dialog()
        self.ui.setupUi(self)
        self.ui.timeCheckBox.toggled.connect(self.timeRangeEnable)
        self.ui.timeCheckBox.setChecked(True)
        self.ui.blurCheckBox.setChecked(True)
        self.ui.endTimeEdit.setDateTime(QDateTime.currentDateTime())

        self.addHeader()
        self.freshContent()
        
        self.ui.addTask.clicked.connect(self.inputTask)
        self.ui.deleteTask.clicked.connect(self.deleteTask)
        self.ui.modifyTask.clicked.connect(self.changeTask)
        self.ui.searchTask.clicked.connect(self.freshContent)
        self.ui.tableWidget.doubleClicked.connect(self.accept)
        self.ui.tableWidget.doubleClicked.connect(self.sendInfo)

        

    def addHeader(self):
        self.tableHeader = [
            None,
            "QYNAME",
            "TASKNAME",
            "TASKNUM",
            "FILMNUM",
            "TASKSTATE",
            "CREATETIME",
            "NOTE",
            "id",
        ]
        self.tableHeaderName = [
            "序号",
            "单位名称",
            "任务名称",
            "任务编号",
            "底片数量",
            "任务状态",
            "创建时间",
            "备注",
            "id",
        ]
        self.ui.tableWidget.setColumnCount(len(self.tableHeaderName))
        self.ui.tableWidget.setHorizontalHeaderLabels(self.tableHeaderName)
        self.ui.tableWidget.setColumnHidden(self.tableHeader.index("id"),True)

    def freshContent(self):
        # self.ui.tableWidget.clearContents()
        self.ui.tableWidget.setRowCount(0)
        # print(webConnect.getUrl(Const.taskManage))
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
            starttime: datetime.datetime = self.ui.startTimeEdit.dateTime().toPython()
            endtime = self.ui.endTimeEdit.dateTime().toPython()
            data.setdefault("starttime", starttime.strftime("%Y-%m-%d %H:%M:%S"))
            data.setdefault("endtime", endtime.strftime("%Y-%m-%d %H:%M:%S"))
        ret = requests.post(
            webConnect.getUrl(Const.searchTask_url), data=data
        ).json()
        if ret["ret"] == 1:
            result = ret.get("res", None)
            if result is not None:
                for result_row in result:
                    rowCount = self.ui.tableWidget.rowCount()
                    self.ui.tableWidget.setRowCount(rowCount + 1)
                    for i, tableHeader in enumerate(self.tableHeader):
                        colVal=result_row.get(tableHeader)
                        if colVal is None:
                            colVal=''
                        if tableHeader is None:
                            self.ui.tableWidget.setItem(
                                rowCount, i, QTableWidgetItem(str(rowCount + 1))
                            )
                        else:
                            self.ui.tableWidget.setItem(
                                rowCount,
                                i,
                                QTableWidgetItem(str(colVal)),
                            )
        self.ui.tableWidget.resizeColumnsToContents()
        self.ui.tableWidget.resizeRowsToContents()

    def timeRangeEnable(self, state):
        if state:
            self.ui.timeRangeWidget.setEnabled(False)
        else:
            self.ui.timeRangeWidget.setEnabled(True)

    def inputTask(self):
        dlg = AddTaskDialog(self)
        dlg.accepted.connect(self.freshContent)
        dlg.exec()

    def deleteTask(self):
        box=MyMessageBox(self)
        box.setIcon(MyMessageBox.Question)
        box.setWindowTitle('提问')
        box.setText('是否删除')
        okbtn=QPushButton('是')
        nobtn=QPushButton('否')
        box.addButton(okbtn,MyMessageBox.AcceptRole)
        box.addButton(nobtn,MyMessageBox.RejectRole)
        box.exec()
        if box.clickedButton()!=okbtn:
            return

        contents = self.ui.tableWidget.selectedItems()
        rowList = []
        for item in contents:
            if item.row() in rowList:
                continue
            rowList.append(item.row())
        rowList = sorted(
            rowList,
            key=lambda x: int(
                self.ui.tableWidget.item(x, self.tableHeader.index(None)).text()
            ),
            reverse=True,
        )
        for row in rowList:
            _id = self.ui.tableWidget.item(row, self.tableHeader.index("id")).text()
            ret = requests.post(
                webConnect.getUrl(Const.deleteTask_url), data={"id": _id}
            ).json()
            if ret["ret"] == 1:
                self.ui.tableWidget.removeRow(row)

        self.freshContent()

    def changeTask(self):
        contents = self.ui.tableWidget.selectedItems()
        rowList = []
        for item in contents:
            if item.row() in rowList:
                continue
            rowList.append(item.row())
        if len(rowList) != 1:
            box=MyMessageBox(self)
            box.setIcon(MyMessageBox.Warning)
            box.setWindowTitle('提示')
            box.setText("请选择一行数据修改")
            box.exec()
            return
        data = {}
        row = rowList[0]
        _id = self.ui.tableWidget.item(row, self.tableHeader.index("id")).text()
        dlg = ModifyTaskDialog(parent=self,id=int(_id))
        dlg.accepted.connect(self.freshContent)
        dlg.exec()
        # requests.post(webConnect.getUrl(Const.changeTask),data=data).json()
    
    def sendInfo(self):
        row=self.ui.tableWidget.currentRow()
        _id=self.ui.tableWidget.item(row,self.tableHeader.index('id')).text()
        _taskname=self.ui.tableWidget.item(row,self.tableHeader.index('TASKNAME')).text()
        _qyname=self.ui.tableWidget.item(row,self.tableHeader.index('QYNAME')).text()
        self.sendSignal.emit(_id,_taskname,_qyname)

