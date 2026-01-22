# An example of creating and user your own function
# Name: Ethan Mayer
# Date: Jan. 22, 2026

def greet(name):
    """This function greets the person whose name is passed in.
    In addition we want to print a welcome message that includes
    the day of the week"""
    message = "Hello" + " " + name + "!"
    return message

user_name = input("Please enter your name: ")
greeting_message = greet(user_name)
print(greeting_message)
