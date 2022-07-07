from qt_for_python.uic.addTask import Ui_Dialog
from PySide6.QtWidgets import QDialog,QMessageBox,QLineEdit
from utils import webConnect,ClientRequests
import requests
import datetime
class AddTaskDialog(QDialog):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.ui=Ui_Dialog()
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
            ret=requests.post(webConnect.getUrl(ClientRequests.addTask),data=data).json()
            if ret['ret']==1:
                self.accept()
            else:
                QMessageBox.warning(self,"错误",ret["msg"])
                self.reject()
        else:
            QMessageBox.warning(self,"提示","信息未完整填充")