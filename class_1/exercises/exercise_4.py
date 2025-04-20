"""
Write a program that asks the user for their age and classifies
 them into groups:

0-12 years: Child

13-19 years: Teenager

20-64 years: Adult

65 or more: Senior
"""
numero=int(input("Escriba su edad: "))

if(numero<=12 and numero>=0):
    print("Child")
elif(numero<=19 and numero>=13):
    print("Teenager")
elif(numero<=64 and numero>=20):
    print("Adulto")
else:
    print("Senior")