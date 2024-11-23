def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide (n1 , n2):
    return n1/n2

operation = {
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide,
}

# print(operation["*"](4 ,8))
should = True
num1 = float(input("What is first number?: "))

while should :
    for symbol in operation:
        print(symbol)
    operation_symbol = input("Pick an operation: ")
    num2 = float(input("What is next number?: "))
    answer = operation[operation_symbol](num1, num2)
    print(f"{num1} {operation_symbol} {num2}  = {answer}")

    choice = input(f"Type 'y' to continue calculating with {answer} ,or type 'n' for start new calculation .")
    if choice == "y":
        num1 = answer
    else:
        should = False