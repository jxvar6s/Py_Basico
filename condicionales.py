#!/usr/bin/env python3

# JulianV
# Oct 20, 2020.
# Practica de condicionales.

edad = int(input("\nEscribe tu edad: "))

if edad > 17:
    print("Eres mayor de edad.\n")
else:
    print("Eres menor de edad.\n")

print('\n\n')
print("-".center(50, '-'))
numero = int(input("\nEscribe un numero: "))

if numero > 5:
    print("Es mayor que 5")
elif numero == 5:
    print("Es igual a 5")
else:
    print("Es menor a 5")