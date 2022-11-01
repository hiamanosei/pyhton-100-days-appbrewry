



def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    return num1 / num2


operand = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

value1 = float(input("first digit"))
value2 = float(input("Second digit"))
#
for key in operand:
    print(f"{key}")

sign = input("What is the operator")

operation_guess = operand[sign]
operation_guess(value2,value1)
calc = operation_guess(value1, value2)
print(f"{value1}and{sign}and{value2} is {calc}")




#calc(value1=value1,value2=value2,sign=sign)