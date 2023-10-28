print("This program computes the product of the integers in a range.")

last_integer = int(input("Enter the lower number of the range: "))
first_integer = int(input("Enter the upper number of the range: "))

product = 1

for i in range(last_integer, first_integer + 1):
    product *= i

print(f"The product of the integers between {last_integer} and {first_integer} is {product}.")
