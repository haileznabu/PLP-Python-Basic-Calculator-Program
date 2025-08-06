# Simple Python Program: Calculator PLP
print("Simple Calculator")

# Get user input for first numbers
num1 = float(input("Enter the first number: "))

# Get user input for second number
num2 = float(input("Enter the second number: "))

# Display available operations
print("Choose operation + for addition, - for subtraction, * for multiplication, / for division")

# Get user input for the operation
op = input("Enter operation (+, -, *, /): ")

# Validate the operation input
# Perform the operation based on user input
if op == '+':
    result = num1 + num2
    print(f"Result: {num1} + {num2} = {result}")
elif op == '-':
    result = num1 - num2
    print(f"Result: {num1} - {num2} = {result}")
elif op == '*':
    result = num1 * num2
    print(f"Result: {num1} * {num2} = {result}")
elif op == '/':
    if num2 != 0:
            result = num1 / num2
            print(f"Result: {num1} / {num2} = {result}")
    else:
        print("Error by zero is not allowed.")
else:
    print("Invalid operation selected.")

