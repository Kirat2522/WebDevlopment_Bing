#This whole shop is made by only me with some of the hints!

print("Welcome to our Home Like Rastrant!")

name = input("What is your name?\n")

print("Hello " + name + ", Thanks for coming in today!")


order = input("What do you like to order? solid meal, snakes or drinks?\n")

if order == "drinks":
    print("Coca-Cola, Fruti, Maza, Sting, Limca")
    order = input("what do you like order?\n")

    if order == "Coca-Cola":
        price = 8
        extra = input("Do you like extra large family bottle?\n")
        if extra == "Yes":
            price = 10
            print("Your price is increased to $10")
        else:
            print("Its will cost you $8")

    if order == "Fruti":
        price = 8
        extra = input("DO you like a family pack bottle?\n")
        if extra == "Yes":
            price = 11
            print("Your Price is increased to $11")
        else:
            print("It will cost you $8")

    if order == "Maza":
        price = 11
        extra = input("Do you want an extra lage bottle?\n")
        if extra == "Yes":
            price = 13
            print("Your price is increased to $13")
        else:
            print("It will cost you $11")
    
    if order == "Sting":
        price = 14
        extra = input("Do you want an extra lage bottle?\n")
        if extra == "Yes":
            price = 17
            print("Your price is increased to $17")
            print("This drink is expencive because it gives you enough energy to do work.")
        else:
            print("It will cost you $14")

    if order == "Limca":
        price = 10
        extra = input("Do you want an extra lage bottle?\n")
        if extra == "Yes":
            price = 12
            print("Your price is increased to $12")
        else:
            print("It will cost you $10")

    balance = int(input("What is you balance sir?\n"))

    quantity = int(input("How much do you want?\n"))

    total = price * int(quantity)

    print("you total is: $" + str(total))

    confermation = input("Are you sure you want to conferm your order?\n")

    if confermation == "No":
        print("Ah, you are not ready yet?")
    
    elif balance < total:
        print("Unfortunatelly, your balance is not enough to buy " + order + ". try to reduce you order!")

    else:
        print("You are good to go! Your order will be ready in a moment.")
else:
    menu = "French Fries, Burger, Pizza, Doritos, Lays"
    print(menu)

order = input("What do you like to order sir?\n\n")

if order == "French Fries":
    price = 2
    extra = input("Do you like extra chessy?\n")
    if extra == "Yes":
        price = 3
        print("your price is increase to $3")
    else:
        print("It will cost you $2")


elif order == "Burger":
    price = 3
    extra = input("Do you like extra chessy?\n")
    if extra == "Yes":
        price = 5
        print("your price is increase to $5")
    else:
        print("It will cost you $3")
    

elif order == "Pizza":
    price = 5
    extras = input("Do you like extra chessy and extra crunchy?\n")
    if extras == "Yes":
        price = 7
        print("Your price is increased to $7")
    else:
        print("It will cost you $5")

elif order == "Doritos":
    price = 2
    print("It will cost you $2 each.")

elif order == "Lays":
    price = 2
    print("It will cost you $2 each.")

else:
    print("We don't have your " + order + ". Right now in our restront.")

balance = int(input("What is you balance sir?\n"))

quantity = int(input("How much do you want?\n"))

total = price * int(quantity)

print("you total is: $" + str(total))

confermation = input("Are you sure you want to conferm your order?\n")

if confermation == "No":
    print("Ah, you are not ready yet?")
    
elif balance < total:
    print("Unfortunatelly, your balance is not enough to buy " + order + ". try to reduce you order!")

else:
    print("You are good to go! Your order will be ready in a moment.")

    







