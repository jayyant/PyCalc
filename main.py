loopcode = True

while loopcode:
	print("Welcome to calculator 3000!\n Please enter two numbers to perform operations on them.")
	print("Enter your operation below:\n1 - Addition\t2 - Substraction\t3 - Multiplication\t4 - Division\t5 - Exit")
	c = int(input())

	if c == 5:
		loopcode = False
		break

	a = int(input("Enter first number: "))
	b = int(input("Enter second number: "))

	if c == 1:
		sum = a + b
		sumstring = "Sum of {} and {} is: {}"
		print(sumstring.format(a,b,sum))
	elif c == 2:
		sub = a - b
		substring = "Difference of {} and {} is: {}"
		print(substring.format(a,b,sub))
	elif c == 3:
		mul = a*b
		mulstring = "Multiplication of {} and {} is: {}"
		print(mulstring.format(a,b,mul))
	elif c == 4:
		div = a/b
		divstring = "Division of {} and {} is: {}"
		print(divstring.format(a,b,div))
	else:
		print("Invalid option!")





