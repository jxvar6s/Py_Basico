#!/usr/bin/env python3

# JulianV
# Nov 4, 2020.
# Return a filter list that it only contains int elements.

# Note: It is not the same:
#       return [new_list.append(x) for x in lista if isinstance(x, int)] 
#       than
#       [new_list.append(x) for x in lista if isinstance(x, int)] 
#       return new_list

def filter_list(lista):
    new_list = []
    [new_list.append(x) for x in lista if isinstance(x, int)] 
    return new_list

def main():
    lista1 = filter_list([1,2,3,'a','b'])
    lista2 = filter_list(['a','1','b',2])
    lista3 = filter_list([1,'a',2,'b',9,'x',100])

    print(lista1)
    print(lista2)
    print(lista3)


if __name__ == "__main__":
    main()