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

#sec 24 nested if statements

print("Welcome to the rollercoaster!")

height = int(input("What's your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster!")

    age = int(input("What's your age? "))

    if age <= 12:
        bill = 5
        print("You have to pay $5")
    elif age <= 18:
        bill = 7
        print("You have to pay $7")
    else:
        bill = 12
        print("You have to pay $12")

    wants_photo = input("Would you like the photo for extra payment? (y/n) ")
    if wants_photo == "y":
        bill += 3

    print(f"Your final bill is ${bill}")

else:
    print("You have to grow taller before you can ride.")

