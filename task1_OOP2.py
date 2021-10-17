class Complex:
    def __init__(self, x, y):
        self.real = x
        self.imag = y

    def __repr__(self):
        return f'{self.real} + ({self.imag})j'

    def __add__(self, other):
        if isinstance(other, int):
            return Complex(self.real + other, self.imag)
        if isinstance(other, Complex):    
            return Complex(self.real + other.real, self.imag + other.imag)

    def __eq__(self, other):
        if isinstance(other, Complex):
            return (self.real == other.real) and (self.imag == other.imag)

    def __abs__(self):
        return (self.real ** 2 + self.imag **2) ** 0.5

    def __sub__(self, other):
        if isinstance(other, int):
            return Complex(self.real - other, self.imag)
        if isinstance(other, Complex):    
            return Complex(self.real - other.real, self.imag - other.imag)

    def __mul__(self, other):
        if isinstance(other, int):
            return Complex(self.real * other, self.imag * other)
        if isinstance(other, Complex):
            return Complex((self.real * other.real - self.imag * other.imag), (self.imag * other.real + self.real * other.imag))

    def __truediv__(self, other):
        if isinstance(other, int):
            return Complex(self.real / other, self.imag / other)
        if isinstance(other, Complex):    
            return Complex(((self.real * other.real + self.imag * other.imag) / (other.real ** 2 + other.imag ** 2)), ((self.imag * other.real - self.real * other.imag) / (other.real ** 2 + other.imag ** 2)))




c = Complex(-5, -1)
a = Complex(-1, 1)
print(c / 3)
