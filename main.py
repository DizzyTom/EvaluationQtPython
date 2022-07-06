from PySide6.QtWidgets import QApplication
import PySide6
import os
from modules.main import MainWindow

# Main Program
if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
