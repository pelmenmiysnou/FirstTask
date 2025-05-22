class Product:
    def __init__(self, title, price):
        self.title = title  # Используем сеттер для валидации
        self.price = price  # Используем сеттер для валидации
    
    @property
    def title(self):
        return self._title
    
    def title(self, value):
        if not isinstance(value, str):
            raise TypeError("Название должно быть строкой")
        if not value.strip():
            raise ValueError("Название не может быть пустым")
        self._title = value
    
    @property
    def price(self):
        return self._price
    
    def price(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Цена должна быть числом")
        if value < 0:
            raise ValueError("Цена не может быть отрицательной")
        self._price = float(value)
    
    def get_discounted_price(self, discount):
        if not isinstance(discount, (int, float)):
            raise TypeError("Скидка должна быть числом")
        if discount < 0 or discount > 100:
            raise ValueError("Скидка должна быть от 0 до 100%")
        
        try:
            return self.price * (1 - discount / 100)
        except ZeroDivisionError:
            raise ValueError("Ошибка при расчете скидки")
    
    def __str__(self):
        return f"Продукт: {self.title}, Цена: {self.price:.2f} руб."


class Book(Product):
    def __init__(self, title, author, price, pages):
        super().__init__(title, price)
        self.author = author  
        self.pages = pages  
    
    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, value):
        if not isinstance(value, str):
            raise TypeError("Автор должен быть строкой")
        if not value.strip():
            raise ValueError("Имя автора не может быть пустым")
        self._author = value
    
    @property
    def pages(self):
        return self._pages
    
    @pages.setter
    def pages(self, value):
        if not isinstance(value, int):
            raise TypeError("Количество страниц должно быть целым числом")
        if value < 1:
            raise ValueError("Количество страниц должно быть положительным")
        self._pages = value
    
    def __str__(self):
        return f"Книга: {self.title}, Автор: {self.author}, {self.pages} стр., Цена: {self.price:.2f} руб."


class EBook(Book):
    def __init__(self, title, author, price, pages, file_size, file_format):
        super().__init__(title, author, price, pages)
        self.file_size = file_size    
        self.file_format = file_format  
    
    @property
    def file_size(self):
        return self._file_size
    
    @file_size.setter
    def file_size(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Размер файла должен быть числом")
        if value <= 0:
            raise ValueError("Размер файла должен быть положительным")
        self._file_size = float(value)
    
    @property
    def file_format(self):
        return self._file_format
    
    @file_format.setter
    def file_format(self, value):
        if not isinstance(value, str):
            raise TypeError("Формат файла должен быть строкой")
        if not value.strip():
            raise ValueError("Формат файла не может быть пустым")
        
        self._file_format = value.upper()
    
    def __str__(self):
        return (f"Электронная книга: {self.title}, Автор: {self.author}, "
                f"{self.pages} стр., {self.file_size:.1f} МБ, Формат: {self.file_format}, "
                f"Цена: {self.price:.2f} руб.")
