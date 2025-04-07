"""
Write a program that asks the user for their age and classifies
 them into groups:

0-12 years: Child

13-19 years: Teenager

20-64 years: Adult

65 or more: Senior
"""

#Almaceno la edad ingresada por el usuario
age = input ("Ingrese su edad: ")

#Con este try aseguro que el valor ingresado sea numérico
try:
    age = int(age)
    #Evalúo cada posible rango de edad
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
#Con este except manejo los valores no numéricos ingresados por el usuario
except:
    print("La edad solo puede ser un número entero ")
    
