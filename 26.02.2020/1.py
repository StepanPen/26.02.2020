def arithmetic (x, y, z):
	if z == "+" :
		return (x + y)
	elif z == "-":
		return (x - y)
	elif z == "*":
		return (x * y)
	elif z == "/":
		return (x / y)
	else :
		return ("Invalid operation")
print (arithmetic(2, 3, '+'))
print (arithmetic(2, 2, '*'))
print (arithmetic(4, 2, '-'))
print (arithmetic(4, 2, '/'))
print (arithmetic(4, 2, 0))


