a = int(input('Enter the first number from 3 to 23: \n'))
b = int(input('Enter the second number from 3 to 23: \n'))
c = input('Enter the arithmetic operation (+, -, *, /): \n')
if c == '+':
    print(a + b)
if c == '-':
    print(a - b)
if c == '*':
    print(a * b)
if c == '/':
    print(a / b)
else:
    print('Error')