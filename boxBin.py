#!/usr/bin/python3

import binascii

prefix: bytes = bytes([0x55, 0xaa, 0x1e, 0x00])
version: bytes = bytes([0x03, 0x01])
ota_start: bytes = bytes([0x55, 0xaa, 0x1c, 0x00])
# 新增 target 字段 0x01 代表指纹芯片， 0x02代表stm32芯片
target: bytes = bytes([0x01])
# 数据包长度 box的长度为1024 lock的长度为512
pkt_len: bytes = bytes([0x00, 0x02])
pkt_size: int = 512

def read():
    file = open("app_new.bin", 'rb')
    out_file = open("tlbox_fix.bin",'wb')
    bin: bytes = file.read()
    file.close
    length: int = len(bin)
    pgk_size = (length + pkt_size -1)//pkt_size
    first_cmd: bytes = gen_first(length, bin)
    out_file.write(first_cmd)
    for index in range(pgk_size):
        start: int = index * pkt_size
        end: int = (index + 1) * pkt_size
        if end > length:
            end = length
        data = bin[start:end]
        data_len: bytes = (end - start).to_bytes(2, byteorder='little')
        data_prefix = prefix + data_len
        crc: bytes = cal_crc(data + data_prefix)
        cmd = data_prefix + data + crc
        out_file.write(cmd)
    out_file.close()

def gen_first(length: int, data: bytes) -> bytes:
    file_len: bytes = int2bytes(length, 4)
    file_crc: bytes = int2bytes(add_bytes(data) & 0xffff, 4)
    cmd_len: bytes = int2bytes(len(version) + len(file_len) + len(file_crc) + len(pkt_len) + len(target), 2)
    cmd_pre: bytes = ota_start + cmd_len + version +file_len + file_crc + pkt_len + target
    cmd_crc: bytes = cal_crc(cmd_pre)
    cmd: bytes = cmd_pre + cmd_crc + bytes(40-21)
    return cmd

def cal_crc(cmd: bytes) -> bytes:
    sum:int = add_bytes(cmd)
    sum = sum & 0xffff
    return sum.to_bytes(2, byteorder='little')

def add_bytes(value: bytes) -> int:
    sum: int = 0
    for b in value:
        sum += int(b)
    return sum

def int2bytes(value: int, length: int) -> bytes: 
    return value.to_bytes(length, byteorder="little")

if __name__ == "__main__":
    read()
