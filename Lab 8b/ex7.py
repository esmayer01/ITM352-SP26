 def multiply(x, y):
   product = 0
   for i in range(y):
       product += x
  
   return product
first = int(input("Enter the first number: "))
second = int(input("Enter the second number: "))
prod = multiply(first, second)
print(f"The product of {first}, {second} is {prod}")