import math
import matplotlib.pyplot as plt
import numpy as np

class Derivative:
  def __init__(self, h = 10**(-5)):
    self.h = h

  def __get__(self, instance, owner):
    def derivative_func(x):
      h = self.h
      return (instance(x + h) - instance(x - h)) / (2 * h)
    return derivative_func

class ExponentialFunction:
  derivative = Derivative()

  def __init__(self, a):
    self.a = a

  def __call__(self, x):
    return self.a * math.exp(x)


exp_func = ExponentialFunction(a = 2)
# print(exp_func(0))
# print(exp_func.derivative(0))

x_vals = np.linspace(-2, 2, 2000)
f_vals = [exp_func(x) for x in x_vals]
df_vals = [exp_func.derivative(x) for x in x_vals]

plt.figure(figsize=(12, 6))
plt.plot(x_vals, f_vals, label="f(x) = 2exp[x]")
plt.plot(x_vals + 1, df_vals, label="f`(x) + 1")
plt.xlabel("x")
plt.ylabel("y")
plt.title("График ф-ции f(x) и  f`(x)")
plt.legend()
plt.grid(True)
plt.show()