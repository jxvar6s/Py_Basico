#!/usr/bin/env python3

pesos = input("Cuantos pesos colombianos tienes: ")
pesos = float(pesos)
valor_dolar = 3812
dolares = pesos / valor_dolar
dolares = round(dolares, 3)
dolares = str(dolares)
print(f"Tienes ${dolares} dolares.")