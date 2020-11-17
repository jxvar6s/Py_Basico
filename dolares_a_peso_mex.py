# JulianV
# Oct 17, 2020.
# Conversion de pesos mexicanos a dolares

dolares = float(input("\n\tCuantos dolares tienes? "))
tipo_de_cambio = 20.97
pesos = dolares * tipo_de_cambio
pesos = round(pesos, 3)
print(f"\tTienes {pesos} pesos mexicanos.")