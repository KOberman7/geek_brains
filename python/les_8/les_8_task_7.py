class Complex_number:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return Complex_number(self.a + other.a, self.b + other.b)

    def __mul__(self, other):
        return Complex_number(self.a * other.a, self.b * other.b)

    def __str__(self):
        print(f'Результат: {str(self.a)}, {str(self.b)}')


c_n = Complex_number(-5 + 3j, 4 + 2j)
c_n2 = Complex_number(1 + 2j, 3 + 4j)
print(c_n + c_n2)
print(c_n * c_n2)