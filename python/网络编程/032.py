#服务端

import os
import json
import socket
import struct

def recv_data(conn, chunk_size=1024):
    has_read_size = 0
    bytes_list = []
    while has_read_size<4:
        chunk = conn.recv(4-has_read_size)
        has_read_size += len(chunk)
        bytes_list.append(chunk)
    header = b"".join(bytes_list)
    data_length = struct.unpack('i', header)[0]

    data_list=[]
    
