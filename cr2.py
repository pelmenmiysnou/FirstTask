#2
import math

class ComplexNumber:
    def __init__(self, real, imag):
        if not isinstance(real, (int, float)) or not isinstance(imag, (int, float)):
            raise TypeError("Действительная и мнимая части должны быть числами")
        
        self.real = real
        self.imag = imag
    
    def __add__(self, other):
        if not isinstance(other, ComplexNumber):
            raise TypeError("Можно складывать только с комплексным числом")
        
        return ComplexNumber(self.real + other.real, self.imag + other.imag)
    
    def __mul__(self, other):
        if not isinstance(other, ComplexNumber):
            raise TypeError("Можно умножать только на комплексное число")
        real_part = self.real * other.real - self.imag * other.imag
        imag_part = self.real * other.imag + self.imag * other.real
        
        return ComplexNumber(real_part, imag_part)
    
    def modulus(self):
        return math.sqrt(self.real ** 2 + self.imag ** 2)
    
    def __repr__(self):
        if self.imag == 0:
            return f"{self.real}"
        
        if self.real == 0:
            return f"{self.imag}i"
        
        if self.imag < 0:
            return f"{self.real} - {abs(self.imag)}i"
        
        return f"{self.real} + {self.imag}i"
