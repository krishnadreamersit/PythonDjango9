class Class1():
    pass
    # varaible (s)
    # function (s)


class Class2():
    # variable
    var1="NA"

    # method/function
    def f1(self):
        print("Hello from f1")


class Class3():
    # Class Variables
    name = "Broadway InfoSys"
    address = "Kathmandu, Nepal"
    tel  = "1234567890"

    def sum(self):
        num1 = int(input("Enter first no : "))
        num2 = int(input("Enter second no : "))
        num3 = num1+num2
        print("Sum : ", num3)


# self - Current Class
class Class4():
    def __init__(self):
        # instance variable
        self.id=0
        self.name="NA"


class Class5():
    def __init__(self, id=0, name="NA"):
        self.id=id # self.id - instance variable and is - parameter
        self.name=name
    def getId(self):
        return self.id
    def getName(self):
        return self.name
    def setId(self, id):
        self.id = id
    def setName(self, name):
        self.name = name
    def __str__(self):
        return str(self.id)+", "+self.name

class Class6():
    def __init__(self, id=0):
        self.id = id
    def setId(self, id):
        self.id=id
    def getId(self):
        return self.id
    def __str__(self):
        return str(self.id)

class Class7():
    def __init__(self, name=""):
        self.name = name
    def setId(self, name):
        self.name=name
    def getId(self):
        return self.name
    def __str__(self):
        return str(self.name)

class Class8(Class6):
    def __init__(self, id=0, name=""):
        Class6.__init__(self, id)
        self.name = name
    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def __str__(self):
        return super().__str__() + ", " + self.name