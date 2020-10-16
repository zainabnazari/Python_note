# file name: input.py
#We want to ask a number from the user and print the number multiplied by 2
a = input("What is your number?") # The console prints "What is your number?" and waits for the user to enter something and press ENTER
print(a * 2) # This only prints the input twice, but doesn't do multiplication. The reason is that input returns a string.
print(int(a) * 2) # So we need to convert a to an integer. We do that using the function int(). Now it works!
