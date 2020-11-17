#!/usr/bin/env python3

# JulianV
# Oct 21, 2020.
# Conversor de moneda 
# Utilizando if-elif-else (conditionals)

def conversor(tipo_peso, valor_dolar):
    pesos = input(f"Cuantos pesos {tipo_peso} tienes: ")
    pesos = float(pesos)
    dolares = pesos / valor_dolar
    dolares = round(dolares, 3)
    dolares = str(dolares)
    print(f"Tienes ${dolares} dolares.")
    
menu = """
Bienvenido al conversor de monedas 💰💸

1- Pesos Colombianos
2- Pesos Argentinos
3- Pesos Mexicanos

Elige una opción: """

opcion = input(menu)

if opcion == '1':
    conversor("colombianos", 3875)
elif opcion == '2':
    conversor("argentinos", 65)
elif opcion == '3':
    conversor("mexicanos", 24)
else:
    print("Ingresa una opción correcta por favor.")

