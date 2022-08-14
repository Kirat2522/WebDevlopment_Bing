print("Welcome to the KIRAT STORE")

name = input("what is your name?\n")

print("Hello " + name + ", Thanks for checking in our store\n\n")

menu = '''Aloo Ka Parantha, Rajma Chawal, Biryani, Curry Chaval,
Bajre Di Rote and sarso da saag, Manchoorian, Symple daal
roti.'''

print( name +", this is our menu for today.\n" + menu)

order = input()

price = 13

quantity = input("Goot Choice! How much would you like to order?\n")

total = price * int(quantity) 

print("Thank you. Your total is: $" + str(total))

print("Sounds Good " + name + ", your order will be ready soon!\n Please recheck you order: Your order is: " + quantity + " " + order)