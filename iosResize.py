#!/usr/bin/python
# -*- coding: utf-8 -*-
import os.path  
import sys  
from PIL import Image  
  
""" 
自动生成不同分辨率下的App图片 
UI设计1080*1920分辨率图片，放在drawable-xxhdpi目录下，自动生成其它的分辨率图片 
"""  
  
__author__ = ['"Xitao":<offbye@gmail.com>']  
  
  
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
  
  
# def path_resize(src, target, percent):  
#     if not os.path.isdir(src):  
#         print(src + " must be a dir")  
#         return -1  
  
#     os.chdir(src)  
#     cwd = os.getcwd()  
#     dirs = os.listdir(cwd)  
#     for file_name in dirs:  
#         print(file_name)  
#         if file_name.endswith('.9.png'):  
#             continue  
  
#         src_file = os.path.join(cwd, file_name)  
  
#         if not os.path.exists(target):  
#             os.mkdir(target)
#         image_resize(src_file, target + '/' + file_name, percent)  

def android(img):
    if not os.path.isabs(img): # 相对路径
          img = os.path.abspath(img)
    out_path = os.path.join(os.path.dirname(img), 'ios')  
  
    if not os.path.exists(out_path):  
        os.mkdir(out_path)  
    base_name = os.path.basename(img)
    split_name = os.path.splitext(base_name)
    image_resize(img, out_path + os.path.sep + split_name[0] + '@3x' + split_name[1], 1.0)  
    image_resize(img, out_path + os.path.sep + split_name[0] + '@2x' + split_name[1], 0.667)  
    image_resize(img, out_path + os.path.sep + split_name[0] + split_name[1], 0.333)  
  
  
if __name__ == "__main__":  
    print('please input your androd res dir path')  
    print(sys.argv)  
    if sys.argv[1]:  
        android(sys.argv[1])  
