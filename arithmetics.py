import math
"""radius = float(input('Enter the radius of a circle:'))
circumference = 2 * math.pi * radius
print(f"The circumference is:{round(circumference,2)}")"""

"""radius = float(input("Enter the radius of a circle:"))
area = math.pi * pow(radius,2)
print(f"The area of the circle is: {round(area,2)}")"""

"""a = float(input("Enter the a: "))
b = float(input("Enter the b: "))
c = math.sqrt(pow(a,2) + pow(b,2))
print(f"The hypothenus is: {round(c,2)}")"""

age = int(input("Enter your age:"))
if age >= 18:
    print("You are now signed up!")
elif age < 0:
    print("You haven't been born yet!")
elif age >= 100:
    print("You are too old to sign up!")
else:
    print("You must be 18+ to sign up!")