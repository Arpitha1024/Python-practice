"""
myTuple = (15, 7, 32)
#index			0	 1	2
print(myTuple[1])
"""


def getNumbers():
	num1 = int(input("1st number: "))
	num2 = int(input("2nd number: "))
	return (num1, num2)

def add():
	inputs = getNumbers()
	output = inputs[0] + inputs[1] 
	return output

def subtract():
	inputs = getNumbers()
	output = inputs[0] - inputs[1]
	return output 

def multiply():
	inputs = getNumbers()
	output = inputs[0] * inputs[1] 
	return output

def divide():
	inputs = getNumbers()
	output = inputs[0] / inputs[1] 
	return output
	
print("Choose a mathematical operation: \n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division")
choice = input()

"""
if choice == "1":
	print(add())
elif choice == "2":
	print(subtract())
elif choice == "3":
	print(multiply())
elif choice == "4":
	print(divide())
"""

match choice:
	case "1":
		print(add())
	case "2":
		print(subtract())
	case "3":
		print(multiply())
	case "4":
		print(divide())
	case _:
		print("Please enter a valid number!")
