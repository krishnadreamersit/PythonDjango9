# Testing a Function
"""
# import function/resources
from unit_5_functions.MyFunctions import *

# Call a function
#for i in range(100):
#    hello()

str1 = "Kathmandu, Nepal"
print_message(str1)
str1 = "Krishna Aryal"
print_message(str1)

print_messages("NAME : ", "Krishna Aryal")
"""

# Class
from unit_6_oops.MyClasses import Class1
from unit_6_oops.MyClasses import Class2
from unit_6_oops.MyClasses import Class3
from unit_6_oops.MyClasses import Class4
from unit_6_oops.MyClasses import Class5
from unit_6_oops.MyClasses import Class6
from unit_6_oops.MyClasses import Class7
from unit_6_oops.MyClasses import Class8

"""
# Declare an object of Class1
obj1 = Class1()
print(type(obj1)) # <class 'unit_6_oops.MyClasses.Class1'>
print(id(obj1))
# print(len(obj1)) # TypeError: object of type 'Class1' has no len()
obj2 = obj1
print(id(obj2))

obj3 = Class2() # object declare and initialize
print(obj3.var1)  # Access class varaible
obj3.f1() # Call class method

obj4 = Class2()
print(obj4.var1)
obj4.f1()

obj5 = Class3()
obj6 = Class3()
obj7 = Class3()

print(obj5.name, obj5.address, obj5.tel)
print(obj6.name, obj6.address, obj6.tel)
print(obj7.name, obj7.address, obj7.tel)

obj5.name="ABC College"
print(obj5.name)
print(obj6.name)
print(obj7.name)

obj04 = Class4() # decalre and initialize
obj04.id=1 # Update
obj04.name="Raj Rai" # Update
print(obj04.id, obj04.name) # Access value

obj05 = Class5(1, "Rajan Thapa")
print(obj05.id, obj05.name)

obj05.setId(2)# Setter is used to update the value
obj05.setName("Raju Limbu") # Setter
print(obj05.getId(), obj05.getName()) # Getter is used to get value from instance varaible

obj05_1 = Class5()
print(obj05_1)
obj05_1 = Class5(3, "Ramesh Thapa")
print(obj05_1)

obj06_1 = Class6(1)
obj07_1 = Class7("Raj Rai")
print(obj06_1, obj07_1)
"""

obj08_1 = Class8(1, "Kiran Thapa Magar")
print(obj08_1)