import matplotlib.pyplot as plt
import numpy as np

#задание 1

def f(x, alpha, beta):
  return (x**beta+alpha**beta)/x**beta

fig, axs = plt.subplots(1, 3, figsize=(14, 4), layout="constrained")

a = 0
left = np.linspace(-10, a-0.01, 2000)
right = np.linspace(a+0.01, 10, 2000)

for i in range(3):
  axs[i].set_xlabel('Частота, с^-1', fontsize=12)
  axs[i].set_ylabel('f(x)', fontsize=12)
  axs[i].set_ylim(-10,10)
  axs[i].set_title('график функции с точкой разрыва второго рода', fontsize=8)
  axs[i].grid(True)
  for j in range(3):
    if i == 0:
      alpha = 1
      beta = 1
      axs[i].plot(left, f(left, alpha, beta), color="blue")
      axs[i].plot(right, f(right, alpha, beta), color="blue")
    elif i == 1:
      alpha = 2
      beta = 1
      axs[i].plot(left, f(left, alpha, beta), color="blue")
      axs[i].plot(right, f(right, alpha, beta), color="blue")
    elif i == 2:
      alpha = 1
      beta = 2
      axs[i].plot(left, f(left, alpha, beta), color="blue")
      axs[i].plot(right, f(right, alpha, beta), color="blue")

#задание 2

def f(x, alpha, beta):
  return (x**beta+alpha**beta)/x**beta

a = 0
right = np.linspace(a+0.01, 25, 2000)

plt.figure(figsize=(12, 6))
plt.xlabel('Частота, с^-1', fontsize=12)
plt.ylabel('f(x)', fontsize=12)
plt.ylim(0,25)
plt.title("график функции f(x) при x>0")
plt.grid(True)

inset_axes_small = plt.axes([1, 0.6, 0.3, 0.3])
inset_axes_small.set_xlim(0, 5)
inset_axes_small.set_ylim(0, 5)
inset_axes_small.grid(True)


for i in range(3):
  if i == 0:
    alpha = 1
    beta = 1
    plt.plot(right, f(right, alpha, beta), color="blue", label='alpha = 1, beta = 1')
  elif i == 1:
    alpha = 2
    beta = 1
    plt.plot(right, f(right, alpha, beta), color="red", label='alpha = 2, beta = 1')
  elif i == 2:
    alpha = 1
    beta = 2
    plt.plot(right, f(right, alpha, beta), color="purple", label='alpha = 1, beta = 2')

plt.legend()
plt.show()

#задание 3

def f(x, alpha, beta):
  return (x**beta+alpha**beta)/x**beta

a = 0
left = np.linspace(-25, a-0.01, 2000)

plt.figure(figsize=(12, 6))
plt.xlabel('Частота, с^-1', fontsize=12)
plt.ylabel('f(x)', fontsize=12)
plt.ylim(-25,5)
plt.title("график функции f(x) при x<0")
plt.grid(True)

plt.axhline(0, color="black", linestyle="--", linewidth=1, label="f(x) = 0")

inset_axes = plt.axes([0.2, 0.45, 0.3, 0.3])
inset_axes.set_xlim(-25, -10)
inset_axes.set_ylim(-2, 2)
inset_axes.grid(True)

for i in range(3):
  if i == 0:
    alpha = 1
    beta = 1
    plt.plot(left, f(left, alpha, beta), color="blue", label='alpha = 1, beta = 1')
  elif i == 1:
    alpha = 2
    beta = 1
    plt.plot(left, f(left, alpha, beta), color="red", label='alpha = 2, beta = 1')
  elif i == 2:
    alpha = 1
    beta = 2
    plt.plot(left, f(left, alpha, beta), color="purple", label='alpha = 1, beta = 2')

plt.legend()
plt.show()
