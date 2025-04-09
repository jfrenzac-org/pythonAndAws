## Description:
## Create a program that counts the occurrence of each word in a sentence entered by the user. 
## It should store the words and their counts in a dictionary.

##Concepts Covered: Dictionaries, for loops, input, print, items()"""

## pedimos al usuario que digite una frase.
frase = input("Ingresa una frase: ").lower()

## Separamos la frase en palabras y la convertimos toda a minúsculas. 
## Luegp creamos una lista a partir de la frase.

list_palabras = frase.split()
print(list_palabras)

## creamos un diccionario vacio para las frecuencia de cada palabra en la lista.

frecuencia = {}
    
for palabra in list_palabras:
    if palabra in frecuencia:
            frecuencia[palabra] += 1
    else:
        frecuencia[palabra] = 1
  
print(frecuencia)






