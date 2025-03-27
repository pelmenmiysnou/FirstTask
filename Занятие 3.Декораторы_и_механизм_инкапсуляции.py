class BankAccount:
  def __init__(self, balance, account_number):
    self.__balance = balance
    self.__account_number = account_number

  def deposit(self, amount):
    if self.valid_balance(amount):
      self.__balance += amount
    else:
      print(">0!!!")
    return self.__balance

  def withdraw(self, amount):
    if self.valid_balance(amount) and amount <= self.__balance:
      self.__balance -= amount
    else:
      print("netu deneg!")
    return self.__balance

  def get_balance(self):
    return self.__balance

  @staticmethod
  def valid_balance(amount):
    return isinstance(amount, (int, float)) and amount > 0

  @classmethod
  def new_acc(cls, account_number):
    return cls(0, account_number)

acc = BankAccount.new_acc("9921")
acc.deposit(200)
print(acc.get_balance())




class User:
  def __init__(self, username, password):
    self.__username = username
    self.__password = password

  def get_username(self):
    return self.__username

  @staticmethod
  def diff_password(password):
    if len(password) < 6:
      return False
    return True

  @classmethod
  def create_default_user(cls, username):
    default_password = "94123bp"
    return cls(username, default_password)

  def set_password(self, new_password):
      if self.diff_password(new_password):
        self.__password = new_password
        print(f"your new password is:{new_password}")
      else:
        print("please change password")

acc = User.create_default_user("Misha_killer")
print(acc.get_username())
acc.set_password("901")




class Book:
  def __init__(self, title, author, year):
    if self.year_of_writing(year):
      self.__title = title
      self.__author = author
      self.__year = year
    else:
      print("wrong year!")

  @staticmethod
  def year_of_writing(year):
    if not isinstance(year, int):
      print("int!")
      return False
    if year > 2025:
      return False
    return True

  @classmethod
  def create_book(cls, title, author):
    default_year = 2025
    return cls(title, author, default_year)

  def get_info(self):
      print(f"title: {self.__title}")
      print(f"author: {self.__author}")
      print(f"year of writing: {self.__year}")

book1 = Book("1984", "George Orwell", 1949)
book1.get_info()
print()
book2 = Book.create_book("Brave New World", "Aldous Huxley")
book2.get_info()