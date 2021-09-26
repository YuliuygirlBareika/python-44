a = int(input('Enter the deposit: \n'))
year = int(input('Enter years: \n'))
x = 0
while x in range(year):
    x = x + 1
    a += a * 0.1
print(round(a, 2))