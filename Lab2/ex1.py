# ask the user for a number between 1 and 100. Square the number and print the number and its square. 
# Name: Ethan Mayer
# Date: Jan. 20, 2026

print("Welcome to the program")
valued_entered = input("Please enter a number between 1 and 100: ")
print("You entered:", valued_entered)

value_as_interger = int(valued_entered)
squared_value = value_as_interger ** 2
print("The square of", valued_entered, "is", squared_value)
print(f"The square of {valued_entered} is {squared_value}")