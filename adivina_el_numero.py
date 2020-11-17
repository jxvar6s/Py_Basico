#!/usr/bin/env python3

# JulianV
# Nov 3, 2020.
# utlizando el modulo random

import random

def main():
    numero_aleatorio = random.randint(1, 100)
    numero_elegido = int(input("Elige un numerodel 1 al 100: "))

    while numero_elegido != numero_aleatorio:
        if numero_elegido < numero_aleatorio:
            print("Busca un numero mas grande: ")
        else:
            print("Busca un numero mas pequeno: ")
        numero_elegido = int(input("Elige otro numero: "))
    
    print("Ganaste...")

if __name__ == "__main__":
    main()