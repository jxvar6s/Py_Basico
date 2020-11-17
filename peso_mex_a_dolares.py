#!/usr/bin/env python3

# JulianV
# Oct 17, 2020.
# Conversion de pesos mexicanos a dolares

pesos = float(input("\n\tCuantos pesos tienes? "))
tipo_de_cambio = 21.13
dolares = pesos / tipo_de_cambio
dolares = round(dolares, 3)
print(f"\tTienes {dolares} dolares.")