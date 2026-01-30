# Define a list of survey response values [5, 7, 3, and 8] and store them in a variable. 
# Next define a tuple of respondent ID values (1012, 1035, 1021, and 1053). 
# Use the .append() method to append the tuple to the list. Print out the list.
# Name: Ethan Mayer
# Date: Jan. 29, 2026

responses = [5, 7, 3, 8]
respondent_ids = (1012, 1035, 1021, 1053)
responses.append(respondent_ids)
print("survey responses with IDs:", responses)

response_values = [(1012, 5), (1035, 7), (1021, 3), (1053, 8)]
response_values.sort()
print("sorted survey responses with IDs:", response_values)