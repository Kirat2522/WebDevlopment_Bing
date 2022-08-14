#this whole script is wrriten by Gurkirat!
number_1 = int(input("Type your first number\n"))
number_2 = int(input("Type your second number\n"))
greaterthan_lessthan = str(input("What do you want Greaterthan or Lessthan?\n"))


if greaterthan_lessthan  == "Greaterthan":
  if number_1 > number_2:
    print("Yup, its true!!")
  else:
    print("Nope, its false!")


if greaterthan_lessthan == "Lessthan":
  if number_1 < number_2:
      print("Yup, its true!!")
  else: 
      print("Nope, its false!!") 
    
    