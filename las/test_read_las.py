import struct


class OneZeroHeader(object):

    def __init__(self):
        self.file_signature = None  # 文件签名
        self.reserved = None  # 预留字段
        self.guid_1 = None  # 项目ID1
        self.guid_2 = None  # 项目ID2
        self.guid_3 = None  # 项目ID3
        self.guid_4 = None  # 项目ID4
        self.version_major = None  # 大版本
        self.version_minor = None  # 小版本
        self.system_identifier = None  # 硬件信息
        self.generating_software = None  # 软件信息
        self.flight_date_julian = None  # 文件创建天数
        self.year = None  # 文件创建年份
        self.header_size = None  # 头文件大小
        self.offset_to_data = None  # 点数据记录起始位置
        self.number_of_variable_length_records = None  # 可变数据记录长度
        self.point_data_record_format = None  # 点数据记录格式
        self.point_data_record_length = None  # 点数据记录长度
        self.number_of_point_records = None  # 总共的点数量
        self.number_of_points_by_return = None  # 回波点数量
        self.x_scale_factor = None  # x比例因子
        self.y_scale_factor = None  # y比例因子
        self.z_scale_factor = None  # z比例因子
        self.x_offset = None  # x偏移量
        self.y_offset = None  # y偏移量
        self.z_offset = None  # z偏移量
        self.max_x = None  # x最大值
        self.min_x = None  # x最小值
        self.max_y = None  # y最大值
        self.min_y = None  # y最小值
        self.max_z = None  # z最大值
        self.min_z = None  # z最小值

    def read_header(self, f):
        """
        读取头
        :param f:
        :return:
        """
        f.seek(0)
        self.file_signature = f.read(4).decode("utf-8")
        self.reserved = struct.unpack('L', f.read(4))[0]
        self.guid_1 = struct.unpack('L', f.read(4))[0]
        self.guid_2 = struct.unpack('H', f.read(2))[0]
        self.guid_3 = struct.unpack('H', f.read(2))[0]
        self.guid_4 = struct.unpack('8s', f.read(8))[0].decode("utf-8")
        self.version_major = struct.unpack('B', f.read(1))[0]
        self.version_minor = struct.unpack('B', f.read(1))[0]
        self.system_identifier = struct.unpack('32s', f.read(32))[0].decode("utf-8")
        self.generating_software = struct.unpack('32s', f.read(32))[0].decode("utf-8")
        self.flight_date_julian = struct.unpack('H', f.read(2))[0]
        self.year = struct.unpack('H', f.read(2))[0]
        self.header_size = struct.unpack('H', f.read(2))[0]
        self.offset_to_data = struct.unpack('L', f.read(4))[0]
        self.number_of_variable_length_records = struct.unpack('L', f.read(4))[0]
        self.point_data_record_format = struct.unpack('B', f.read(1))[0]
        self.point_data_record_length = struct.unpack('H', f.read(2))[0]
        self.number_of_point_records = struct.unpack('L', f.read(4))[0]
        self.number_of_points_by_return = struct.unpack('5L', f.read(20))[0]
        self.x_scale_factor = struct.unpack('d', f.read(8))[0]
        self.y_scale_factor = struct.unpack('d', f.read(8))[0]
        self.z_scale_factor = struct.unpack('d', f.read(8))[0]
        self.x_offset = struct.unpack('d', f.read(8))[0]
        self.y_offset = struct.unpack('d', f.read(8))[0]
        self.z_offset = struct.unpack('d', f.read(8))[0]
        self.max_x = struct.unpack('d', f.read(8))[0]
        self.min_x = struct.unpack('d', f.read(8))[0]
        self.max_y = struct.unpack('d', f.read(8))[0]
        self.min_y = struct.unpack('d', f.read(8))[0]
        self.max_z = struct.unpack('d', f.read(8))[0]
        self.min_z = struct.unpack('d', f.read(8))[0]


class OneOneHeader(object):

    def __init__(self):
        self.file_signature = None  # 文件签名
        self.file_source_id = None  # 文件ID
        self.reserved = None  # 预留字段
        self.project_id_1 = None  # 项目ID1
        self.project_id_2 = None  # 项目ID2
        self.project_id_3 = None  # 项目ID3
        self.project_id_4 = None  # 项目ID4
        self.version_major = None  # 大版本
        self.version_minor = None  # 小版本
        self.system_identifier = None  # 硬件信息
        self.generating_software = None  # 软件信息
        self.file_creation_day_of_year = None  # 文件创建天数
        self.file_creation_year = None  # 文件创建年份
        self.header_size = None  # 头文件大小
        self.offset_to_point_data = None  # 点数据记录起始位置
        self.number_of_variable_length_records = None  # 可变数据记录长度
        self.point_data_record_format = None  # 点数据记录格式
        self.point_data_record_length = None  # 点数据记录长度
        self.number_of_point_records = None  # 总共的点数量
        self.number_of_points_by_return = None  # 回波点数量
        self.x_scale_factor = None  # x比例因子
        self.y_scale_factor = None  # y比例因子
        self.z_scale_factor = None  # z比例因子
        self.x_offset = None  # x偏移量
        self.y_offset = None  # y偏移量
        self.z_offset = None  # z偏移量
        self.max_x = None  # x最大值
        self.min_x = None  # x最小值
        self.max_y = None  # y最大值
        self.min_y = None  # y最小值
        self.max_z = None  # z最大值
        self.min_z = None  # z最小值

    def read_header(self, f):
        f.seek(0)
        self.file_signature = f.read(4).decode("utf-8")
        self.file_source_id = struct.unpack('H', f.read(2))[0]
        self.reserved = struct.unpack('H', f.read(2))[0]
        self.project_id_1 = struct.unpack('L', f.read(4))[0]
        self.project_id_2 = struct.unpack('H', f.read(2))[0]
        self.project_id_3 = struct.unpack('H', f.read(2))[0]
        self.project_id_4 = struct.unpack('8s', f.read(8))[0].decode("utf-8")
        self.version_major = struct.unpack('B', f.read(1))[0]
        self.version_minor = struct.unpack('B', f.read(1))[0]
        self.system_identifier = struct.unpack('32s', f.read(32))[0].decode("utf-8")
        self.generating_software = struct.unpack('32s', f.read(32))[0].decode("utf-8")
        self.file_creation_day_of_year = struct.unpack('H', f.read(2))[0]
        self.file_creation_year = struct.unpack('H', f.read(2))[0]
        self.header_size = struct.unpack('H', f.read(2))[0]
        self.offset_to_point_data = struct.unpack('L', f.read(4))[0]
        self.number_of_variable_length_records = struct.unpack('L', f.read(4))[0]
        self.point_data_record_format = struct.unpack('B', f.read(1))[0]
        self.point_data_record_length = struct.unpack('H', f.read(2))[0]
        self.number_of_point_records = struct.unpack('L', f.read(4))[0]
        self.number_of_points_by_return = struct.unpack('5L', f.read(20))[0]
        self.x_scale_factor = struct.unpack('d', f.read(8))[0]
        self.y_scale_factor = struct.unpack('d', f.read(8))[0]
        self.z_scale_factor = struct.unpack('d', f.read(8))[0]
        self.x_offset = struct.unpack('d', f.read(8))[0]
        self.y_offset = struct.unpack('d', f.read(8))[0]
        self.z_offset = struct.unpack('d', f.read(8))[0]
        self.max_x = struct.unpack('d', f.read(8))[0]
        self.min_x = struct.unpack('d', f.read(8))[0]
        self.max_y = struct.unpack('d', f.read(8))[0]
        self.min_y = struct.unpack('d', f.read(8))[0]
        self.max_z = struct.unpack('d', f.read(8))[0]
        self.min_z = struct.unpack('d', f.read(8))[0]


class OneTwoHeader(object):
    def __init__(self):
        self.file_signature = None  # 文件签名
        self.file_source_id = None  # 文件ID
        self.global_encoding = None  # 全球编码
        self.project_id_1 = None  # 项目ID1
        self.project_id_2 = None  # 项目ID2
        self.project_id_3 = None  # 项目ID3
        self.project_id_4 = None  # 项目ID4
        self.version_major = None  # 大版本
        self.version_minor = None  # 小版本
        self.system_identifier = None  # 硬件信息
        self.generating_software = None  # 软件信息
        self.file_creation_day_of_year = None  # 文件创建天数
        self.file_creation_year = None  # 文件创建年份
        self.header_size = None  # 头文件大小
        self.offset_to_point_data = None  # 点数据记录起始位置
        self.number_of_variable_length_records = None  # 可变数据记录长度
        self.point_data_record_format = None  # 点数据记录格式
        self.point_data_record_length = None  # 点数据记录长度
        self.number_of_point_records = None  # 总共的点数量
        self.number_of_points_by_return = None  # 回波点数量
        self.x_scale_factor = None  # x比例因子
        self.y_scale_factor = None  # y比例因子
        self.z_scale_factor = None  # z比例因子
        self.x_offset = None  # x偏移量
        self.y_offset = None  # y偏移量
        self.z_offset = None  # z偏移量
        self.max_x = None  # x最大值
        self.min_x = None  # x最小值
        self.max_y = None  # y最大值
        self.min_y = None  # y最小值
        self.max_z = None  # z最大值
        self.min_z = None  # z最小值

    def read_header(self, f):
        f.seek(0)
        self.file_signature = f.read(4).decode("utf-8")
        self.file_source_id = struct.unpack('H', f.read(2))[0]
        self.global_encoding = struct.unpack('H', f.read(2))[0]
        self.project_id_1 = struct.unpack('L', f.read(4))[0]
        self.project_id_2 = struct.unpack('H', f.read(2))[0]
        self.project_id_3 = struct.unpack('H', f.read(2))[0]
        self.project_id_4 = struct.unpack('8s', f.read(8))[0].decode("utf-8")
        self.version_major = struct.unpack('B', f.read(1))[0]
        self.version_minor = struct.unpack('B', f.read(1))[0]
        self.system_identifier = struct.unpack('32s', f.read(32))[0].decode("utf-8")
        self.generating_software = struct.unpack('32s', f.read(32))[0].decode("utf-8")
        self.file_creation_day_of_year = struct.unpack('H', f.read(2))[0]
        self.file_creation_year = struct.unpack('H', f.read(2))[0]
        self.header_size = struct.unpack('H', f.read(2))[0]
        self.offset_to_point_data = struct.unpack('L', f.read(4))[0]
        self.number_of_variable_length_records = struct.unpack('L', f.read(4))[0]
        self.point_data_record_format = struct.unpack('B', f.read(1))[0]
        self.point_data_record_length = struct.unpack('H', f.read(2))[0]
        self.number_of_point_records = struct.unpack('L', f.read(4))[0]
        self.number_of_points_by_return = struct.unpack('5L', f.read(20))[0]
        self.x_scale_factor = struct.unpack('d', f.read(8))[0]
        self.y_scale_factor = struct.unpack('d', f.read(8))[0]
        self.z_scale_factor = struct.unpack('d', f.read(8))[0]
        self.x_offset = struct.unpack('d', f.read(8))[0]
        self.y_offset = struct.unpack('d', f.read(8))[0]
        self.z_offset = struct.unpack('d', f.read(8))[0]
        self.max_x = struct.unpack('d', f.read(8))[0]
        self.min_x = struct.unpack('d', f.read(8))[0]
        self.max_y = struct.unpack('d', f.read(8))[0]
        self.min_y = struct.unpack('d', f.read(8))[0]
        self.max_z = struct.unpack('d', f.read(8))[0]
        self.min_z = struct.unpack('d', f.read(8))[0]


class OneThreeHeader(object):
    def __init__(self):
        self.file_signature = None  # 文件签名
        self.file_source_id = None  # 文件ID
        self.global_encoding = None  # 全球编码
        self.project_id_1 = None  # 项目ID1
        self.project_id_2 = None  # 项目ID2
        self.project_id_3 = None  # 项目ID3
        self.project_id_4 = None  # 项目ID4
        self.version_major = None  # 大版本
        self.version_minor = None  # 小版本
        self.system_identifier = None  # 硬件信息
        self.generating_software = None  # 软件信息
        self.file_creation_day_of_year = None  # 文件创建天数
        self.file_creation_year = None  # 文件创建年份
        self.header_size = None  # 头文件大小
        self.offset_to_point_data = None  # 点数据记录起始位置
        self.number_of_variable_length_records = None  # 可变数据记录长度
        self.point_data_record_format = None  # 点数据记录格式
        self.point_data_record_length = None  # 点数据记录长度
        self.number_of_point_records = None  # 总共的点数量
        self.number_of_points_by_return = None  # 回波点数量
        self.x_scale_factor = None  # x比例因子
        self.y_scale_factor = None  # y比例因子
        self.z_scale_factor = None  # z比例因子
        self.x_offset = None  # x偏移量
        self.y_offset = None  # y偏移量
        self.z_offset = None  # z偏移量
        self.max_x = None  # x最大值
        self.min_x = None  # x最小值
        self.max_y = None  # y最大值
        self.min_y = None  # y最小值
        self.max_z = None  # z最大值
        self.min_z = None  # z最小值
        self.start_of_waveform_data_packet_record = None  # 波形数据包记录的开始位置

    def read_header(self, f):
        f.seek(0)
        self.file_signature = f.read(4).decode("utf-8")
        self.file_source_id = struct.unpack('H', f.read(2))[0]
        self.global_encoding = struct.unpack('H', f.read(2))[0]
        self.project_id_1 = struct.unpack('L', f.read(4))[0]
        self.project_id_2 = struct.unpack('H', f.read(2))[0]
        self.project_id_3 = struct.unpack('H', f.read(2))[0]
        self.project_id_4 = struct.unpack('8s', f.read(8))[0].decode("utf-8")
        self.version_major = struct.unpack('B', f.read(1))[0]
        self.version_minor = struct.unpack('B', f.read(1))[0]
        self.system_identifier = struct.unpack('32s', f.read(32))[0].decode("utf-8")
        self.generating_software = struct.unpack('32s', f.read(32))[0].decode("utf-8")
        self.file_creation_day_of_year = struct.unpack('H', f.read(2))[0]
        self.file_creation_year = struct.unpack('H', f.read(2))[0]
        self.header_size = struct.unpack('H', f.read(2))[0]
        self.offset_to_point_data = struct.unpack('L', f.read(4))[0]
        self.number_of_variable_length_records = struct.unpack('L', f.read(4))[0]
        self.point_data_record_format = struct.unpack('B', f.read(1))[0]
        self.point_data_record_length = struct.unpack('H', f.read(2))[0]
        self.number_of_point_records = struct.unpack('L', f.read(4))[0]
        self.number_of_points_by_return = struct.unpack('5L', f.read(20))[0]
        self.x_scale_factor = struct.unpack('d', f.read(8))[0]
        self.y_scale_factor = struct.unpack('d', f.read(8))[0]
        self.z_scale_factor = struct.unpack('d', f.read(8))[0]
        self.x_offset = struct.unpack('d', f.read(8))[0]
        self.y_offset = struct.unpack('d', f.read(8))[0]
        self.z_offset = struct.unpack('d', f.read(8))[0]
        self.max_x = struct.unpack('d', f.read(8))[0]
        self.min_x = struct.unpack('d', f.read(8))[0]
        self.max_y = struct.unpack('d', f.read(8))[0]
        self.min_y = struct.unpack('d', f.read(8))[0]
        self.max_z = struct.unpack('d', f.read(8))[0]
        self.min_z = struct.unpack('d', f.read(8))[0]
        self.start_of_waveform_data_packet_record = struct.unpack('Q', f.read(8))[0]


class OneFourHeader(object):

    def __init__(self):
        self.file_signature = None  # 文件签名
        self.file_source_id = None  # 文件ID
        self.global_encoding = None  # 全球编码
        self.project_id_1 = None  # 项目ID1
        self.project_id_2 = None  # 项目ID2
        self.project_id_3 = None  # 项目ID3
        self.project_id_4 = None  # 项目ID4
        self.version_major = None  # 大版本
        self.version_minor = None  # 小版本
        self.system_identifier = None  # 硬件信息
        self.generating_software = None  # 软件信息
        self.file_creation_day_of_year = None  # 文件创建天数
        self.file_creation_year = None  # 文件创建年份
        self.header_size = None  # 头文件大小
        self.offset_to_point_data = None  # 点数据记录起始位置
        self.number_of_variable_length_records = None  # 可变数据记录长度
        self.point_data_record_format = None  # 点数据记录格式
        self.point_data_record_length = None  # 点数据记录长度
        self.legacy_number_of_point_records = None  # 老格式总共的点数量
        self.legacy_number_of_points_by_return = None  # 老格式回波点数量
        self.x_scale_factor = None  # x比例因子
        self.y_scale_factor = None  # y比例因子
        self.z_scale_factor = None  # z比例因子
        self.x_offset = None  # x偏移量
        self.y_offset = None  # y偏移量
        self.z_offset = None  # z偏移量
        self.max_x = None  # x最大值
        self.min_x = None  # x最小值
        self.max_y = None  # y最大值
        self.min_y = None  # y最小值
        self.max_z = None  # z最大值
        self.min_z = None  # z最小值
        self.start_of_waveform_data_packet_record = None  # 波形数据记录起始点
        self.start_of_first_extended_variable_length_record = None  # 扩展变长记录起始
        self.number_of_extended_variable_length_records = None  # 扩展变长记录数目
        self.number_of_point_records = None  # 点记录总数
        self.number_of_points_by_return = None  # 回波点数量

    def read_header(self, f):
        self.file_signature = f.read(4).decode("utf-8")
        self.file_source_id = struct.unpack('H', f.read(2))[0]
        self.global_encoding = struct.unpack('H', f.read(2))[0]
        self.project_id_1 = struct.unpack('L', f.read(4))[0]
        self.project_id_2 = struct.unpack('H', f.read(2))[0]
        self.project_id_3 = struct.unpack('H', f.read(2))[0]
        self.project_id_4 = struct.unpack('8s', f.read(8))[0].decode("utf-8")
        self.version_major = struct.unpack('B', f.read(1))[0]
        self.version_minor = struct.unpack('B', f.read(1))[0]
        self.system_identifier = struct.unpack('32s', f.read(32))[0].decode("utf-8")
        self.generating_software = struct.unpack('32s', f.read(32))[0].decode("utf-8")
        self.file_creation_day_of_year = struct.unpack('H', f.read(2))[0]
        self.file_creation_year = struct.unpack('H', f.read(2))[0]
        self.header_size = struct.unpack('H', f.read(2))[0]
        self.offset_to_point_data = struct.unpack('L', f.read(4))[0]
        self.number_of_variable_length_records = struct.unpack('L', f.read(4))[0]
        self.point_data_record_format = struct.unpack('B', f.read(1))[0]
        self.point_data_record_length = struct.unpack('H', f.read(2))[0]
        self.legacy_number_of_point_records = struct.unpack('L', f.read(4))[0]
        self.legacy_number_of_points_by_return = struct.unpack('5L', f.read(20))[0]
        self.x_scale_factor = struct.unpack('d', f.read(8))[0]
        self.y_scale_factor = struct.unpack('d', f.read(8))[0]
        self.z_scale_factor = struct.unpack('d', f.read(8))[0]
        self.x_offset = struct.unpack('d', f.read(8))[0]
        self.y_offset = struct.unpack('d', f.read(8))[0]
        self.z_offset = struct.unpack('d', f.read(8))[0]
        self.max_x = struct.unpack('d', f.read(8))[0]
        self.min_x = struct.unpack('d', f.read(8))[0]
        self.max_y = struct.unpack('d', f.read(8))[0]
        self.min_y = struct.unpack('d', f.read(8))[0]
        self.max_z = struct.unpack('d', f.read(8))[0]
        self.min_z = struct.unpack('d', f.read(8))[0]
        self.start_of_waveform_data_packet_record = struct.unpack('Q', f.read(8))[0]
        self.start_of_first_extended_variable_length_record = struct.unpack('Q', f.read(8))[0]
        self.number_of_extended_variable_length_records = struct.unpack('L', f.read(4))[0]
        self.number_of_point_records = struct.unpack('Q', f.read(8))[0]
        self.number_of_points_by_return = struct.unpack('15Q', f.read(120))[0]


def head(version):
    if version == (1, 0):
        return OneZeroHeader()
    elif version == (1, 1):
        return OneOneHeader()
    elif version == (1, 2):
        return OneTwoHeader()
    elif version == (1, 3):
        return OneThreeHeader()
    elif version == (1, 4):
        return OneFourHeader()
    else:
        return False


def get_version(f):
    f.read(24)
    version_major, version_minor = struct.unpack('2B', f.read(2))
    print(f"las版本:{version_major}.{version_minor}")
    return version_major, version_minor


def get_header(f, version):
    if version == (1, 0):
        new_header = OneZeroHeader()
    elif version == (1, 1):
        new_header = OneOneHeader()
    elif version == (1, 2):
        new_header = OneTwoHeader()
    elif version == (1, 3):
        new_header = OneThreeHeader()
    elif version == (1, 4):
        new_header = OneFourHeader()
    else:
        raise Exception("未找到对应文件版本")

    new_header.read_header(f)
    return new_header


if __name__ == '__main__':
    f = open('test.las', 'rb')
    version = get_version(f)
    header = get_header(f, version)
    print(header.__dict__)
