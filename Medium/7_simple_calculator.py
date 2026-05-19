#Simple Calculator with Menu
print("simple calculator")
while True:
    print("\n 1.Add")
    print("2.Subtract")
    print("3.multiplication")
    print("4.Division")
    print("5.Exit")
    choice = int(input("Enter your choice"))
    if choice  == 5:
        break
    if choice in [1,2,3,4]:
        n1 =int(input("Enter the first number:"))
        n2 =int(input("Enter the second number:"))
        if choice == 1:
            print(f"Result:{n1}+{n2} ={n1+n2}")
        elif choice == 2:
            print(f"Result:{n1}-{n2} ={n1-n2}")
        elif choice == 3:
            print(f"Result:{n1}*{n2} ={n1*n2}")
        elif choice ==4:
            if n2 !=0:
                print(f"Result:{n1}/{n2} ={n1/n2}")
            else:
                print ("Error: Cannot divide by zero!")
    else:
        print("Invalid choice! Please try again.")

        
    