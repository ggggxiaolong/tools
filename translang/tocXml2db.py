#!/usr/bin/python
# -*- coding: UTF-8 -*-
from xml.dom.minidom import parse
import xml.dom.minidom
import sqlite3
import os.path
import sys


def inittable(path, filename, db_path):
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
        c.execute("INSERT INTO lang (file_name,label,default_text,not_trans) \
        VALUES (?,?,?,?)",(filename, label, content, transFlag))
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

def read_basepath(path, baseName, db_path):
    os.chdir(path)
    root_path = os.listdir(os.getcwd())
    for name in root_path:
        if name.endswith('.xml'):
            inittable(path + '/' + name, name, db_path)
            print(path + '/' + name, baseName + '/' + name)

def read_transpath(path, baseName, db_path):
    lang = baseName[-2:]
    os.chdir(path)
    root_path = os.listdir(os.getcwd())
    for name in root_path:
        if name.endswith('.xml'):
            update(path + '/' + name, name, lang, db_path)
            print(path + '/' + name, baseName + '/' + name, lang)

def spare_file(res_dir):
    if not os.path.isabs(res_dir):
        res_dir = os.path.abspath(res_dir)
    db_path = res_dir + '/language.db'
    print(res_dir)
    print(db_path)
    os.chdir(res_dir)
    root_path = os.listdir(os.getcwd())
    child_path = res_dir + '/values'
    read_basepath(child_path, '/values', db_path)
    for base_path in root_path:
        child_path = res_dir + '/' + base_path
        if os.path.isdir(child_path):
            if not base_path == "values":
                read_transpath(child_path, base_path, db_path)

if __name__ == "__main__":
    print(sys.argv)  
    if sys.argv[1]:
        spare_file(sys.argv[1]) 
