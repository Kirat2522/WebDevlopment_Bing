#faulty calculator

operator = input("Enter operator")
val1 = int(input("Enter first operator\n"))
val2 = int(input("Enter second operator\n"))

if operator == "+":
    if val1 == 56 and val2 == 9:
        print("77")
    else:
        print("sum is: ", val1 + val2)
if operator == "*":
    if val1 == 45 and val2 == 3:
        print("555")
    else:
        print("Subtract is: ", val1 - val2)

if operator == "/":
    if val1 == 56 and val2 == 6:
        print("4")
    else:
        print("devide is: ", val1/val2)

if operator == "-":
    print("subtraact is: ", val1 - val2)
