# -*- coding:utf8 -*-
from PIL import  Image
import os.path
import glob
def convertjpg(jpgfile,outir,width = 416 ,height = 416):#将图片修改为416X416
    img = Image.open(jpgfile)
    try:
        new_img = img.resize((width,height),Image.BILINEAR)
        new_img.save(os.path.join(outir,os.path.basename(jpgfile)))
    except Exception as e:
        print(e)
imgName = 't'
for jpgfile in  glob.glob("D:\phpStudy\WWW\image\*.jpg"):
    try:
        convertjpg(jpgfile,"image")
    except:
        continue
