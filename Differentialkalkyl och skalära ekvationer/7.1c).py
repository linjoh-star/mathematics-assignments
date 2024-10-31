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


def cos_taylor(x, tol):
    sgn_cos, x = flytta_intervall_cos(x)
    cos_approx = 0
    n = 0
    fel_lista = []
    iterationer = []
    cos_numpy = np.cos(x)
    while True:
        term = ((-1)**n) * (x**(2*n)) / factorial(2*n)
        cos_approx += term
        error = abs(sgn_cos * cos_approx - cos_numpy)
        fel_lista.append(error)
        iterationer.append(n)
        if error < tol:
            break
        n += 1
    return sgn_cos * cos_approx, iterationer, fel_lista


def sin_taylor(x, tol):
    sgn_sin, x = flytta_intervall_sin(x)
    sin_approx = 0
    n = 0
    fel_lista = []
    iterationer = []
    sin_numpy = np.sin(x)
    while True:
        term = ((-1)**n) * (x**(2*n + 1)) / factorial(2*n + 1)
        sin_approx += term
        error = abs(sgn_sin * sin_approx - sin_numpy)
        fel_lista.append(error)
        iterationer.append(n)
        if error < tol:
            break
        n += 1
    return sgn_sin * sin_approx, iterationer, fel_lista


x = 1
tol = 1e-15

cos_value, iterationer_cos, fel_lista_cos = cos_taylor(x, tol)
iterationer_needed_cos = len(iterationer_cos)

sin_value, iterationer_sin, fel_lista_sin = sin_taylor(x, tol)
iterationer_needed_sin = len(iterationer_sin)


polgrad_cos = [2 * n for n in iterationer_cos]
polgrad_sin = [2 * n + 1 for n in iterationer_sin]

plt.figure(figsize=(12, 6))


plt.subplot(1, 2, 1)
plt.semilogy(polgrad_cos, fel_lista_cos, marker="o",
             color="blue", label="cos(1)")
plt.title("Mängd polynomgrader för TOL > |numpy - taylor|")
plt.xlabel("Polynomgrad")
plt.ylabel("Felets storlek")
plt.grid(True)
plt.legend()

plt.subplot(1, 2, 2)
plt.semilogy(polgrad_sin, fel_lista_sin, marker="o",
             color="red", label="sin(1)")
plt.title("Mängd polynomgrader för TOL > |numpy - taylor|")
plt.xlabel("Polynomgrad")
plt.ylabel("Felets storlek")
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()
