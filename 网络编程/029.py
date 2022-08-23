#解决粘包问题

import struct

payload = 'string'
#数值转为固定的4字节
v1 = struct.pack('i',199)#长度为199
print(v1)

for i in v1:
    print(i,bin(i))

#再将4字节转换为数字
v2 = struct.unpack('i', v1)
print(v2)

