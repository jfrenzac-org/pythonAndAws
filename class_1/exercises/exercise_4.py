"""
Write a program that asks the user for their age and classifies
 them into groups:

0-12 years: Child

13-19 years: Teenager

20-64 years: Adult

65 or more: Senior
"""
age = input ("Ingrese su edad: ")

try:
    age = int(age)
    if age < 0:
        print("La edad no puede ser un número negativo")
    elif age >= 0 and age <= 12:
        print(f"El usuario con una edad de {age} años es un/una niño/a ")
    elif age > 12 and age <= 19:
        print(f"El usuario con una edad de {age} años es un/una adolescente ")
    elif age > 19 and age < 64:
        print(f"El usuario con una edad de {age} años es un/una adulto/a ")
    else:
        print(f"El usuario con una edad de {age} años es un/una adulto/a mayor ")
except:
    print("La edad solo puede ser un número entero ")
    
