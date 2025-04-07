"""Combine Names and Ages (zip + enumerate + lists)
Task:
Given two lists: one of names and one of ages.
Print each person with their number (starting from 1) and age,
using zip() and enumerate()."""

names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 22]


for x, (name, age) in enumerate(zip(names, ages)):
    print(f"{x+1}. {name} is {age} years old")

# Example Output:

"""
1. Alice is 25 years old
2. Bob is 30 years old
3. Charlie is 22 years old
"""
