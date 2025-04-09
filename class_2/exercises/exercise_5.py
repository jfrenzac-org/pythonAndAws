"""Description:
Write a program that takes a dictionary with numerical values and calculates
the average of those values. The dictionary keys are student names, and the values
 are their respective scores.

Concepts Covered: Dictionaries, for loops, values(), sum(), len(), print"""

## Vamos a crear el diccionario:

calificaciones = {"Alberto" : 4.5,
                  "Guillermo" : 4.8,
                  "Nicolás" : 4.0,
                  "Gabriela" : 4.6,
                  "Martín" : 3.7} 

## nombres = clave
## calificaciones = valor

print(list(calificaciones.values()))
    
Total = sum(calificaciones.values())

Cantidad = len(calificaciones)

Promedio = Total/Cantidad

print (f"El promedio de calificaciones de los estudiantes es: {Promedio}.")
