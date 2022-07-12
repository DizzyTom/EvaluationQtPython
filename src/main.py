from PySide6.QtWidgets import QApplication
from utils.login import LoginWindow
from utils.main import MainWindow
if __name__=='__main__':
    app=QApplication([])
    main_window=MainWindow()
    login_window=LoginWindow()
    login_window.show()
    login_window.login_signal.connect(lambda:main_window.showMaximized())
    # main_window.showMaximized()
    app.exec()
