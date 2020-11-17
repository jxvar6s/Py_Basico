#!/usr/bin/env python3

# JulianV
# Nov 8, 2020.
# Given the string, remove the characters up to 
# the given integer.

def remove_chars(text, index_number):
    if index_number < len(text):
        new_text = text[index_number::]
        print(f"\n\tYour new text is: {new_text}.")
    else:
        print("\nYour number is lager than the length of your text.")
        print("Thanks...\n")

def input_text():
    text = input("Enter your text: ")
    number = int(input("Enter your limit number: "))
    return text, number

def description():
    title = """
    Given a string and an integer number n, 
    remove characters from a string starting 
    from zero up to n and return a new string.
    """
    print(title)

def main():
    description()
    text, number = input_text()
    remove_chars(text, number)


if __name__ == "__main__":
    main()