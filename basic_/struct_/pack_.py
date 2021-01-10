import struct

# h is short in C type
# l is long in C type
# 'hhl' stands for 'short short long'
var = struct.pack('hhl', *[1, 2, 3])
print(var)

# i is int in C type
# 'iii' stands for 'int int int'
var = struct.pack('iii', *[1, 2, 3])
print(var)
