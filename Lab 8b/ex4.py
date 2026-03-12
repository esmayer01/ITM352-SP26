#Debugging exercise # 4
# Retrieving elements from a list
def get_element(lst, index):
    if index < len(lst):
        return lst[index]
    else:
        return "Error: index out of range"
my_list = [1, 2, 3, 4, 5]
print(get_element(my_list, 2))  
print(get_element(my_list, 5))