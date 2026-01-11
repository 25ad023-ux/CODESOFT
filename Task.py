

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("\nSelect Operation:")
print("+  Addition")
print("-  Subtraction")
print("*  Multiplication")
print("/  Division")

choice = input("Enter operation: ")

match choice:
    case "+":
        print("Result =", num1 + num2)

    case "-":
        print("Result =", num1 - num2)

    case "*":
        print("Result =", num1 * num2)

    case "/":
        if num2 != 0:
            print("Result =", num1 / num2)
        else:
            print("Error: Division by zero")

    case _:
        print("Invalid operation selected")
