from PySide6.QtWidgets import QApplication, QMainWindow
from qt_for_python.uic.main import Ui_MainWindow
import PySide6
import os

# Configure the environment of Qt
dirname = os.path.dirname(PySide6.__file__)
plugin_path = os.path.join(dirname, 'plugins', 'platforms')
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = plugin_path

# Main Window Class
class Window(QMainWindow):
    def __init__(self,parent=None) -> None:
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

# Main Program
if __name__ == '__main__':
    app = QApplication([])
    window = Window()
    window.show()
    app.exec()
