import struct

var = struct.pack('?hil', True, 2, 5, 445)
print(var)
print(struct.calcsize('?hil'))
print(struct.calcsize('?qf'))
