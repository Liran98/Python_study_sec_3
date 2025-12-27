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

print("welcome to the rollercoaster!")

height = int(input("whats your height in cm ?"))

if(height >= 120):
    print("you can ride the rollerCoaster")
    age = int(input("whats your age ?"))

    if(age <= 18):
     print("you have to pay 7$")

    elif (age <= 12):
        print("you have to pay 5$")
    else:
        print("you have to pay 12$")

else: print("you have to wait to grow before u can ride ")
