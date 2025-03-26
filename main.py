# This is my first python program
print("i like thick thighs")
print("it's really good")

name = "Bro Code"
age = 25
gpa = 3.2
is_student = True

print(type(is_student))

gpa = int(gpa)
print(gpa)

age = float(age)
print(age)

age = str(age)
print(type(age))

name = bool(name)
print(name)

#input() = A function that prompts the user to enter data
#          Returns the entered data as a string

name = input("What is your name?: ")
age = int(input("How old are you?: "))
#age = int(age)
age = age + 1
print(f"Hello {name}!")
print("Happy birthday!")
print(f"You are {age} years old!")

# Exercise 1 Rectangle Area Calc

length = float(input("Enter length:"))
width = float(input("Enter width:"))
area = length * width

print(f"Tha area is: {area}cm²")

# Exercise 2 Shopping Cart Program

item = input("What item would you like to buy?: ")
price = float(input("What is the price?: "))
quantity = int(input("How many would you like?: "))
total = price * quantity

print(f"You have bought {quantity} x {item}/s")
print(f"Your total is: ${total}")









#comment


print("My first python program")
#Strings
first_name = "Bro"
food = "pizza"
email = "bro23@fake.com"

print(first_name)
print(f"hello {first_name}")
print(f"You like {food}")
print("\033[92mCeci est du texte en vert !\033[0m")
print(f"You like {food}")
print(f"My email is: {email}")


#integers
age = 25
quantity = 3
print(f"You are {age} years old!")
print(f"You are buying {quantity} items")

#float
price = 9.99
gpa = 3.2
distance = 5.5
print(f"The price is ${price}")
print(f"your gpa is {gpa}")
print(f"Your run {distance}km")

#boolean
is_student = False

print(f"Are you a student? : {is_student}")


for_sale = True
is_online = False

if is_online:
    print("You are online")
else:
    print("You are not online")

# Typecasting = the process of converting a variable from one data type to another
#                str(), int(), float(), bool()