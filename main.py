if __name__ == '__main__':
    num1 = input("What is the first number?")
    op = input("What is the operator?")
    num2 = input("What is second number")
    if op == "+" :
        print(int(num1) + int(num2))
    if op == "-":
        print(int(num1) - int(num2))
    if op == "*":
        print(int(num1) * int(num2))
    if op == "/":
        print(int(num1) / int(num2))
