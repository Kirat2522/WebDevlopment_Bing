

print("Hello welcome to Kirat coffee!")

name = input("What is you name?\n")

if name == "Ben":
    evil_status = input("Are you evil?\n")
    if evil_status == "Yes":
        print("You're not welcome here Evil ben!! Get Out!!")
        exit()
    else:
        print("Oh, so you're not that evil ben. Come on you are in!!")
else:
    print("Hello " + name + ", Thank you so much for coming in today.\n\n")




menu = "Black Coffee, Espresso, Latte, Cappucino, Frappuccino"

print(name + ", What do you like  from our today's menu?\n" 
+ menu)

order = input()

price = 8

quantity = input("How many coffees do you like?\n")

total = price * int(quantity)

print("Thank you. Your total is: $" + str(total))

print("Sounds good " + name + ", we'll have your " + quantity + " " + order + "ready for you in a moment.")

