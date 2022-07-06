from PySide6.QtWidgets import QMainWindow
from PySide6.QtGui import QIcon,QPixmap
from qt_for_python.uic.main import Ui_MainWindow


# Main Window Class
class MainWindow(QMainWindow):
    def __init__(self,parent=None) -> None:
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)