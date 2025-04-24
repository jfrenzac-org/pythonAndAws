"""Description:
Create a program that counts the occurrence of each word in a sentence
 entered by the user. It should store the words and their counts in a dictionary.

Concepts Covered: Dictionaries, for loops, input, print, items()"""

String=input("Escriba una frase ")

Lista=list(String.split(' '))

Contador=int(0)
Dic={}

#print(Lista)

for i in range(len(Lista)):
    for j in range(len(Lista)):
        if(Lista[i]==Lista[j]):
            Contador=Contador+1
    Dic[Lista[i]]=Contador
    Contador=0

print(Dic)
