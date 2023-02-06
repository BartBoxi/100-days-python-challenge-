
from art import logo
print(logo)






#Calc

def add(n1, n2):
    return n1 + n2

def substract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": substract,
    "*": multiply,
    "/": divide
}

num1 = int(input("What's the first number"))
num2 = int(input("What's the second number"))

for key in operations:
 print(key)

operation_symbol = input("Pick an operation form the line above: ")
if operation_symbol == "+":
    answer = add(num1,num2)
elif operation_symbol == "-":
    answer = substract(num1, num2)
elif operation_symbol == "*":
    answer = multiply(num1, num2)
elif operation_symbol == "/":
    answer = divide(num1, num2)







print(f"{num1} {operation_symbol} {num2} = {answer}")
