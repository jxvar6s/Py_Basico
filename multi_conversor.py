#!/usr/bin/env python3

# JulianV
# Oct 21, 2020.
# Conversor de moneda 
# Utilizando if-elif-else (conditionals)

menu = """
Bienvenido al conversor de monedas 💰💸

1- Pesos Colombianos
2- Pesos Argentinos
3- Pesos Mexicanos

Elige una opción: """

opcion = input(menu)

if opcion == '1':
    pesos = input("Cuantos pesos colombianos tienes: ")
    pesos = float(pesos)
    valor_dolar = 3812
    dolares = pesos / valor_dolar
    dolares = round(dolares, 3)
    dolares = str(dolares)
    print(f"Tienes ${dolares} dolares.")
elif opcion == '2':
    pesos = input("Cuantos pesos argentinos tienes: ")
    pesos = float(pesos)
    valor_dolar = 65
    dolares = pesos / valor_dolar
    dolares = round(dolares, 3)
    dolares = str(dolares)
    print(f"Tienes ${dolares} dolares.")
elif opcion == '3':
    pesos = input("Cuantos pesos mexicanos tienes: ")
    pesos = float(pesos)
    valor_dolar = 24
    dolares = pesos / valor_dolar
    dolares = round(dolares, 3)
    dolares = str(dolares)
    print(f"Tienes ${dolares} dolares.")
else:
    print("Ingresa una opción correcta por favor.")

