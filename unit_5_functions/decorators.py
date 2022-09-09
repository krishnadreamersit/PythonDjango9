# https://www.programiz.com/python-programming/decorator

# function as parameter
def inc(x):
	return x+1

def operate(func, x):
	result = func(x)
	return result

#print(operate(inc, 3))

# inner function-1
def outer_function1(message):
	title="Hello"
	def inner_function():
		print(title, message)
	inner_function()

#outer_function1("Hi")

# inner function-2
def outer_function2(message):
	title="Hello"
	def inner_function2():
		print(title, message)
	return inner_function2

func2 = outer_function2("Hi")
func2()
