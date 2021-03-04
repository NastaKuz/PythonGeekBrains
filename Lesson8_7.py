"""Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте перегрузку
методов сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса (комплексные
числа) и выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата."""


class Complex:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):
        return Complex(self.real + other.real, self.imaginary + other.imaginary)

    def __mul__(self, other):
        mul_real = self.real * other.real - self.imaginary * other.imaginary
        mul_imag = self.real * other.imaginary + self.imaginary * other.real
        return Complex(mul_real, mul_imag)

    def __str__(self):
        return f"{self.real}{'+' if self.imaginary > 0 else '-'}" \
               f"{abs(self.imaginary) if abs(self.imaginary) != 1 else ''}i "


complex1 = Complex(2, 3)
complex2 = Complex(-1, 1)
print(complex1)
print(complex2)
print("Сложение:", complex1 + complex2)
print("Умножение:", complex1 * complex2)
