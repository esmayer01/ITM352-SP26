# Ethan Mayer
# March 3, 2026

n = int(input("Enter a number: "))
Range = range(1, n + 1)
for i in Range:
	if i % 3 == 0 and i % 5 == 0:
		print("FizzBuzz")
	elif i % 3 == 0:
		print("Fizz")
	elif i % 5 == 0:
		print("Buzz")
	else:
		print(i)