"""
x = int(input('Insert the number :\n'))

c = x % 10
b = x // 10 % 10
a = x // 100

print(f'Sum result:', a + b + c)
"""
x = int(input('Insert the number :\n'))

Sum_result = 0

while x > 0:
    last = x % 10
    Sum_result = Sum_result + last
    x = x // 10

print(f'Sum result:', Sum_result)
