#!/usr/bin/env python3

# JulianV
# Oct 21, 2020.
# Funciones - conceptos basicos.

# def conversacion(mensaje):
#     print("Hola")
#     print("Como estas")
#     print(mensaje)
#     print("Adios")

# def imprimir_mensaje():
#     print("Mensaje especial: ")
#     print("!Estoy aprendienando a usar funciones.!")

# imprimir_mensaje()

# print("\n\n\n\n")

# opcion = int(input("Elige una opcion (1, 2, 3): "))

# if opcion == 1:
#     conversacion("Elegiste la opcion 1")
# elif opcion == 2:
#     conversacion("Elegiste la opcion 2")
# elif opcion == 3:
#     conversacion("Elegiste la opcion 3")
# else:
#     print("Escribe la opcion correcta")

def suma(a, b):
    print("Se suman dos numeros.")
    resultado = a + b
    return resultado

sumatoria = suma(1,5)
print(sumatoria)