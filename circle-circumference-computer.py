print("this program computes the circumference of a circle.")

pi = 3.14

number_of_circumferences = int(input("Enter the number of circumferences you want to compute: "))
for whatever in range (number_of_circumferences):   
    radius = float(input ("Enter the radius of the circle: "))
    circumference = 2*radius*pi
    print ("The circumference of a circle with radius "+str(radius)+" is "+str(circumference)+".")

