def calculator():
    print("calculator!")
    while True:
        try:
            num1 = float(input("Enter first number: "))
            operation = input("Enter operation (+, -, *, /): ")
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. plz enter a number.")
            continue
        
        if operation == '+':
            print(f"Result: {num1} + {num2} = {num1 + num2}")
        elif operation == '-':
            print(f"Result: {num1} - {num2} = {num1 - num2}")
        elif operation == '*':
            print(f"Result: {num1} * {num2} = {num1 * num2}")
        elif operation == '/':
            if num2 == 0:
                print(" Div by zero Error!!.")
            else:
                print(f"Result: {num1} / {num2} = {num1 / num2}")
        else:
            print("Invalid operation. Plz enter '+', '-', '*', or '/'.")
        
        choice = input("Do you want to perform another calculation?(yes/no): ")
        if choice.lower() != 'yes':
            print("Thank you")
            break

calculator()
