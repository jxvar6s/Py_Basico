#!/usr/bin/env python3

# JulianV
# Oct 30, 2020.
# Recorriendo texto (strings)

def main():
    nombre = input("Escribe tu nombre: ")

    for letra in nombre:
        print(letra.capitalize())

if __name__ == '__main__':
    main()
