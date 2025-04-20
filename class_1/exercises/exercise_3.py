"""Write a program that asks the user for a score (0 to 100) and prints the
 corresponding letter grade based on the following scale:

90 or more: "A"

80 to 89: "B"

70 to 79: "C"

60 to 69: "D"

Below 60: "F""
"""

numero=int(input("Escriba un número entre 0 y 100: "))

if(numero<60):
    print("F")
elif(numero>=60 and numero<=69):
    print("D")
elif(numero>=70 and numero<=79):
    print("C")
elif(numero>=80 and numero<=89):
    print("B")
elif(numero>=90 and numero<=100):
    print("A")        
else:
    print("El número no esta entre 0 y 100")