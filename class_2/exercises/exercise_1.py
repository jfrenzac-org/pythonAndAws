"""Description:
Create a program that accepts a list of numbers from the user (comma-separated) and calculates the
sum of only the odd numbers in that list.

Concepts Covered: Lists, for loops, input, print"""

String=input("Escriba una lista de números separada por comas ")

Lista=list(String.split(','))

Suma=int(0);

for i in range(len(Lista)):
    
    
    if(Lista[i]!=","and int(Lista[i])%2!=0):
      Suma=Suma+int(Lista[i])
      
print(Suma)