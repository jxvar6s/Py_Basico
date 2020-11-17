#!/usr/bin/env python3

# JulianV
# Oct 22, 2020.
# Defining main functions in python

def messages():
    print("This file is to test Python's execution methods.")
    print("The variable __name__ tells me which context this file is running in.")
    print("The value of __name__ is:", repr(__name__))

def main():
    print("\nHello World!")
    messages()


if __name__ == "__main__":
    main()