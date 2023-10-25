print("This program computes the sum of the integers between two integers.")

first_term = int(input("Enter the first integer: "))
last_term = int(input("Enter the last integer: "))

sum = 0

for i in range(last_term + 1):
    sum = sum + i

for i in range(first_term):
    sum = sum - i

print("The sum of the integers between "+str(first_term)+" and "+str(last_term)+" is "+str(sum)+".")