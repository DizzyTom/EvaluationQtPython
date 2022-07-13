from PySide6.QtWidgets import QMainWindow
from qt_for_python.uic.main import Ui_MainWindow
from utils.utils_qt.utils_qt import MyMessageBox
from .tasks import TasksWindow
from .utils import tiff_force_8bit
from PIL import Image
import os

class MainWindow(QMainWindow):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.setMenu()
        self.setSubWindows()
        
        
    def setMenu(self):
        self.ui.imageSplitter.setStretchFactor(1,1)
        self.ui.mainSplitter.setStretchFactor(1,1)
        self.menuList=[
            self.ui.startbutton,
            self.ui.viewbutton,
            self.ui.helpbutton,
        ]
        self.ui.startbutton.clicked.connect(lambda:self.ui.tools.setCurrentWidget(self.ui.startpage))
        self.ui.viewbutton.clicked.connect(lambda:self.ui.tools.setCurrentWidget(self.ui.viewpage))
        self.ui.helpbutton.clicked.connect(lambda:self.ui.tools.setCurrentWidget(self.ui.helppage))
        for bt in self.menuList:
            bt.clicked.connect(self.resetMenu)
        self.ui.startbutton.click()

    def setSubWindows(self):
        self.taskWindow=TasksWindow()
        self.ui.taskManage.clicked.connect(lambda:self.taskWindow.exec())
        self.taskWindow.sendSignal.connect(self.ui.tableWidgetFiles.setScanTaskID)
        self.taskWindow.sendSignal.connect(lambda:self.setFilmInfo())
        self.ui.addFilm.clicked.connect(self.ui.tableWidgetFiles.addFilm)
        self.ui.delFilm.clicked.connect(self.ui.tableWidgetFiles.delFilm)
        self.ui.syncFilm.clicked.connect(self.ui.tableWidgetFiles.syncFilm)

        self.ui.tableWidgetFiles.doubleClicked.connect(self.setImage)
    
    def resetMenu(self):
        for bt in self.menuList:
            if self.sender().objectName()==bt.objectName():
                bt.setProperty('select',True)
            else:
                bt.setProperty('select',False)
            self.ui.menubar.style().polish(bt)

    def setFilmInfo(self):
        row=self.taskWindow.ui.tableWidget.currentRow()
        taskname=self.taskWindow.ui.tableWidget.item(row,self.taskWindow.tableHeader.index('TASKNAME')).text()
        qyname=self.taskWindow.ui.tableWidget.item(row,self.taskWindow.tableHeader.index('QYNAME')).text()
        tasknum=self.taskWindow.ui.tableWidget.item(row,self.taskWindow.tableHeader.index('TASKNUM')).text()
        createtime=self.taskWindow.ui.tableWidget.item(row,self.taskWindow.tableHeader.index('CREATETIME')).text()
        self.ui.taskName.setText(taskname)
        self.ui.companyName.setText(qyname)
        self.ui.taskNum.setText(tasknum)
        self.ui.createTime.setText(createtime)

    def setImage(self):
        row=self.ui.tableWidgetFiles.currentRow()
        filePath=self.ui.tableWidgetFiles.item(row,self.ui.tableWidgetFiles.tableHeader.index('FILMLJ')).text()
        if not os.path.exists(filePath):
            box=MyMessageBox(self)
            box.setIcon(MyMessageBox.Information)
            box.setWindowTitle('提示')
            box.setText('无效路径,请同步底片')
            box.exec()
            return 
        try:
            image=Image.open(filePath)
        except Exception as e:
            box=MyMessageBox(self)
            box.setIcon(MyMessageBox.Information)
            box.setWindowTitle('提示')
            box.setText('服务器中该图像损坏,请联系管理员后重新同步底片')
            box.exec()
            return
        self.ui.image.setImage(tiff_force_8bit(image))
