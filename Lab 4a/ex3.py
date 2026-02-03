# Manipulating a list in various ways
# Name: Ethan Mayer
# Date: Jan. 29, 2026

# responseValues = [5, 7, 3, 8]
# responseValues.append(0)
# print("After appending 0:", responseValues)

# responseValues.insert(2, 6)
# responseValues = responseValues[:2] + [6] + responseValues[2:]
# print("After inserting 6 at index 2:", responseValues)

responseValues = [5, 7, 3, 8]

# add 0 to the end
responseValues = responseValues + [0]

# insert 6 between 7 and 3 (index 2)
responseValues = responseValues[:2] + [6] + responseValues[2:]

print("Updated response values:", responseValues)