# coding:utf-8
import math
import multiprocessing
import time
import mmap
import os


# ----------------生成测试文件---------------#
def build_txt(file, number):
    """
    生成测试数据文件
    :return:
    """

    data = ["1"] * number
    with open(file, 'w') as f:
        f.writelines(data)


# ----------------顺序读取文件---------------#
def next_read(file, number):
    """
    顺序读取文件
    :param file:
    :return:
    """
    start_time = time.time()
    print("开始顺序读取数据")
    i = 0
    with open(file, 'r') as f:
        while i < number:
            f.read()
            i += 1
    end_time = time.time()
    print(f"读取完成耗时：{end_time - start_time}")


# ----------------多进程读取文件---------------#
def read(file_name, start, end):
    i = start
    with open(file_name, 'r') as f:
        f.seek(start)
        while i < end:
            f.read()
            i += 1


def get_interval_data(number, split_number=10000):
    """
    一个进程一次性处理多少点
    :return:
    """
    num = math.ceil(number / split_number)
    data = []
    for item in range(num):
        t1 = item * split_number
        t2 = (item + 1) * split_number
        if t2 > number:
            data.append((t1, number))
            break
        data.append((t1, t2))
    return data


def pro_read(file, number):
    """
    多进程读取文件
    """

    pool = multiprocessing.Pool(3)

    print("开始多进程读取数据")
    start_time = time.time()
    for item in get_interval_data(number):
        pool.apply_async(read, args=(file, item[0], item[1]))

    pool.close()
    pool.join()
    end_time = time.time()
    print(f"读取完成耗时：{end_time - start_time}")


# ----------------内存映射方式多进程读取文件---------------#
def open_file(file):
    """
    内存映射文件
    """
    fd = os.open(file, os.O_RDONLY)
    f = mmap.mmap(fd, 0, access=mmap.ACCESS_READ)
    return f


def mmap_read(file, start, end):
    i = start
    f = open_file(file)
    f.seek(start)
    while i < end:
        f.read()
        i += 1
    f.close()


def pro_mmap_read(file, number):
    """
    使用内存映射多进程读取文件
    """

    pool = multiprocessing.Pool(multiprocessing.cpu_count())

    print("开始内存映射多进程读取数据")
    start_time = time.time()
    for item in get_interval_data(number):
        pool.apply_async(mmap_read, args=(file, item[0], item[1]))

    pool.close()
    pool.join()
    end_time = time.time()
    print(f"读取完成耗时：{end_time - start_time}")


# ----------------测试---------------#
if __name__ == '__main__':
    file = "test.txt"
    number = 200000
    # 构建测试数据
    build_txt(file, number)
    # 顺序对齐
    next_read(file, number)
    # 多进程读取
    pro_read(file, number)
    # 内存映射多进程读取
    pro_mmap_read(file, number)
