import struct
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
                   )

    data = points.read_point(f, header.offset_to_point_data,
                             header.point_data_record_format,
                             header.number_of_point_records)

    f.close()

    with open("point.txt", 'a+') as f:
        for item in data:
            f.write(f'{item[0]},{item[1]},{item[2]}\n')
