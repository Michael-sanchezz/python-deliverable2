choice = True
x = input("x value ").lower()
if x == str.lower("A"):
    print(x)
else:
    print(x)

while choice == True:
    choice = input("choice y/n ")
    if choice == "y":
        choice = True
    elif choice == "n":
        choice = False
    else:
        choice = True
        print("try again")

