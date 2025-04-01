"""radius = float(input('Enter the radius of a circle:'))
circumference = 2 * math.pi * radius
print(f"The circumference is:{round(circumference,2)}")"""
#/////////////////////////////////////////////////////////////////
"""radius = float(input("Enter the radius of a circle:"))
area = math.pi * pow(radius,2)
print(f"The area of the circle is: {round(area,2)}")"""
#////////////////////////////////////////////////////////////////
"""a = float(input("Enter the a: "))
b = float(input("Enter the b: "))
c = math.sqrt(pow(a,2) + pow(b,2))
print(f"The hypothenus is: {round(c,2)}")"""
#////////////////////////////////////////////////////////////////
"""age = int(input("Enter your age:"))
if age >= 18:
    print("You are now signed up!")
elif age < 0:
    print("You haven't been born yet!")
elif age >= 100:
    print("You are too old to sign up!")
else:
    print("You must be 18+ to sign up!")"""
#///////////////////////////////////////////////////////////////////
"""response = input("Would you like food? (Y/N):")

if response == "Y":
    print("Have some food!")
elif response == "N":
    print("No food for you!")
else:
    print("Answer the question!!")"""
#/////////////////////////////////////////////////////////////////////
"""name = input("Enter your name:")

if name == "":
    print("Please enter your name!")
else:
    print(f"Hello {name}")"""
#//////////////////////////////////////////////////////////////////////
"""Online = True
if Online:
    print("This user is online")
else:
    print("This user is offline")"""
#///////////////////////////////////////////////////////////////////////
#Number Checker

"""Number = int(input("Enter a number:"))

if Number > 0:
    print("The number is positive!")
elif Number < 0:
    print("The number is negative!")
elif Number == 0:
    print("The number is zero!")"""
#////////////////////////////////////////////////////////////////////////////
#Even or odd

"""test = int(input("Enter a number:"))

if test % 2 == 0:
    print("It's an even number!")
else:
    print("It's an odd number!")"""
#///////////////////////////////////////////////////////////////////////////////
#Age category

"""age = int(input("Enter your age:"))

if age < 13:
    print("You are a child!")
elif age >= 13 and age < 19:
    print("You are a teenager!")
elif age >= 19:
    print("You are an adult!")"""
#/////////////////////////////////////////////////////////////////////////////////
#Maximum of theese numbers

"""num1 = int(input("Enter number 1:"))
num2 = int(input("Enter number 2:"))
num3= int(input("Enter number 3:"))

if num1 > num2 and num1 > num3:
    print(f"{num1} is the maximum number!")
elif num2 >num1 and num2 >num3:
    print(f"{num2} is the maximum number!")
elif num3 >num1 and num3 >num2:
    print(f"{num3} is the maximum number!")"""
#//////////////////////////////////////////////////////////////////////////////////
#Garding system

"""grade = float(input("Enter you grade:"))

if grade >= 90:
    print("Grade A")
elif grade >= 80 and grade < 90:
    print("Grade B")
elif grade >= 70 and grade < 80:
    print("Grade C")
else:
    print("Grade F")"""
#//////////////////////////////////////////////////////////////////////////////////
#Password checker

"""pwd = input("Enter a password:")

if pwd == "admin123":
    print("Access granted!")
else:
    print("Access denied!")"""
#//////////////////////////////////////////////////////////////////////////////////
#Vowel or Consonant

"""char = input("Enter a letter:")

if (char == 'a' or char == 'e' or char == 'i' or
     char == 'o' or char == 'u' or char == 'y'):
    print("It's a vowel!")
elif char == "":
    print("it's a conconant!")
else:
    print("Error, not a letter!")"""
#/////////////////////////////////////////////////////////////////////////////////
#Python calculator

"""operator = input("Enter an operator (+ - * /):")
num1 = float(input("Enter the 1st number:"))
num2 = float(input("Enter the 2nd number:"))

if operator == "+":
    result = num1 + num2
    print(result)
elif operator == "-":
    result = num1 - num2
    print(result)
elif operator == "*":
    result = num1 * num2
    print(result)
elif operator == "/":
    result = num1 / num2
    print(result)
else:
    print(f"{operator} is not an operator!")"""
#//////////////////////////////////////////////////////////////////////////////////
#Python weight converter

"""weight = float(input("Enter your weight:"))
unit = input("Kilograms pr Pounds? (K or L):")

if unit == "K":
    weight = weight * 2.205
    unit = "Lbs."
    print(f"Your weight is {round(weight)} {unit}")
elif unit == "L":
    weight = weight / 2.205
    unit = "Kgs."
    print(f"Your weight is {round(weight)} {unit}")
else:
    print(f"{unit} was not valid!")"""
#/////////////////////////////////////////////////////////////////////////////////










