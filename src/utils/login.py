from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Qt, Signal,QRegularExpression
from PySide6.QtGui import QPainter,QRegularExpressionValidator
from win32gui import ReleaseCapture
from win32api import SendMessage
import win32con
from qt_for_python.uic.login import Ui_Form
from utils.utils import webConnect,Const,encodeGBK
from utils.utils_qt.utils_qt import MyMessageBox
import requests
from .utils import Const


class LoginWindow(QWidget):
    login_signal=Signal(int)
    def __init__(self, parent=None, radius=10):
        super().__init__(parent)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowFlags(Qt.FramelessWindowHint |
                            Qt.WindowMinimizeButtonHint)
        self.radius = radius
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        ipRegex = QRegularExpression("^" + Const.ipRange + "\\." + Const.ipRange + "\\." + Const.ipRange + "\\." + Const.ipRange + "$")
        ipValidator = QRegularExpressionValidator(ipRegex, self)
        self.ui.ip.setValidator(ipValidator)

        portRegex=QRegularExpression("^"+Const.portRange+"$")
        portValidator=QRegularExpressionValidator(portRegex,self)
        self.ui.port.setValidator(portValidator)

        # 填写默认IP和端口号
        ip,port=webConnect.getIP_Port()
        self.ui.ip.setText(ip)
        self.ui.port.setText(port)
        self.ui.name.setFocus()
        # 点击退出按钮关闭
        self.ui.quit.clicked.connect(self.close)

        # 点击登录按钮尝试连接
        self.ui.login.clicked.connect(self.try_connect)
        
        self.ui.login.setShortcut('enter')
        self.ui.quit.setShortcut('esc')    
        

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setBrush(Qt.white)
        painter.setPen(Qt.transparent)
        painter.drawRoundedRect(self.rect(), self.radius, self.radius)
        event.accept()

    def mouseMoveEvent(self, event):
        ReleaseCapture()
        SendMessage(self.window().winId(), win32con.WM_SYSCOMMAND,
                    win32con.SC_MOVE + win32con.HTCAPTION, 0)
        event.ignore()

    def try_connect(self):
        # 保存ip port
        webConnect.setIP_Port(self.ui.ip.text(),self.ui.port.text())
        url=webConnect.getUrl(Const.login_url)
        data={}
        data.setdefault('yhbm',self.ui.name.text())
        data.setdefault('yhmm',self.ui.password.text())
        ret=requests.post(url,encodeGBK(data)).json()
        if ret['ret']==1:
            self.login_signal.emit(1)
            self.close()
        else:
            messageBox=MyMessageBox(self)
            messageBox.setIcon(MyMessageBox.Information)
            messageBox.setWindowTitle('登录失败')
            messageBox.setText(ret['msg'])
            messageBox.addButton('确定',MyMessageBox.YesRole)
            messageBox.exec()
        
