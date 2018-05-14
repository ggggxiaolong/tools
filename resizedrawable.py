#!/usr/bin/python
# -*- coding: utf-8 -*-
import os.path  
import sys  
from PIL import Image  
  
""" 
自动生成不同分辨率下的App图片 
UI设计1080*1920分辨率图片，drawable-xxxhdpi目录下，自动生成其它的分辨率图片 
"""  
  
__author__ = ['"Xitao":<freemrtan@gmail.com>']  
  
  
def image_resize(img_file, target, percent):  
    """resize image and save to target path 
    :param img_file: image file path 
    :param target: save path 
    :param percent: resize percent 
    :return: 
    """  
    img = Image.open(img_file)  
    print(img.size)  
    width, height = img.size  
    target_img = img.resize((int(width * percent), int(height * percent)), Image.ANTIALIAS)  
    target_img.save(target)  
    img.close()  
    target_img.close()  
    print(" save target image to " + target)  
  
  
def path_resize(src, target, percent):  
    if not os.path.isdir(src):  
        print(src + " must be a dir")  
        return -1  
  
    os.chdir(src)  
    cwd = os.getcwd()  
    dirs = os.listdir(cwd)  
    for file_name in dirs:  
        print(file_name)  
        if file_name.endswith('.9.png'):  
            continue  
  
        src_file = os.path.join(cwd, file_name)  
  
        if not os.path.exists(target):  
            os.mkdir(target)
        image_resize(src_file, target + '/' + file_name, percent)  
  
  
def android(res_dir):
    if not os.path.isabs(res_dir):
          res_dir = os.path.abspath(res_dir)
    xxhdpi_path = res_dir + "/drawable-xxxhdpi/"  
  
    if not os.path.isdir(xxhdpi_path):  
        print("xxhdpi_path must be a dir")  
        return -1  
  
    path_resize(xxhdpi_path, res_dir + '/drawable-land-xxhdpi', 1)
    path_resize(xxhdpi_path, res_dir + '/drawable-land-xhdpi', 0.75)
    path_resize(xxhdpi_path, res_dir + '/drawable-xxhdpi', 0.75)
    path_resize(xxhdpi_path, res_dir + '/drawable-xhdpi', 0.5)  
    path_resize(xxhdpi_path, res_dir + '/drawable-hdpi', 0.375)  
    path_resize(xxhdpi_path, res_dir + '/drawable-mdpi', 0.25)  
  
  
if __name__ == "__main__":  
    print('please input your androd res dir path')  
    print(sys.argv)  
    if sys.argv[1]:  
        android(sys.argv[1])  
