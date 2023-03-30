#Calculator
from art import logo

#Add
def add(n1, n2):
    return n1 + n2

#Subtract
def subtract(n1, n2):
    return n1 - n2

#Multiply
def multiply(n1, n2):
    return n1 * n2

#Divide
def divide(n1, n2):
    return n1 / n2

operations = {
    "+" : add,
    "-": subtract,
    "*" : multiply,
    "/" : divide,
}

def calculator():
    print(logo)
    num1 = float(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)
    cont = True

    while cont:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1,num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        restart = input(f"Type 'y' to continue calculating with {answer}, or press 's' to start over, or press 'n' to exit.: ")

        if restart == "y":
            num1 = answer
        elif restart == "s":
            cont = False
            calculator()
        else:
            cont = False

calculator()
