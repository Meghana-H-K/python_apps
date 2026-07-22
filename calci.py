try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    print("\nSelect Operation")
    print("+ : Addition")
    print("- : Subtraction")
    print("* : Multiplication")
    print("/ : Division")

    choice = input("Enter operation (+, -, *, /): ")

    if choice == "+":
        result = num1 + num2
        print("Result:", result)

    elif choice == "-":
        result = num1 - num2
        print("Result:", result)

    elif choice == "*":
        result = num1 * num2
        print("Result:", result)

    elif choice == "/":
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
        else:
            result = num1 / num2
            print("Result:", result)

    else:
        print("Invalid operation selected.")

except ValueError:
    print("Error: Please enter valid numeric values.")