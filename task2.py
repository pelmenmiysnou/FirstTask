class Sauce:
  def __init__(self, taste):
    self.taste = taste

  def show_my_sauce(self):
    if self.taste:
      print(f"sauce: {self.taste}")
    else:
      print("mayonez!")

sauce_out = Sauce(input("input taste "))
sauce_out.show_my_sauce()




class Employee:
  @classmethod
  def validate(cls, name, age, salary, bonus):
    return (
      isinstance(name, str) and
      isinstance(age, int) and
      isinstance(salary, (int, float)) and
      isinstance(bonus, (int, float))
        )

  def __init__(self, name: str, age: int, salary, bonus):
    if self.validate(name, age, salary, bonus):
      self._name = name
      self._age = age
      self._salary = salary
      self._bonus = bonus
    else:
      raise ValueError("Invalid input types: name must be STR type")

  @property
  def get_salary(self):
    return self._salary

  @get_salary.setter
  def get_salary(self, value):
    if self.validate(None, None, value, None):
      self._salary = value
    else:
      raise ValueError("Invalid salary type: salary must be FLOAT type")

  @property
  def get_bonus(self):
    return self._bonus

  @get_bonus.setter
  def set_bonus(self, value):
    if self.validate(None, None, None, value):
      self._bonus = value
    else:
      raise ValueError("Invalid bonus type: bonus must be FLOAT type")

  @property
  def total_salary(self):
    return self._salary + self._bonus

employ = Employee("Sasha", 25, 30000, 3000)
print(employ.__dict__)
print(employ.total_salary)
employ.get_bonus




class Reciple:
  def __init__(self, name, reciple):
    self.name = name
    if isinstance(reciple, str):
      self.reciple = reciple.split(', ')
    else:
      self.reciple = reciple

  def print_ingredients(self):
    print(f"Ингредиент для {self.name}:")
    for ingredient in self.reciple:
      print(f"- {ingredient}")

  def cook(self):
        print(f"Сегодня мы готовим {self.name}.")
        print(f"Выполняем инструкцию по приготовлению блюда {self.name}...")
        print(f"Блюдо {self.name} готово!")

dish = Reciple("pelmeni", "voda, sol")
dish.print_ingredients()
dish.cook()
print()
dish = Reciple("chai", "chainyi_packetik, voda")
dish.print_ingredients()
dish.cook()