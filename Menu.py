# Menu Function
# can be moved if needed

def menu():
    """""Creates a menu players can access."""

    options = ["Exit Menu", "Display Items","Pick Up Item", "Drop Item","Save Game"]
    print("Options: \n")
    
    for i in enumerate(options, start = 1):
        print(i)

    choice = int(input("Enter the number of the chosen option: "))

    if choice == 1:
        abc = 1
    elif choice == 2:
        abc = 1
    elif choice == 3:
        abc=1
    elif choice == 4:
        abc = 1
    elif choice == 5:
        abc = 1
    else:
        print("That is not one of the options. Please try again.")
        menu()
    
