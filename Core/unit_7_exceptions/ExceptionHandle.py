# Errors
# Example-1
print("Hello")
# print("Hello" # SyntaxError: unexpected EOF while parsing

# Example-2
print(10/2) # 5.0
# print(10/0) # ZeroDivisionError: division by zero

# Example-3
# print(4 + var1 *3) # NameError: name 'var1' is not defined

# Example-4
# print('2' + 2) # TypeError: can only concatenate str (not "int") to str
print('2' + '2')  #22
print(int('2') + 2) # 4

# Handling Errors/Exceptions

# Example-5
import sys
# Declare Variables
try:
    # input, process, output
    pass
except:
    # display error message
    pass
finally:
    # delete all the resources
    pass

# Example-6
import sys
# Declare Variables
num1 = None
num2 = None
num3 = None
try:
    # input, process, output
    num1 = 4
    num2 = 3
    num3 = num1/num2
    print("Result ", num3)
except:
    # display error message
    print("Error : ", sys.exc_info()[1])
finally:
    # delete all the resources
    del (num1)
    del (num2)
    del (num3)

# Example-7
# Handling Multiple Exceptions
import sys
list1 = [10, 2, 0]
try:
    for item in list1:
        print(item)
        result = 1/int(item)
        print(result)
except (ZeroDivisionError, ValueError):
    print("Error : ", sys.exc_info()[1])


# Example-7
# User Defined Exceptions
class MyError(Exception):
    pass

class ValueToSamllError(MyError):
    pass

class ValueToLargeError(MyError):
    pass

num1 = 10
while True:
    try:
        tmp_num = int(input("Enter any number : "))
        if tmp_num<num1:
            raise ValueToSamllError
        elif tmp_num>num1:
            raise ValueToLargeError
        print(tmp_num, " Value is in range")
        break
    except ValueToSamllError:
        print("Value is to small!")
    except ValueToLargeError:
        print("Value is to large!")
    finally:
        del tmp_num