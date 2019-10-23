#!/usr/bin/python
# -*- coding: UTF-8 -*-
from xml.dom.minidom import parse
import xml.dom.minidom
import sqlite3
import time
import sys
import os


def inittable(path, filename, db_path, mode_name):
    DOMTree = xml.dom.minidom.parse(path)
    root = DOMTree.documentElement
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    res = root.getElementsByTagName("string")
    for trans in res:
        label = trans.getAttribute("name")
        content = trans.childNodes[0].data
        if trans.hasAttribute("translatable") and trans.getAttribute("translatable") == "false":
            transFlag = 1
        else:
            transFlag = 0
        c.execute("INSERT INTO lang (file_name,label,descripe,not_trans,user_id,project_id,mode_name,create_time) \
        VALUES (?,?,?,?,?,?,?,?)",(filename, label, content, transFlag, 1, 3, mode_name, int(round(time.time() * 1000))))
        # print(filename, label, content, transFlag)
    conn.commit()
    conn.close()

def update(path, filename, lang, db_path):
    DOMTree = xml.dom.minidom.parse(path)
    root = DOMTree.documentElement
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    res = root.getElementsByTagName("string")
    for trans in res:
        label = trans.getAttribute("name")
        content = trans.childNodes[0].data
        # sql = "UPDATE toc_android SET %s = ? WHERE file_name = ? \
        # and labe = ?" % (lang)
        # print(sql, content, filename, label)
        c.execute("UPDATE lang SET %s = ? WHERE file_name = ? \
        and label = ?" % (lang),(content, filename, label))
    conn.commit()
    conn.close()

def read_basepath(path, baseName, db_path, mode_name):
    root_path = os.listdir(path)
    for name in root_path:
        if name.endswith('.xml'):
            inittable(path + '/' + name, name, db_path, mode_name)
            print(path + '/' + name, baseName + '/' + name)

def read_transpath(path, baseName, db_path):
    lang = baseName[-2:]
    root_path = os.listdir(path)
    for name in root_path:
        if name.endswith('.xml'):
            update(path + '/' + name, name, lang, db_path)
            print(path + '/' + name, baseName + '/' + name, lang)

def spare_file(res_dir, db_path, mode_name):
    print(res_dir)
    print(db_path)
    # os.chdir(res_dir)
    root_path = os.listdir(res_dir)
    child_path = res_dir + '/values'
    read_basepath(child_path, 'values', db_path, mode_name)
    for base_path in root_path:
        child_path = res_dir + '/' + base_path
        if os.path.isdir(child_path):
            if not base_path == "values":
                read_transpath(child_path, base_path, db_path)

def check_mode(res_dir, project_dir):
    if not os.path.isabs(res_dir):
        res_dir = os.path.abspath(res_dir)

    if not os.path.isabs(project_dir):
        project_dir = os.path.abspath(project_dir)
    db_path = res_dir + '/database.sqlite'
    # 遍历modle
    os.chdir(project_dir)
    mode_dirs = os.listdir(os.getcwd())
    for mode_path in mode_dirs:
        res_dir = mode_path + '/src/main/res'
        if os.path.exists(res_dir):
            spare_file(res_dir, db_path, mode_path)
            # print(res_dir)
            # print(mode_path)

if __name__ == "__main__":
    print(sys.argv)  
    if sys.argv[1]:
        check_mode(sys.argv[1], sys.argv[2]) 
