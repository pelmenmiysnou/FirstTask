#4
class Temperature:
    def __init__(self, celsius=0):
        self.celsius = celsius
    
    @property
    def celsius(self):
        return self._celsius
    
    @celsius.setter
    def celsius(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Температура должна быть числом")
        self._celsius = float(value)
    
    @property
    def fahrenheit(self):
        # Формула: F = C * 9/5 + 32
        return self.celsius * 9/5 + 32
        
    @fahrenheit.setter
    def fahrenheit(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Температура должна быть числом")
        
        self.celsius = (value - 32) * 5/9
        
    def __str__(self):
        return f"{self.celsius:.2f} C = {self.fahrenheit:.2f} F"

