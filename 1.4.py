print ("This program displays a multiplication table.")

num = int(input("Enter the number for which the multiplication table should be shown: "))

for i in range(0, 10):
    result = num * i
    print (f"{i} x {num} = {result}")