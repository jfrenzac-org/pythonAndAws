"""Description:
Create a program that counts the occurrence of each word in a sentence
 entered by the user. It should store the words and their counts in a dictionary.

Concepts Covered: Dictionaries, for loops, input, print, items()"""

#Inicializo mi diccionario contador de palabras
word_counter = {}

"""
Recibo la lista de palabras del usuario y remuevo espacios en blanco
antes y después de la lista de palabras y la transformo en minúscula
para facilitar la copmparación
"""
user_input = input("Ingrese una cadena de palabras: ").strip().lower()

#Separo las palabras por espacios
words = user_input.split(" ")

"""
Creo una lista que me ayuda a eliminar los " " que se pueden generar si el usuario
ingresa un dos espacios o mas entre avrias palabras
"""
clean_words = []
for word in words:
    if word != "":
        clean_words.append(word)

#Creo un ciclo que evalúa y cuenta las palabras
for word in words:
    if word in word_counter:
        word_counter[word] +=1
    else:
        word_counter[word] = 1

#imprimo el resultado    
print(word_counter)
    

