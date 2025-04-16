"""Combine Names and Ages (zip + enumerate + lists)
Task:
Given two lists: one of names and one of ages.
Print each person with their number (starting from 1) and age,
using zip() and enumerate()."""

# Your code here


def combine_list(names: list, ages: list):
    output = ""
    for i, name_age in enumerate(zip(names, ages), start=1):
        output += f"{i}. {name_age[0]} is {name_age[1]} years old\n"
    return output


if __name__ == "__main__":
    names = ["Alice", "Bob", "Charlie"]
    ages = [25, 30, 22]
    print(combine_list(names, ages))


# Example Output:

"""
1. Alice is 25 years old
2. Bob is 30 years old
3. Charlie is 22 years old
"""
