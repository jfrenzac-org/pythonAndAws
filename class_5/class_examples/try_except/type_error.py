"""
TypeError try - except
"""

try:
    print(2 + "2")
except TypeError:
    print("No es posible sumar 'int' y 'str'")
