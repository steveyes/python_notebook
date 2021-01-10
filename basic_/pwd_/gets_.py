import pwd

pwname = pwd.getpwnam('root')
print(pwname)

pwuid = pwd.getpwuid(0)
print(pwuid)

pwall = pwd.getpwall()
[print(pw) for pw in pwd.getpwall()]
