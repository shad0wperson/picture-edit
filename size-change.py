# -*- coding: utf-8 -*-
import os
import glob
from PIL import Image
import os.path

 

'''修改图片文件大小jpgfile：图片文件；savedir：修改后要保存的路径'''
def convertjpg(jpgfile,savedir,width=400,height=300):

    img=Image.open(jpgfile)
    new_img=img.resize((width,height),Image.BILINEAR)
    new_img.save(os.path.join(savedir,os.path.basename(jpgfile)))

'''查找给定路径下图片文件，并修改其大小'''
def modifyjpgSize(file,saveDir):
    for jpgfile in glob.glob(file):
        try:
            convertjpg(jpgfile,saveDir)
        except OSError:
            print("格式不对,跳过")
            continue

#测试代码
file = r'D:\ele-pic\*.png'
saveDir = r'D:\ele-pic1'

modifyjpgSize(file,saveDir)
