#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import sqlite3
from xml.etree.ElementTree import Element, SubElement, ElementTree
import sys
import os

def write_es(array:[(str, str)]):
    # 生成根节点
    root = Element('resources')
    for item in array:
        (label, text) = item
        head = SubElement(root, 'string')
        head.set('name', label)
        head.text = text
    tree = ElementTree(root)
    tree.write('result_es.xml', encoding="utf-8")

def write_ko(array:[(str, str)]):
    # 生成根节点
    root = Element('resources')
    for item in array:
        (label, text) = item
        head = SubElement(root, 'string')
        head.set('name', label)
        head.text = text
    tree = ElementTree(root)

    tree.write('result_ko.xml', encoding="utf-8")

def read_db(db_path: str):
    if not os.path.isabs(db_path):
        res_dir:str = os.path.abspath(db_path)
    db_path = res_dir + '/language.db'
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    ko_array:[(str,str)] = []
    es_array:[(str,str)] = []
    for row in c.execute("SELECT label, ko, es FROM lang"):
        (label, ko, es) = row
        ko_array.append((label, ko))
        es_array.append((label, es))
    conn.close()
    write_es(es_array)
    write_ko(ko_array)

if __name__ == "__main__":
    # print(sys.argv)  
    if sys.argv[1]:
        read_db(sys.argv[1]) 