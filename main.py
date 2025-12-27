# print("welcome to the rollercoaster!")
#
# height = int(input("whats your height in cm ?"))
#
# if(height >= 120):
#     print("you can ride the rollerCoaster")
# else: print("you have to wait to grow before u can ride ")


# #sec 23 modulo
# num_to_check = int(input("what number do you want to check ?"))
#
# print(num_to_check % 2)
#
# if num_to_check % 2 == 0:
#     print("even")
# else:
#     print("odd")

#sec 24 & 25 nested if statements

# print("Welcome to the rollercoaster!")
#
# height = int(input("What's your height in cm? "))
# bill = 0
#
# if height >= 120:
#     print("You can ride the rollercoaster!")
#
#     age = int(input("What's your age? "))
#
#     if age <= 12:
#         bill = 5
#         print("You have to pay $5")
#     elif age <= 18:
#         bill = 7
#         print("You have to pay $7")
#     else:
#         bill = 12
#         print("You have to pay $12")
#
#     wants_photo = input("Would you like the photo for extra payment? (y/n) ")
#     if wants_photo == "y":
#         bill += 3
#
#     print(f"Your final bill is ${bill}")
#
# else:
#     print("You have to grow taller before you can ride.")
#


# lec 26 pizza order app
print("Welcome to python pizza deliveries")

size = input("What size pizza do you want? S, M, or L: ")
pepperoni = input("Do you want pepperoni? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

bill = 0

# Pizza size price
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25
else:
    print("You haven't chosen a valid size")

# Pepperoni price
if pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

# Extra cheese price
if extra_cheese == "Y":
    bill += 1

print(f"Your total bill is ${bill}")



