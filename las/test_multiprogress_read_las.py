# coding:utf-8
import math
import mmap
import multiprocessing
import os
import struct
import time

from las.head import get_header
from las.point import Point


def get_version(f):
    """
    获取版本号
    :param f:
    :return:
    """
    f.read(24)
    version_major, version_minor = struct.unpack('2B', f.read(2))
    print(f"las版本:{version_major}.{version_minor}")
    return version_major, version_minor


def open_file(file_name):
    """
    将文件映射到内存
    :param file_name:
    :return:
    """
    fd = os.open(file_name, os.O_RDONLY)
    f = mmap.mmap(fd, 0, access=mmap.ACCESS_READ)
    return f


def get_interval_data(number_point, split_number=1000):
    """
    一个进程一次性处理多少点
    :param number_point: 总数据量
    :param split_number: 每段数据量
    :return:
    """
    num = math.ceil(number_point / split_number)

    data = []

    for item in range(num):
        t1 = item * split_number
        t2 = (item + 1) * split_number
        if t2 > number_point:
            data.append((t1, number_point))
            break
        data.append((t1, t2))
    return data


def read_point(file_name, offset_data, interval, point_format,
               x_s_f, y_s_f, z_s_f, x_o, y_o, z_o, ):
    """
    读取点数据
    :param file_name: 文件名
    :param offset_data: 文件开始位置
    :param interval: 点间隔
    :param point_format: 点数据格式
    :param x_s_f: x刻度因子
    :param y_s_f: y刻度因子
    :param z_s_f: z刻度因子
    :param x_o: x偏移量
    :param y_o: y偏移量
    :param z_o: z偏移量
    :return:
    """
    lower_interval, upper_interval = interval

    point = Point(x_s_f,
                  y_s_f,
                  z_s_f,
                  x_o,
                  y_o,
                  z_o,
                  point_format
                  )

    num = upper_interval - lower_interval
    lower_interval = offset_data + lower_interval * (point.offset_bytes + 12)
    f = open_file(file_name)
    print("开始测试读取点数据")
    start = time.time()
    data = point.read_point(f, lower_interval, num)
    end = time.time()
    print(f"完成消耗时间:{end - start}")
    f.close()
    return data


def write_file(data):
    """
    输出到文件
    :param data:
    :return:
    """
    with open("point1.txt", 'a+') as f:
        f.writelines(data)


if __name__ == '__main__':
    file_name = 'test.las'
    f = open_file(file_name)
    version = get_version(f)
    header = get_header(f, version)
    f.close()

    print(header.__dict__)

    interval_data = get_interval_data(header.number_of_point_records, 10000)
    pool = multiprocessing.Pool(multiprocessing.cpu_count())

    print("开始测试读取点数据")
    write_start = time.time()
    for item in interval_data:
        pool.apply_async(read_point,
                         args=(file_name,
                               header.offset_to_point_data,
                               item,
                               header.point_data_record_format,
                               header.x_scale_factor,
                               header.y_scale_factor,
                               header.z_scale_factor,
                               header.x_offset,
                               header.y_offset,
                               header.z_offset,
                               ),
                         callback=write_file
                         )

    pool.close()
    pool.join()
    write_end = time.time()
    print(f"完成消耗时间:{write_end - write_start}")
