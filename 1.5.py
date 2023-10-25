print ("This program displays a multiplication table.")

num = int(input("Enter the number for which the multiplication table should be shown: "))

first_term = int(input ("Enter the first integer: "))
last_term = int(input ("Enter the last integer: "))

for i in range(first_term, last_term):
    result = num * i
    print (f"{i} x {num} = {result}")