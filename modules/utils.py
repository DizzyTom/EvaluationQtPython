import os
from typing import List
import numpy as np
from PIL import Image

def getFilesWithSubffix(rootpath,subffixs)->List:
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
