# Simple Calculator Program

# Prompt user for input
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

print("Select operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")

choice = input("Enter your choice (+, -, *, /): ")

# Perform calculation based on user input
if choice == '+':
    result = num1 + num2
    print("Result:", result)
elif choice == '-':
    result = num1 - num2
    print("Result:", result)
elif choice == '*':
    result = num1 * num2
    print("Result:", result)
elif choice == '/':
    if num2 != 0:
        result = num1 / num2
        print("Result:", result)
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operation selected.")
