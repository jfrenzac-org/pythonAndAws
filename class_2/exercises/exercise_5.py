"""Description:
Write a program that takes a dictionary with numerical values and calculates
the average of those values. The dictionary keys are student names, and the values
 are their respective scores.

Concepts Covered: Dictionaries, for loops, values(), sum(), len(), print"""


Notas={"Juliet":4.5, "Lina":4.9, "Carlos":2.1, "Arturo":1.8, "Juan":0.2, "Simon":0.5, "Doris":3.7}

#print(Notas)

def get_average(Dict1):

    suma=0
    
    for i,j in Dict1.items():
        suma=suma+j

    return(suma/len(Dict1))    

print(f"El promedio de notas del salón es: {"%.2f" % round(get_average(Notas), 2)}")

