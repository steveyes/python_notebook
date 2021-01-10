from enum import (
    Enum,
)


class Days(Enum):
    Sun = 1
    Mon = 2
    Tue = 3
    Wed = 4
    Thu = 5
    Fri = 6
    Sat = 7


print(Days.Sun)
print(repr(Days.Mon))
print(type(Days.Tue))
print(isinstance(Days.Wed, Days))
print(Days.Thu.name)
print(Days.Fri.name)

# iteration
for weekday in Days:
    print(weekday)

# access
print(Days(1))
print(Days['Mon'])
