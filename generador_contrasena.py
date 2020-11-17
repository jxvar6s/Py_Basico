#!/usr/bin/env python3

# JulianV
# Nov 4, 2020.
# Generador de contrasena.

import random


def generar_contrasena():
    mayusculas = ['A','B','C','D','E','F','G',
               'H','I','J','K']
    minusculas = ['a','b','c','d','e','f','g']
    numeros = ['0','1','2','3','4','5','6','7','8','9']
    simbolos = ['!','@','#','$','$','%','^','&','*','(',')']

    caracteres = mayusculas + minusculas + numeros + simbolos

    contrasena = []
    for i in range(15):
        caracter_random = random.choice(caracteres)
        contrasena.append(caracter_random)

    contrasena = "".join(contrasena)
    return contrasena


def main():
    contrasena = generar_contrasena()
    print(f"Tunueva contrasena es: {contrasena}")


if __name__ == "__main__":
    main()