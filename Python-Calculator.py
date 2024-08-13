def calculator():
    while True:
        
        # Print options for the user
        print("Enter '+' to add two numbers")
        print("Enter '-' to subtract two numbers")
        print("Enter '*' to multiply two numbers")
        print("Enter '/' to divide two numbers")
        print("Enter 'quite' to end the program")

        # Get user Input
        user_choice = input("Enter your choice: ")

        # logic for calculator and error handling
        if user_choice == 'quit':
            break
        if user_choice in ('+', '-', '*','/'):
            try:
                num1 = float(input("Enter the first number: ")) 
                num2 = float(input("Enter the second number: "))
            except ValueError:
                print("Invalid Input")
                continue
            
            if user_choice == '+':
                print("Sum: ",num1+num2)
            elif user_choice == '-':
                print("Difference: ", num1-num2)
            elif user_choice == '*':
                print("Product: ", num1*num2)
            elif user_choice == '/':
                if num2 != 0:
                    print("Division", num1/num2)
                else:
                    print("Division By Zero Error!!")
        else:
            print("Invalid Choice")

# Run the program 
calculator()