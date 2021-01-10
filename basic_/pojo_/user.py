class User(object):

    def __init__(self) -> None:
        super().__init__()
        self.__name = None
        self.__age = None

    def __hide(self):
        print("hidden method")

    def getname(self):
        return self.__name

    def setname(self, name):
        if len(name) < 3 or len(name) > 8:
            raise ValueError("the length of the user name must be between 3 and 8")
        self.__name = name

    name = property(getname, setname)

    def getage(self):
        return self.__age

    def setage(self, age):
        if age < 18 or age > 70:
            raise ValueError("the range of the user age must be between 18 and 70")
        self.__age = age

    age = property(getage, setage)


if __name__ == '__main__':
    u1 = User()
    u1.name = 'alice'
    u1.age = 19
    print(u1.name)
    print(u1.age)
    u2 = User()
    u2.name = 'al'
    u2.age = 17

