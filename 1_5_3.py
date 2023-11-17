from fractions import Fraction


def add(a, b):
    print('{0} + {1} = {2}'.format(a, b, a + b))


def subtract(a, b):
    print('{0} - {1} = {2}'.format(a, b, a - b))


def multiply(a, b):
    print('{0} * {1} = {2}'.format(a, b, a * b))


def divide(a, b):
    print('{0} / {1} = {2}'.format(a, b, a / b))


if __name__ == '__main__':

    while True:
        a = Fraction(input('Enter first fraction: '))

        b = Fraction(input('Enter second fraction: '))
        op = str.lower(
            input('Operation to perform - Add, Subtract, Mulitply, Divide: '))
        if op == 'add':
            add(a, b)
        elif op == 'subtract':
            subtract(a, b)
        elif op == 'multiply':
            multiply(a, b)
        elif op == 'divide':
            divide(a, b)
        else:
            print('Input a valid operation')

        answer = input('Do you want to exit? (y) for yes ')
        if answer == 'y':
            break
