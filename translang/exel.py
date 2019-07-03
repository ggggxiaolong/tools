#!/usr/bin/python
# -*- coding: UTF-8 -*-
import xlwt
import os.path
import sys
import sqlite3

def write_excel(db_path):
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    header = ['id','file_name','label','default_text','not_trans','en','ko','ja','sk','cs','fr']

    book = xlwt.Workbook(encoding='utf-8', style_compression=0) # 创建一个Workbook对象，这就相当于创建了一个Excel文件
    sheet = book.add_sheet('translate', cell_overwrite_ok=True)  # # 其中的test是这张表的名字,cell_overwrite_ok，表示是否可以覆盖单元格，其实是Worksheet实例化的一个参数，默认值是False

    # 设置表头
    i = 0
    for k in header:
        sheet.write(0, i, k)
        i = i + 1

    # 数据写入excel
    row = 1
    cursor = c.execute("SELECT id,file_name,label,default_text,not_trans,en,ko,ja,sk,cs,fr from lang")
    for val in cursor:
        print(val)
        sheet.write(row , 0, val[0])
        sheet.write(row , 1, val[1])
        sheet.write(row , 2, val[2])
        sheet.write(row , 3, val[3])
        sheet.write(row , 4, val[4])
        sheet.write(row , 5, val[5])
        sheet.write(row , 6, val[6])
        sheet.write(row , 7, val[7])
        sheet.write(row , 8, val[8])
        sheet.write(row , 9, val[9])
        sheet.write(row , 10, val[10])
        row = row + 1

    conn.close()
    # 最后，将以上操作保存到指定的Excel文件中
    book.save(r'language.xls')

if __name__ == "__main__":
    print(sys.argv)  
    if sys.argv[1]:
        write_excel(sys.argv[1])
