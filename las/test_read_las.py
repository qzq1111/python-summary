"""
使用须知：
1. las点云文件格式文档地址：https://www.asprs.org/divisions-committees/lidar-division/laser-las-file-format-exchange-activities
2. 可以使用包laspy文档地址：https://github.com/laspy/laspy
3. 可以使用包plcpy文档地址：https://github.com/davidcaron/pclpy
4. 具体需求，具体使用。
"""
# coding:utf-8
import struct
import time
from las.head import get_header
from las.point import Point


def get_version(f):
    f.read(24)
    version_major, version_minor = struct.unpack('2B', f.read(2))
    print(f"las版本:{version_major}.{version_minor}")
    return version_major, version_minor


if __name__ == '__main__':
    f = open('test.las', 'rb')
    version = get_version(f)
    header = get_header(f, version)
    print(header.__dict__)

    points = Point(header.x_scale_factor,
                   header.y_scale_factor,
                   header.z_scale_factor,
                   header.x_offset,
                   header.y_offset,
                   header.z_offset,
                   header.point_data_record_format,

                   )
    print("开始测试读取点数据")
    write_start = time.time()
    data = points.read_point(f,
                             header.offset_to_point_data,
                             header.number_of_point_records,
                             )

    f.close()
    write_end = time.time()

    with open("point.txt", 'a+') as f:
        f.writelines(data)
    print(f"完成消耗时间:{write_end - write_start}")
