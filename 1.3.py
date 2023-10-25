print ("This program compute the average of multiple numbers")

total = 0

circumference = int(input("Enter the number of circumferences you want to compute: "))

for i in range(circumference):
    num = float(input ("Enter a number: "))
    total += num / circumference

print ("The average number is: "+str(total)+".")