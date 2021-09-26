a = input()
b = input()
if a.isdigit and b.isdigit:
    a = int(a)
    b = int(b)
    if 3 < a < 22 and 3 < b < 22:
        if a > b:
            print(round(a - b))
        else:
            print(round(b - a))
else:
    a = str(a)
    b = str(b)
    print(a + b)

