def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def main():
    num1 = float(input("Type first number: "))
    operation = input("Choose an operation (+, -, *, /): ")
    num2 = float(input("Type second number: "))

    if operation == '+':
        result = add(num1, num2)

    elif operation == '-':
        result = subtract(num1, num2)

    elif operation == '*':
        result = multiply(num1, num2)

    elif operation == '/':
        result = divide(num1, num2)

    else:
        print("Invalid an operation")
        return main()

    print("Result: ", result)

if __name__ == "__main__":
    main()
