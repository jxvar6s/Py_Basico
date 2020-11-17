#!/usr/bin/env python3

# JulianV
# Oct 22, 2020.
# best practice usin __main__
# Dividing in small task the program to work
# independently.

from time import sleep

print("This is my file to demostrate best practice.")

def process_data(data):
    print("Beginning data processing..")
    modified_data = data + " that has been modified."
    sleep(3)
    print("Data processing finished.")
    return modified_data

def main():
    data = "My data read from the web"
    print(data)
    modified_data = process_data(data)
    print(modified_data)

if __name__ == "__main__": # starting point in python.
    # data = "My data read from the web"
    # print(data)
    # modified_data = process_data(data)
    # print(modified_data)
    main()
    