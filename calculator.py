while True:
    x = int(input("Enter number 1: "))
    y = int(input("Enter number 2: "))
    operation = input("Choose arithmetic operation symbol: ")

    if operation == "+":
        print(x + y)
    elif operation == "-":
        print(x - y)
    elif operation == "*":
        print(x * y)
    elif operation == "/":
        print(x / y)
    else:
        print("Wrong arithmetic operator!")
