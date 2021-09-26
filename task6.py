"""
def evc (a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    print(a)

evc(100, 200)
"""
def evc (a, b):
    if b == 0:
        return a
    else:
        return evc(b, a % b)

print(evc(565, 205))
    
         




