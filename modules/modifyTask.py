from PySide6.QtWidgets import QDialog,QLineEdit
from qt_for_python.uic.addTask import Ui_Dialog
import requests
from utils import webConnect,ClientRequests

class ModifyTaskDialog(QDialog):
    def __init__(self,id:int,parent=None):
        super().__init__(parent)
        self.ui=Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowTitle("修改任务")
        ret=requests.post(webConnect.getUrl(ClientRequests.getTaskInfo),data={"id":id}).json()
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
        requests.post(webConnect.getUrl(ClientRequests.changeTask),data=data)
        return super().accept()