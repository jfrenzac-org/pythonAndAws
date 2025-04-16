"""Description:
Create a program that counts the occurrence of each word in a sentence
 entered by the user. It should store the words and their counts in a dictionary.

Concepts Covered: Dictionaries, for loops, input, print, items()"""

import string


def count_phrase(phrase: str) -> str:
    # Remove punctuation
    translator = str.maketrans("", "", string.punctuation)
    cleaned_phrase = phrase.translate(translator)

    # Normalize and split words
    list_of_words = [word.lower() for word in cleaned_phrase.split()]

    counts = {}

    for word in list_of_words:
        key = word.capitalize()
        counts[key] = counts.get(key, 0) + 1

    return f"The count of words in the given phrase is: {counts}"


if __name__ == "__main__":
    phrase = input("Enter a phrase: ")
    print(count_phrase(phrase))
