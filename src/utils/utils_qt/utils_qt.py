from PySide6.QtWidgets import QMessageBox,QSplitter

class MyMessageBox(QMessageBox):
    def __init__(self,parent=None):
        super().__init__(parent=parent)
        with open('res/qss/messagebox.qss','r',encoding='utf-8') as f:
            self.setStyleSheet(f.read())