"""Nathan Marson"""
name = input("Name: ")
if name == "":
    print("Invalid Input")
    name = input("Name: ")
print(name[1::2])
