"""Description:
Write a program that takes a dictionary with numerical values and calculates
the average of those values. The dictionary keys are student names, and the values
 are their respective scores.


Concepts Covered: Dictionaries, for loops, values(), sum(), len(), print"""

#Creo mi diccionario con las notas para cada estudiante
notes = {"Eliana":[5.0,4.9,4.8,5.0,4.6], "Elena":[4.1,4.0],"Alejandro":[4.2,4.1,4.9,4.0],"Miguel":[3.8,4.8,4.5]}

#Inicializo un diccionario que almacena la nota promedio de cada estudiante
avg_notes = {}

#Creo un ciclo que encuentra la nota promedio de cada estudiante y lo agrega al diccionario de promedios
for student,note in notes.items():
    avg=0
    avg = round((sum(note)/len(note)),2)
    avg_notes[student]=avg
    
print(avg_notes.items())
    