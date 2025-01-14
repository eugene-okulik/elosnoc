def action_selector(func):

    def wrapper(*args):
        if first < 0 or second < 0:
            operation = '*'
            print('Multiplying numbers:')
            func(first, second, operation)
        elif first == second:
            operation = '+'
            print('Summing the first and the second numbers:')
            func(first, second, operation)
        elif first > second:
            operation = '1-2'
            print('Subtracting the second number from the first:')
            func(first, second, operation)
        else:
            operation = '2-1'
            print('Subtracting the first number from the second:')
            func(first, second, operation)
    return wrapper


@action_selector
def calc(first, second, operation):
    if operation == '+':
        print(first + second)
    elif operation == '*':
        print(first * second)
    elif operation == '1-2':
        print(first - second)
    else:
        print(second - first)


first = int(input('Enter first number:'))
second = int(input('Enter second number:'))
calc()

# Код ниже с другими наименованиями аргументов тоже выполняется, но я не могу понять причину.
# Вероятнее всего, неверно написан сам декоратор, хоть и выполняется код.
#
# def action_selector(func):
#
#     def wrapper(*args):
#         if first < 0 or second < 0:
#             operation = '*'
#             print('Multiplying numbers:')
#             func(first, second, operation)
#         elif first == second:
#             operation = '+'
#             print('Summing the first and the second numbers:')
#             func(first, second, operation)
#         elif first > second:
#             operation = '1-2'
#             print('Subtracting the second number from the first:')
#             func(first, second, operation)
#         else:
#             operation = '2-1'
#             print('Subtracting the first number from the second:')
#             func(first, second, operation)
#     return wrapper
#
#
# @action_selector
# def calc(x, y, operation):
#     if operation == '+':
#         print(first + second)
#     elif operation == '*':
#         print(first * second)
#     elif operation == '1-2':
#         print(first - second)
#     else:
#         print(second - first)
#
#
# first = int(input('Enter first number:'))
# second = int(input('Enter second number:'))
# calc()
