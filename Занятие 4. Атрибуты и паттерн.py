class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __setattr__(self, key, value):
    if key == 'name' and len(value) == 0:
      raise ValueError("Name cannot be empty!")
    elif key == 'age' and isinstance(value, int) and value < 0:
      raise ValueError("Age must be a positive number!")
    super().__setattr__(key, value)

person = Person("Misha", 11)
print(person.name)
print(person.age)
person.name = ''
person.age = -1




class Counter:
  def __getattribute__(self, item):
    print(f"доступ к атрибуту {item}")
    try:
      return object.__getattribute__(self, item)
    except AttributeError:
      # raise ValueError("None")
      return None

c = Counter()
c.value = 5
print(c.value)
print(c.name)




class Car:
  def __init__(self, make, model):
    self.make = make
    self.model = model
    
  def __getattr__(self, item):
    print("This attribute is not available")

c = Car("Toyota", "Corolla")
print(c.make)
print(c.color)
print(c.year)




class Rectangle:
  def __init__(self, width, height):
    self.width = width
    self.height = height

  def __setattr__(self, key, value):
    if key == 'width' or key == 'height':
      super().__setattr__(key, value)
    else:
      raise AttributeError("Local attributes are not allowed")

tochka = Rectangle(10, 15)
print(tochka.width)
print(tochka.height)
tochka.height = 25
print(tochka.height)
tochka.coord = 25