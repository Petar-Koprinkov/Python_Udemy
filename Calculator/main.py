from operator_symbols import add, divide, subtract, multiply, modulo
from logo import art

operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
    '%': modulo
}


def calculate():
    print(art)

    first_number = int(input("Enter first number: "))
    flag = True

    while flag:
        operator_symbol = input("Enter operator: ")
        if operator_symbol in operations:
            second_number = int(input("Enter second number: "))
            result = operations[operator_symbol](first_number, second_number)
            print(result)
            is_continue = input("Do you want to continue? (y/n): ")

            if is_continue == "y":
                first_number = result
            elif is_continue == "n":
                flag = False
                calculate()
        else:
            print("Invalid operator!")


calculate()
