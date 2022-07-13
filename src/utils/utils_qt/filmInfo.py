from PySide6.QtWidgets import QTableWidget,QFileDialog,QTableWidgetItem,QPushButton
from PySide6.QtCore import QThread,Signal
import requests
from ..utils import Const,webConnect,encodeGBK
from .utils_qt import MyMessageBox,LoadingWindow
import os
import shutil

class DownloadThread(QThread):
    trigger=Signal(int,int)
    def __init__(self,ljs,ids,parent=None) -> None:
        super().__init__(parent)
        self.ljs=ljs
        self.ids=ids
    def run(self):
        try:
            self.trigger.emit(0,len(self.ljs))
            for i in range(len(self.ljs)):
                lj=self.ljs[i]
                data={
                "filmid":self.ids[i]
                }
                ret=requests.post(webConnect.getUrl(Const.downloadFilm_url),data=encodeGBK(data))
                with open(lj,'wb') as f:
                    f.write(ret.content)
                self.trigger.emit(i+1,len(self.ljs))
        except Exception as e:
            print(e)
            self.trigger.emit(-1,0)
        self.quit()


class UploadThread(QThread):
    trigger=Signal(int,int)
    def __init__(self, data,files,data2,parent=None) -> None:
        super().__init__(parent)
        self.files=files
        self.data=data
        self.data2=data2
    def run(self):
        try:
            self.trigger.emit(0,1)
            ret=requests.post(webConnect.getUrl(Const.uploadFilm_url),data=encodeGBK(self.data),files=self.files).json()
            if ret['ret']!=1:
                box=MyMessageBox(self.parent())
                box.setIcon(MyMessageBox.Information)
                box.setWindowTitle('提示')
                box.setText('底片上传失败')
                box.exec()
            else:
                requests.post(webConnect.getUrl(Const.addFilm_url),encodeGBK(self.data2)).json()
                self.parent().refresh()
            self.trigger.emit(1,1)
        except Exception as e:
            print(e)
            self.trigger.emit(-1,0)
        self.quit()

class FilmInfo(QTableWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.tableHeader=[None,'FILMNAME','DPPJ','FILMLJ','id']
        self.tableHeaderName=['序号','底片名称','评定状态','底片路径','id']
        self.setColumnCount(len(self.tableHeader))
        self.setHorizontalHeaderLabels(self.tableHeaderName)
        # self.setColumnHidden(self.tableHeader.index('id'),True)
        self._window=LoadingWindow(self)
        self._window.hide()
    
    def resizeEvent(self,event):        
        self._window.reShape()
        super().resizeEvent(event)
    def setScanTaskID(self,_id,taskname,companyname):
        self.scantaskID=_id
        self.taskname=taskname
        self.companyname=companyname
        self.refresh()

    def refresh(self):
        data={
            'id':self.scantaskID
        }
        ret=requests.post(webConnect.getUrl(Const.searchFilms_url),data).json()
        self.clearContents()
        self.setRowCount(0)
        # print(ret['res'])
        for i,ans in enumerate(ret['res']):
            row=self.rowCount()
            self.setRowCount(row+1)
            for name in self.tableHeader:
                txt=ans.get(name,None)
                if name is None:
                    txt=str(i)
                elif name=='DPPJ':
                    if txt is None:
                        txt='未评定'
                    else:
                        txt='已评定'
                else:
                    txt=str(txt)
                self.setItem(row,self.tableHeader.index(name),QTableWidgetItem(txt))
        self.resizeColumnsToContents()
        self.resizeRowsToContents()
    def addFilm(self):
        if self.scantaskID is None:
            return
        filePath=QFileDialog.getOpenFileName(self,caption='选择底片',filter='Image(*.mim *.png *.jpg *.bmp)')[0]
        dstPath="D:\\底片数据\\"+self.companyname+'\\'+self.taskname+'\\'+str(self.rowCount())+os.path.splitext(filePath)[-1]
        if filePath!=dstPath:
            if not os.path.exists(os.path.dirname(filePath)):
                os.makedirs(os.path.dirname(filePath))
            shutil.copy(filePath,dstPath)
        data={
            'filepath':dstPath,
        }
        files={
            'img':(
                filePath,
                open(filePath,'rb')
            )
        }
        data2={
            'scantaskid':self.scantaskID,
            'filmname':str(self.rowCount()),
            'filmlj':dstPath
        }
        self._window.show()
        self.thread_upload=UploadThread(data,files,data2,self)
        self.thread_upload.trigger.connect(self.downloadFinish)
        self.thread_upload.start()
    
    def delFilm(self):
        contents = self.selectedItems()
        rowList = []
        for item in contents:
            if item.row() in rowList:
                continue
            rowList.append(item.row())
        if len(rowList)==0:
            return

        box=MyMessageBox(self)
        box.setIcon(MyMessageBox.Question)
        box.setWindowTitle('提问')
        box.setText('是否删除')
        okbtn=QPushButton('是')
        nobtn=QPushButton('否')
        box.addButton(okbtn,MyMessageBox.AcceptRole)
        box.addButton(nobtn,MyMessageBox.RejectRole)
        box.exec()
        if box.clickedButton()!=okbtn:
            return
        rowList = sorted(
            rowList,
            key=lambda x: int(
                self.item(x, self.tableHeader.index(None)).text()
            ),
            reverse=True,
        )
        for row in rowList:
            _id = self.item(row, self.tableHeader.index("id")).text()
            ret = requests.post(
                webConnect.getUrl(Const.delFilm_url), data={"filmid": _id}
            ).json()
            if ret["ret"] == 1:
                self.removeRow(row)
        self.refresh()

    def syncFilm(self):
        # self.window().setWindowModality(Qt.ApplicationModal)
        contents = self.selectedItems()
        rowList = []
        for item in contents:
            if item.row() in rowList:
                continue
            rowList.append(item.row())
        if len(rowList)==0:
            return
        self._window.show()
        rows=self.rowCount()
        _ids=[]
        _filmljs=[]
        for i in rowList:
            _id=self.item(i,self.tableHeader.index('id')).text()  
            _filmlj=self.item(i,self.tableHeader.index('FILMLJ')).text()
            if not os.path.exists(os.path.dirname(_filmlj)):
                os.makedirs(os.path.dirname(_filmlj))
            _ids.append(_id)
            _filmljs.append(_filmlj)
            
        self.thread_download=DownloadThread(_filmljs,_ids,parent=self)        
        self.thread_download.trigger.connect(self.downloadFinish)
        self.thread_download.start()

    def downloadFinish(self,now,tot):
        if now==-1:
            self.thread_download.exit()
            self._window.hide()
        if now==tot:
            self._window.ui.label_2.setText("加载完毕")
            # self.window().setWindowModality(Qt.NonModal)
            self._window.hide()
        else:
            self._window.ui.label_2.setText("加载中,第{}个,共{}个".format(now,tot))