def add(x, y):
    return x + y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero."

def subtract(x, y):
    return x - y

def modulo(x, y):
    if y != 0:
        return x % y
    else:
        return "Cannot perform modulo by zero."

while True:
    print("Choose operation:")
    print("1. Addition")
    print("2. Multiplication")
    print("3. Division")
    print("4. Subtraction")
    print("5. Modulo")
    print("6. Exit")

    choice = input("Enter choice (1/2/3/4/5/6): ")

    if choice == '6':
        print("Exiting the program. Goodbye!")
        break

    if choice not in ['1', '2', '3', '4', '5']:
        print("Invalid choice. Please enter a valid number.")
        continue

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        print(f"{num1} + {num2} = {add(num1, num2)}")
    elif choice == '2':
        print(f"{num1} * {num2} = {multiply(num1, num2)}")
    elif choice == '3':
        result = divide(num1, num2)
        print(f"{num1} / {num2} = {result}")
    elif choice == '4':
        print(f"{num1} - {num2} = {subtract(num1, num2)}")
    elif choice == '5':
        result = modulo(num1, num2)
        print(f"{num1} % {num2} = {result}")
