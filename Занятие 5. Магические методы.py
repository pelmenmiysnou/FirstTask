class Fraction:
  def __new__(cls, chislitel, znamenatel):
    if not isinstance(chislitel, int) or not isinstance(znamenatel, int):
      raise TypeError("int!")
    if znamenatel == 0:
      raise ValueError("zero division!")
    return super().__new__(cls)


  def __init__(self, chislitel, znamenatel):
    self._chislitel = chislitel
    self._znamenatel = znamenatel

  def __repr__(self):
    return f"{self._chislitel}/{self._znamenatel}"

  @property
  def chislitel(self):
    return self._chislitel

  @property
  def znamenatel(self):
    return self._znamenatel

  @property
  def value(self):
    return round(self._chislitel / self._znamenatel,3 )

  def __add__(self, other):
    upper = self._chislitel * other.znamenatel + other.chislitel * self._znamenatel
    lower = self._znamenatel * other.znamenatel
    return Fraction(upper, lower)

  def __sub__(self, other):
    upper = self._chislitel * other.znamenatel - other.chislitel * self._znamenatel
    lower = self._znamenatel * other.znamenatel
    return Fraction(upper, lower)

  def __mul__(self, other):
    upper = self._chislitel * other.chislitel
    lower = self._znamenatel * other.znamenatel
    return Fraction(upper, lower)

  def __truediv__(self, other):
    upper = self._chislitel * other.znamenatel
    lower = self._znamenatel * other.chislitel
    return Fraction(upper, lower)

# f1 = Fraction(10, -11)
# f2 = Fraction(11, -10)
# print(f1 + f2)
# print(f1 - f2)
# print(f1 * f2)
# print(f1 / f2)
# print(f1.value)
# f3 = f1/f2
# print(f3.value)




class FractionMatrix:
  def __new__(cls, matrix):
    if not isinstance(matrix, list) or not matrix:
      raise ValueError("empty list")
    for row in matrix:
      if not isinstance(row, list):
        raise TypeError("string not is list")
    instance = super().__new__(cls)
    return instance

  def __init__(self, matrix):
    self.matrix = matrix
    # self.rows = len(matrix)
    # self.cols = len(matrix[0]) if self.rows > 0 else 0

  def __str__(self):
    return "\n".join(" ".join(str(elem) for elem in row) for row in self.matrix)

  @property
  def rows(self):
    return len(self.matrix)

  @property
  def cols(self):
    return len(self.matrix[0]) if self.rows > 0 else 0

  def __add__(self, other):
    result = []
    if not isinstance(other, FractionMatrix):
      return NotImplemented
    if self.rows != other.rows or self.cols != other.cols:
      raise ValueError("different size of matrix")
    for i in range(self.rows):
      stroka = []
      for j in range(self.rows):
        stroka.append(self.matrix[i][j] + other.matrix[i][j])
      result.append(stroka)
    return FractionMatrix(result)

  def __sub__(self, other):
    result = []
    if not isinstance(other, FractionMatrix):
      return NotImplemented
    if self.rows != other.rows or self.cols != other.cols:
      raise ValueError("different size of matrix")
    for i in range(self.rows):
      stroka = []
      for j in range(self.rows):
        stroka.append(self.matrix[i][j] - other.matrix[i][j])
      result.append(stroka)
    return FractionMatrix(result)

  def __mul__(self, other):
    result = []
    for i in range(self.rows):
      stroka = []
      for j in range(other.cols):
        elem = 0
        for k in range(self.cols):
          elem += self.matrix[i][k] * other.matrix[k][j]
        stroka.append(elem)
      result.append(stroka)
    return FractionMatrix(result)

  def transp(self):
    result = []
    for i in range(self.rows):
      stroka = []
      for j in range(self.rows):
        stroka.append(self.matrix[j][i])
      result.append(stroka)
    return FractionMatrix(result)

  def det(self):
    return f"{self.matrix[0][0]*self.matrix[1][1]-self.matrix[0][1]*self.matrix[1][0]}"


m1 = FractionMatrix([[Fraction(1, 2), Fraction(1, 3)], [Fraction(2, 5), Fraction(3, 4)]])
m2 = FractionMatrix([[Fraction(1, 3), Fraction(2, 3)], [Fraction(1, 2), Fraction(2, 5)]])
print(m1+m2)
print()
print(m1-m2)
print()
print(m1)
print()
print(m1.transp())
print()
print(m1.det())
print()
print(m1*m2)