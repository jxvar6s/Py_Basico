#!/usr/bin/env python3

# JulianV
# Oct 30, 2020.
# Using brack and continue

def main():
    #for counter in range(1000):
     #   if counter % 2 != 0:
     #       continue
     #   print(count)
    
    #for i in range(10000):
    #    print(i)
    #    if i == 5678:
    #        break
    
    texto = input("Escribe un text: ")

    for letra in texto:
        if letra == 'o':
            break
        print(letra)


if __name__ == '__main__':
    main()
