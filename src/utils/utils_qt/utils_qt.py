from PySide6.QtWidgets import QMessageBox,QMainWindow,QWidget
from PySide6.QtCore import Qt
from qt_for_python.uic.loading import Ui_MainWindow
import resource_rc

class MyMessageBox(QMessageBox):
    def __init__(self,parent=None):
        super().__init__(parent=parent)
        with open('res/qss/messagebox.qss','r',encoding='utf-8') as f:
            self.setStyleSheet(f.read())

class LoadingWindow(QMainWindow):
    def __init__(self,parent:QWidget=None):
        super().__init__(parent)
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)
        if parent is not None:
            self.setGeometry(0,0,parent.width(),parent.height())

    def reShape(self):
        if self.parent() is not None:
            self.setGeometry(0,0,self.parent().width(),self.parent().height())

