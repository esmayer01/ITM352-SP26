# Ethan Mayer
# March 3, 2026

searchMe = [ 2, 5, 7, 11, 15, 22, 27, 30, 34, 41, 55, 57, 58, 60, 77]

number = int(input("Enter a number to search for: "))
if number in searchMe:
	print(f"{number} exists in the array.")
else:
	print(f"{number} does not exist in the array.")