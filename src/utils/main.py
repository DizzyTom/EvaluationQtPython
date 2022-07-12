from PySide6.QtWidgets import QMainWindow,QFileDialog,QTableWidgetItem
from qt_for_python.uic.main import Ui_MainWindow
from .tasks import TasksWindow
from .utils import getFilesWithSubffix,tiff_force_8bit
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
            self.ui.taskbutton,
            self.ui.judgebutton,
            self.ui.recordbutton,
            self.ui.configbutton,
            self.ui.viewbutton,
            self.ui.helpbutton,
        ]
        self.ui.taskbutton.clicked.connect(lambda:self.ui.tools.setCurrentWidget(self.ui.taskpage))
        self.ui.judgebutton.clicked.connect(lambda:self.ui.tools.setCurrentWidget(self.ui.judgepage))
        self.ui.recordbutton.clicked.connect(lambda:self.ui.tools.setCurrentWidget(self.ui.recordpage))
        self.ui.configbutton.clicked.connect(lambda:self.ui.tools.setCurrentWidget(self.ui.configpage))
        self.ui.viewbutton.clicked.connect(lambda:self.ui.tools.setCurrentWidget(self.ui.viewpage))
        self.ui.helpbutton.clicked.connect(lambda:self.ui.tools.setCurrentWidget(self.ui.helppage))
        for bt in self.menuList:
            bt.clicked.connect(self.resetMenu)
        self.ui.taskbutton.click()

    def setSubWindows(self):
        self.taskWindow=TasksWindow()
        self.ui.taskManage.clicked.connect(lambda:self.taskWindow.exec())
    
    def resetMenu(self):
        for bt in self.menuList:
            if self.sender().objectName()==bt.objectName():
                bt.setProperty('select',True)
            else:
                bt.setProperty('select',False)
            self.ui.centralwidget.style().polish(bt)

    
    
