import grp

print(grp.getgrnam('root'))
print(grp.getgrgid(0))
[print(g) for g in grp.getgrall()]
