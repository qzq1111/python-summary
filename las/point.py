"""
定义点数据0~10格式解析
"""
import struct


class Point(object):

    def __init__(self, x_s_f, y_s_f, z_s_f, x_o, y_o, z_o, point_format):
        self.x_scale_factor = x_s_f
        self.y_scale_factor = y_s_f
        self.z_scale_factor = z_s_f
        self.x_offset = x_o
        self.y_offset = y_o
        self.z_offset = z_o
        self.offset_bytes = self.get_offset_bytes(point_format)

    def get_offset_bytes(self, point_format):
        """
        根据不同的点格式跳过的字节数
        :param point_format:点格式0~10
        :return:
        """
        # x,y,z共占12字节
        data_format = {
            0: 8,  # 点格式0 共20字节
            1: 16,  # 点格式1 共28字节
            2: 14,  # 点格式2 共26字节
            3: 22,  # 点格式3 共34字节
            4: 45,  # 点格式4 共57字节
            5: 51,  # 点格式5 共63字节
            6: 18,  # 点格式6 共30字节
            7: 24,  # 点格式7 共36字节
            8: 26,  # 点格式8 共38字节
            9: 47,  # 点格式9 共59字节
            10: 55,  # 点格式10 共67字节
        }

        offset_bytes = data_format.get(point_format, None)
        if offset_bytes is None:
            raise Exception(f"不存在当前的点格式{point_format}")
        return offset_bytes

    def read_point(self, f, offset_to_point_data, num):
        """
        读取当前文件中的点数据
        :param f:  数据文件
        :param offset_to_point_data: 点数据开始读取的地方
        :param num: 读取多少个点
        :return: 读取的数据点
        """
        f.seek(offset_to_point_data)
        points = list()
        i = 0
        while i < num:
            point_bytes = f.read(12 + self.offset_bytes)
            x_record, y_record, z_record = struct.unpack_from('3l', point_bytes[:12])
            x = x_record * self.x_scale_factor + self.x_offset
            y = y_record * self.y_scale_factor + self.y_offset
            z = z_record * self.z_scale_factor + self.z_offset
            i += 1
            points.append(f'{x}, {y}, {z}\n')

        return points
