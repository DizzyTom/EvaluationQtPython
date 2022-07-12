import json
import os
import numpy as np
from PIL import Image



class Const:
    # path
    config_path='conf/config.json'
    # urls
    login_url='YHXG/login/'
    taskManage_url="ScanTask/TaskManage/"
    addTask_url="ScanTask/AddTask/"
    deleteTask_url="ScanTask/DeleteTask/"
    changeTask_url="ScanTask/ChangeTask/"
    searchTask_url="ScanTask/SearchTask/"
    getTaskInfo_url="ScanTask/GetTaskInfo/"
    searchFilms_url="ScanTask/SearchFilms/"
    addFilm_url="ScanTask/AddFilm/"
    delFilm_url="ScanTask/DelFilm/"
    searchFilms_url="ScanTask/SearchFilms/"
    uploadFilm_url="ScanTask/UploadFilm/"
    downloadFilm_url="ScanTask/DownloadFilm/"
    # standards
    # IP地址规范
    ipRange = "([0-1]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])"
    # 端口 0~65535
    portRange = "([1-9]|[1-9][0-9]|[1-9][0-9][0-9]|[1-9][0-9][0-9][0-9]|[1-5][0-9][0-9][0-9][0-9]|6[0-4][0-9][0-9][0-9]|65[0-4][0-9][0-9]|655[0-2][0-9]|6553[0-5])"
    

class WebConnect:
    def __init__(self) -> None:
        self.ip,self.port=self.getIP_Port()
    def getIP_Port(self):
        with open(Const.config_path, 'r', encoding='utf-8') as f:
            conf = json.load(f)
        return conf['ip'],conf['port']

    def getUrl(self,path=''):
        return "http://" + self.ip + ":" + self.port + "/" + path
  
    def setIP_Port(self,ip:str,port:str):
        with open(Const.config_path, 'r', encoding='utf-8') as f:
            conf = json.load(f)
        conf['ip']=ip
        conf['port']=port
        with open(Const.config_path,'w',encoding='utf-8') as f:
            json.dump(conf,f)
        self.ip=ip
        self.port=port
webConnect=WebConnect()

def encodeGBK(x):
    for k,v in x.items():
        x[k]=v.encode("GBK")
    return x


def getFilesWithSubffix(rootpath,subffixs):
    fileList=os.listdir(rootpath)
    ans=[]
    for file in fileList:
        path = os.path.join(rootpath, file)
        if os.path.splitext(path)[-1] in subffixs:
            ans.append(path)
        elif os.path.isdir(path):
            ans+=getFilesWithSubffix(path,subffixs)
    return ans

def tiff_force_8bit(image):
    if image.format == 'TIFF' and image.mode == 'I;16':
        array = np.array(image)
        normalized = (array.astype(np.uint16) - array.min()) * 255.0 / (array.max() - array.min())
        image = Image.fromarray(normalized.astype(np.uint8))
    return image
