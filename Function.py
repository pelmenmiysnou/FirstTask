#7
class Function:
    def __call__(self, x):
        if not isinstance(x, (int, float)):
            raise TypeError("Аргумент x должен быть числом")
        
        raise NotImplementedError("Метод должен быть переопределен в подклассах")
    
    def __repr__(self):
        return "Function()"
    
    def __eq__(self, other):
        if not isinstance(other, Function):
            raise TypeError("Можно сравнивать только с другой функцией")
        
        return self(1) == other(1)
    
    def __lt__(self, other):
        if not isinstance(other, Function):
            raise TypeError("Можно сравнивать только с другой функцией")
        
        return self(1) < other(1)
    
    def __gt__(self, other):
        return other < self
    
    def __le__(self, other):
        return self <= other
    
    def __ge__(self, other):
        return self >= other 


class LinearFunction(Function):
    def __init__(self, a, b):
        self._validate_coefficients(a, b)
        self.a = a
        self.b = b
    
    def _validate_coefficients(self, a, b):
        if not isinstance(a, (int, float)):
            raise TypeError("Коэффициент a должен быть числом")
        if not isinstance(b, (int, float)):
            raise TypeError("Коэффициент b должен быть числом")
    
    def __call__(self, x):
        try:
            super().__call__(x)  
            return self.a * x + self.b
        except NotImplementedError:
            return self.a * x + self.b
    
    def __repr__(self):
        if self.a == 0:
            return f"f(x) = {self.b}"
        
        if self.b == 0:
            return f"f(x) = {self.a}x"
        
        if self.b > 0:
            return f"f(x) = {self.a}x + {self.b}"
        
        return f"f(x) = {self.a}x - {abs(self.b)}"


class QuadraticFunction(Function):
    def __init__(self, a, b, c):
        self._validate_coefficients(a, b, c)
        self.a = a
        self.b = b
        self.c = c
    
    def _validate_coefficients(self, a, b, c):
        if not isinstance(a, (int, float)):
            raise TypeError("Коэффициент a должен быть числом")
        if not isinstance(b, (int, float)):
            raise TypeError("Коэффициент b должен быть числом")
        if not isinstance(c, (int, float)):
            raise TypeError("Коэффициент c должен быть числом")
        
        if a == 0:
            raise ValueError("Коэффициент a не может быть равен 0 для квадратичной функции")
    
    def __call__(self, x):
        try:
            super().__call__(x)  
            return self.a * x**2 + self.b * x + self.c
        except NotImplementedError:
            return self.a * x**2 + self.b * x + self.c
    
    def __repr__(self):
        if self.b != 0:
            if self.b > 0:
                result += f" + {self.b}x"
            else:
                result += f" - {abs(self.b)}x"
        
        if self.c != 0:
            if self.c > 0:
                result += f" + {self.c}"
            else:
                result += f" - {abs(self.c)}"
        
        return result
