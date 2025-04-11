"""Combine Names and Ages (zip + enumerate + lists)
Task:
Given two lists: one of names and one of ages.
Print each person with their number (starting from 1) and age,
using zip() and enumerate()."""

names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 22]

# Your code here

# Example Output:

"""
1. Alice is 25 years old
2. Bob is 30 years old
3. Charlie is 22 years old
"""

## Creamos un inventario a partir de las dos listas, nombres y edades.

names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 22]

## Utilizamos el loop for para relacionar los nombres con las edades y 
## la función enumerate para mostrar la lista ordenada.

for i, (name, age) in enumerate(zip(names, ages), start = 1):
    print(f"{i}. {name} is {age} years old")