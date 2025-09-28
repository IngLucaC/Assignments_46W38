# Task_two.py
import string

filename = "The_Zen_of_Python.txt"


def count_words(filename):
    """Count the number of words in the given text file"""
    try:
        with open(filename, "r", encoding="utf-8") as file:
            text = file.read()

            # Create a translation table to remove punctuation
            translator = str.maketrans("", "", string.punctuation)

            # Remove punctuation from the text
            clean_text = text.translate(translator)
            # print(clean_text)  # Optional: print the cleaned text

            words = clean_text.split()
            num = len(words)
            print(f"The title of the file is: {filename}")
            print(f"The text contains {num} words.")

    except FileNotFoundError:
        print(f"Error: File {filename} not found.")
        return None


count_words(filename)
