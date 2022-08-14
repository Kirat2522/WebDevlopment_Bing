#This is my coffee shop and we have to stop evil ben, Particia and Loki!

print("Hello welcome to Kirat coffee!")

name = input("What is you name?\n")

if name == "Ben" or name == "Patricia" or name == "Loki":
    evil_status = input("Are you evil?\n")
    good_deeds = int(input("How many good deed have you done today?\n"))
    if evil_status == "Yes" and good_deeds < 4:
        print("You're not welcome here Evil " + name + "!! Get Out!!")
        exit()
    else:
        print("Oh, so you're not that Evil " + name + ". Come on you are in!!")

else:
    print("Hello " + name + ", Thank you so much for coming in today.\n\n")




menu = "Black Coffee, Espresso, Latte, Cappucino, Frappuccino"

print(name + ", What do you like  from our today's menu?\n" 
+ menu)

order = input()

if order == "Black Coffee":
    price = 4
    print("It will cost you $4")
    
elif order == "Espresso":
    price = 6
    print("It will cost you $6")

elif order == "Latte":
    price = 8
    print("It will cost you $8")


elif order == "Cappucino":
    price = 13
    print("It will cost you $13")

elif order == "Frappuccino":
    price = 16
    print("It will cost you $16")

else:
    print("OOps! we don't cell " + order)
    exit()
    


quantity = input("How many coffees do you like?\n")


total = price * int(quantity)

print("Thank you. Your total is: $" + str(total))

budget = int(input("What is you budget?\n"))

if total>budget:
    print("Oops! It seems like you don't have enough money")
else:
    print("Sounds good " + name + ", we'll have your " + quantity + " " + order + "ready for you in a moment.")

