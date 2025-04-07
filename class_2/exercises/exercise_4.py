"""Description:
You are given two lists: one with keys and the other with values.
Create a dictionary by pairing the elements of the two lists.

Concepts Covered: Lists, dictionaries, for loops, zip(), items()"""

#Creo la lista de llaves y valores
keys_list = [1,2,3,4,5,6,7,8,9,10]
values_list = [2,4,6,8,10,12,14,16,18,20]

#Inicializo mi diccionario
dict={}

#Ciclo for para llenar mi diccionario
for keys, values in zip(keys_list,values_list):
    dict[keys] = values
print(dict)