import struct

# '?' -> _BOOL
# 'h' -> short
# 'i' -> int
# 'l' -> long
var = struct.pack('?hil', True, 2, 5, 445)
print(var)

tup = struct.unpack('?hil', var)
print(tup)

# q -> long long int
# f -> float
var = struct.pack('qf', 5, 2.3)
print(var)

tup = struct.unpack('qf', var)
print(tup)
