"""
使用须知：
1. 使用struct包，转换二进制数据
2. C语言数据类型与Python数据类型转换：https://docs.python.org/3/library/struct.html#format-characters
"""

import struct

# 创建float型二进制数据
a = struct.pack('f', 12.34)
print(f"转换的二进制：{a}", )
# 创建char[]类型二进制数据
b = struct.pack('4s', 'test'.encode('utf-8'))
print(f"转换的二进制：{b}", )

# 写入到二进制文件
f = open('test.dat', 'wb+')
f.write(a)
f.write(b)
f.close()

# 读取二进制文件
f = open('test.dat', 'rb')
a = f.read(4)
print(f"读取的二进制：{a}", a)
a = struct.unpack('f', a)
print(f"转换为Python数据类型：{a}", )
b = f.read(4)
print(f"读取的二进制：{b}", )
b = struct.unpack('4s', b)
print(f"转换为Python数据类型：{b}", )
f.close()
