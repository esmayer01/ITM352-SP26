# Name: Ethan Mayer
# Date: Feb. 3, 2026

sentance = input

# 1. Turn string into a list of words
words = sentance.split(" ")
print("List of words:", words)

# 2. Reverse the list of words
words.reverse()
print("Reversed list of words:", words)

# 3. Join the reversed list of words back into a string
new_sentance = " ".join(words)
print("Reversed sentance:", new_sentance)
