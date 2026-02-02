# string manipulation examples
# Name: Ethan Mayer
# Date: Jan. 29, 2026

first = input("Enter your first name: ")
middleIn = input("Enter your middle name (or press Enter if none): ")
last = input("Enter your last name: ")

# full_name = first + " " + middleIn + " " + last
# print(f"Your full name is: {full_name}")

print(f"Your full name is: {first} {middleIn} {last}")

# full_name = "%s %s %s" % (first, middleIn, last)
# print("Your full name is: %s" % full_name)

# full_name = "{} {} {}".format(first, middleIn, last)
# print("Your full name is: {}".format(full_name))

# full_name = " ".join([first, middleIn, last])
# print("Your full name is:", full_name)

name_parts = [first, middleIn, last]
full_name = "{} {} {}".format(*name_parts)
print("Your full name is: {}".format(full_name))