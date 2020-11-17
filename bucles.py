#!/usr/bin/env python3

# JulianV
# Oct 23, 2020.
# while loop

def run():
    LIMETE = 1000000
    
    contador = 0 
    potencia_2 = 2**contador
    while potencia_2 < LIMETE:
        print(f"2 elevado a {contador} es igual a: {potencia_2}")
        contador += 1
        potencia_2 = 2**contador


if __name__ == "__main__":
    run()