#advance list!
# i'm changing camping_list to supplies!
supplies = ["test", "sleeping bags", "water", "raspberry pi", "coffee", "knife", "ethernet cable","flash drive", "bread oil", "marshmellow"]

camp_site = ["Crystal Lake", 404, 89.3, True]

#this is usesd to add a single item
#supplies.append("Bread")
#supplies.append("banana")

#this dose the same thing as addition method given below
#supplies.extend(["bread", "banana"])

#this is used to add multiple things in the list.
#supplies = supplies + ["Bread", "Banana"]

supplies.insert(0, "Banana")
print(supplies)
