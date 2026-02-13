# Ethan Mayer
# Feb. 10, 2026

result = emotions = ("happy", "sad", "fear", "surprise")
emotions = ("happy", "sad", "fear", "surprise")

# Write a code that uses a conditional expressions (do not use an if statement or ternary expressions) to 
# print "true" if the last element is "happy" and there are more than 3 elements, or "false" if it is not.
result = emotions[-1] == "happy" and len(emotions) > 3
if(result == True):
    print("true")
else:
    print("false")
    
