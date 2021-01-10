import struct
import ctypes

_size = struct.calcsize('hhl')
print(_size)

buff = ctypes.create_string_buffer(_size)

x = struct.pack('hhl', 2, 2, 3)
print(x)
print(struct.unpack('hhl', x))

struct.pack_into('hhl', buff, 0, 2, 2, 3)
print(struct.unpack_from('hhl', buff, 0))
