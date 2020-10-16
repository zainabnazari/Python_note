number = 24352
if(number == 0):
	print(number, "is 0") #This line is only run if the condition in the if-statement is true.
elif(number % 2 == 0):
	print(number, "is an even number") #This line is only run if the condition in the elif-statement is true and the condition in the if statement (and any possible elif statements before this) is false.
else:
	print(number, "is an odd number") #This line is only run if the conditions in the if and the elif statements are all false.