import numpy as np
import matplotlib.pyplot as plt
from math import factorial


def flytta_intervall_cos(x):
    x1 = x % (2 * np.pi)

    if 0 <= x1 <= np.pi / 2:
        sgn_cos = 1
        x_reducerad = x1
    elif np.pi / 2 < x1 <= np.pi:
        sgn_cos = -1
        x_reducerad = np.pi - x1
    elif np.pi < x1 <= 3 * np.pi / 2:
        sgn_cos = -1
        x_reducerad = x1 - np.pi
    else:
        sgn_cos = 1
        x_reducerad = 2 * np.pi - x1

    return sgn_cos, x_reducerad


def flytta_intervall_sin(x):
    x1 = x % (2 * np.pi)
    if x1 > np.pi:
        sgn_sin = -1
        x1 = 2 * np.pi - x1
    else:
        sgn_sin = 1
    if x1 > (np.pi / 2):
        x_reducerad = np.pi - x1
    else:
        x_reducerad = x1
    return sgn_sin, x_reducerad


def cos_taylor(x):
    sgn_cos, x = flytta_intervall_cos(x)
    cos_approx = 0
    for n in range(10):
        term = ((-1) ** n) * (x ** (2 * n)) / factorial(2 * n)
        cos_approx += term
    return sgn_cos * cos_approx


def sin_taylor(x):
    sgn_sin, x = flytta_intervall_sin(x)
    sin_approx = 0
    for n in range(10):
        term = ((-1) ** n) * (x ** (2 * n + 1)) / factorial(2 * n + 1)
        sin_approx += term
    return sgn_sin * sin_approx


x_värden = np.linspace(-10, 10, 100000)
cos_skillnad = []
sin_skillnad = []

for x in x_värden:
    cos_taylor_värde = cos_taylor(x)
    sin_taylor_värde = sin_taylor(x)

    cos_numpy_värde = np.cos(x)
    sin_numpy_värde = np.sin(x)

    skillnad_cos = abs(cos_taylor_värde - cos_numpy_värde)
    skillnad_sin = abs(sin_taylor_värde - sin_numpy_värde)

    cos_skillnad.append(skillnad_cos)
    sin_skillnad.append(skillnad_sin)

plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.plot(
    x_värden, cos_skillnad, label=f"abs(taylor_cos - np.cos) p = 20 ", color="blue"
)
plt.title("Skillnaden mellan taylorserien och numpys värde för cos")
plt.xlabel("x")
plt.ylabel("Skillnad")
plt.grid(True)
plt.legend(loc="upper right")

plt.subplot(1, 2, 2)
plt.plot(x_värden, sin_skillnad, label=f"abs(taylor_sin - np.sin) p = 21", color="red")
plt.title("Skillnaden mellan taylorserien och numpys värde för sin")
plt.xlabel("x")
plt.ylabel("Skillnad")
plt.grid(True)
plt.legend(loc="upper right")
plt.tight_layout()
plt.show()
