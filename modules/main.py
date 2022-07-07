from PySide6.QtWidgets import (
    QMainWindow, QMenu, QFileDialog, QTableWidgetItem, QMessageBox, QGraphicsPixmapItem,QGraphicsScene)
from PySide6.QtCore import QModelIndex
from PySide6.QtGui import QPixmap
from qt_for_python.uic.main import Ui_MainWindow
from .utils import getFilesWithSubffix,tiff_force_8bit
import os
from PIL import Image,ImageQt

# Main Window Class


class MainWindow(QMainWindow):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setMenu()
        self.setTableWidgetFiles()

    def setMenu(self):
        self.setActions()
        # File Menu
        self.menuFile = QMenu()
        self.menuFile.addActions([
            self.ui.actionOpen,
            self.ui.actionOpenDatabase
        ])
        self.menuFile.addSeparator()
        self.menuFile.addActions([
            self.ui.actionPrintPreview,
            self.ui.actionPrintConfig
        ])
        self.menuFile.setFixedWidth(140)
        self.menuFile.setFixedHeight(200)
        with open('res/qss/menu.qss', 'r', encoding='utf-8') as f:
            style = f.read()
        self.menuFile.setStyleSheet(style)
        self.ui.pushButtonFile.setMenu(self.menuFile)
        # Config Menu
        self.menuConfig = QMenu()
        self.menuConfig.addActions([
            self.ui.actionCloudConnect
        ])
        self.menuConfig.setFixedWidth(140)
        self.menuConfig.setFixedHeight(200)
        self.menuConfig.setStyleSheet(style)
        self.ui.pushButtonConfig.setMenu(self.menuConfig)

    def setActions(self):
        self.ui.actionOpen.triggered.connect(self.openFiles)

    def openFiles(self):
        directory = QFileDialog.getExistingDirectory(self, "选取文件夹", "./")
        if not os.path.exists(directory):
            return
        files = getFilesWithSubffix(directory, ['.png','.jpg','.mim','.bmp'])
        self.ui.tableWidgetFiles.clearContents()
        self.ui.tableWidgetFiles.setRowCount(len(files))
        for i in range(len(files)):
            path = files[i]
            self.ui.tableWidgetFiles.setItem(
                i, 0, QTableWidgetItem('.'.join(os.path.basename(path).split('.')[:-1])))
            self.ui.tableWidgetFiles.setItem(i, 1, QTableWidgetItem(path))
        self.ui.tableWidgetFiles.resizeColumnsToContents()
        self.ui.tableWidgetFiles.resizeRowsToContents()

    def setTableWidgetFiles(self):
        with open('res/qss/verticalScroll.qss', 'r') as f:
            vScrollStyle = f.read()
        self.ui.tableWidgetFiles.verticalScrollBar().setStyleSheet(vScrollStyle)
        with open('res/qss/horizontalScroll.qss', 'r') as f:
            hScrollStyle = f.read()
        self.ui.tableWidgetFiles.horizontalScrollBar().setStyleSheet(hScrollStyle)
        self.ui.tableWidgetFiles.resizeColumnsToContents()
        self.ui.tableWidgetFiles.resizeRowsToContents()
        self.ui.tableWidgetFiles.doubleClicked.connect(
            self.tableWidgetFilesDoubleClick)

    def tableWidgetFilesDoubleClick(self, index: QModelIndex):
        row = index.row()
        path = self.ui.tableWidgetFiles.item(row, 1).text()
        if not os.path.exists(path):
            QMessageBox(QMessageBox.Critical, '错误', '文件不存在').exec()
            return
        image=tiff_force_8bit(Image.open(path))
        self.showImage(image)

    def showImage(self,image):        
        frame = ImageQt.ImageQt(image)
        pix = QPixmap.fromImage(frame)
        item = QGraphicsPixmapItem(pix)
        scene=QGraphicsScene()
        scene.addItem(item)
        self.ui.graphicsView.setScene(scene)

