figure = input('Enter type of geometric figure:\n')

if figure == 'triangle':
    a = int(input('Enter the first side:\n'))
    b = int(input('Enter the second side:\n'))
    c = int(input('Enter the third side:\n'))
    p = ((a + b + c) / 2)
    S = abs(p * (p - a) * (p - b) * (p - c))
    # print(S)
    print(f'The area is:', round(S))
elif figure == 'rectungle':
    a = int(input('Enter the first side:\n'))
    b = int(input('Enter the second side:\n'))
    S = a * b
    print(f'The area is:', round(S))
elif figure == 'circle':
    r = int(input('Enter the radius:\n'))
    from math import pi
    S = pi * r * 2
    print(f'The area is:', round(S))
