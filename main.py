name = input("what is your name? ")
choice = True
fruit_choice = ""
fruits = ("Apple", "Grape", "Orange")
fruit_counter = 0
apple_counter = 0
grape_counter= 0
orange_counter = 0
while choice == True:
    print(f"1) {fruits[0]} $2")
    print(f"2) {fruits[1]} $1")
    print(f"3) {fruits[2]} $3")
    fruit_choice = input(f"\nhello {name}. Which fruit would you like to buy ")
    if fruit_choice == "1":
        print(f"you bought 1 {fruits[0]}")
        apple_counter = apple_counter + 1
    if fruit_choice == "2":
        print(f"you bought 1 {fruits[1]}")
        grape_counter = grape_counter + 1
    if fruit_choice == "3":
        print(f"you bought 1 {fruits[2]}")
        orange_counter = orange_counter + 1
    choice = input("would you like to buy  another piece of fruit? y/n ").lower()
    if choice == "y":
        choice = True
    elif choice == "n":
        choice = False
    else:
        choice = True
        while choice == True:
            print("not a valid option")
            choice = input("would you like to buy another piece of fruit? y/n ")
            if choice == "y":
                choice = True
                break
            else:
                choice = True
                print(f'choice: {choice}')
fruit_cost = (apple_counter * 2) + (grape_counter * 1) + (orange_counter * 3)
tax = (fruit_cost * .05)
total = tax + fruit_cost
print(f"Order for {name}")
print(f"You bought {apple_counter} {fruits[0]} at $2 apiece")
print(f"You bought {grape_counter} {fruits[1]} at $1 apiece")
print(f"You bought {orange_counter} {fruits[2]} at $3 apiece")
print(f"Sub Total ${fruit_cost}")
print(f"Tax ${tax}")
print(f"Total ${total}")