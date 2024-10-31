import numpy as np
from math import factorial


def cos_taylor(x, antal_termer=10):
    cos_beräkning = 0
    for n in range(antal_termer):
        term = ((-1) ** n * x ** (2 * n)) / factorial(2 * n)
        cos_beräkning += term
    return cos_beräkning


def sin_taylor(x, antal_termer=10):
    sin_beräkning = 0
    for n in range(antal_termer):
        term = ((-1) ** n * x ** (2 * n + 1)) / factorial(2 * n + 1)
        sin_beräkning += term
    return sin_beräkning


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


while True:
    try:
        x = float(input(
            "Vilken vinkel vill du ha i cosinus och sinus (i radianer, valfritt intervall): "))
        break
    except ValueError:
        print("Vänligen ange en giltig vinkel")

tecken_sin, x_flyttad_sin = flytta_intervall_sin(x)
sin_beräkning = sin_taylor(x_flyttad_sin) * tecken_sin

tecken_cos, x_flyttad_cos = flytta_intervall_cos(x)  # Corrected here
cos_beräkning = cos_taylor(x_flyttad_cos) * tecken_cos
numpy_sin = np.sin(x)
numpy_cos = np.cos(x)
print(f"Taylor seriens cos-värde för vinkeln ({x} radianer): {cos_beräkning}")
print(f"numpys värde för cos = {numpy_cos}")
print(f"Taylor seriens sin-värde för vinkeln ({x} radianer): {sin_beräkning}")
print(f"numpys värde för sin = {numpy_sin}")
