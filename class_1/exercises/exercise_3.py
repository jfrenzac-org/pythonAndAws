##"""Write a program that asks the user for a score (0 to 100) and prints the
## corresponding letter grade based on the following scale:

## 90 or more: "A"

## 80 to 89: "B"

## 70 to 79: "C"

## 60 to 69: "D"

## Below 60: "F""
## """

score=int(input("Por favor introduce tu puntaje, debe ser máximo de 100 puntos: "))

if 90<=score:
    print("Tu calificación es: 'A' ")
elif 80<=score<90:
    print("Tu calificación es: 'B' ")
elif 70<=score<80:
    print("Tu calificación es: 'C' ")
elif 60<=score<70:
    print("Tu calificación es: 'D' ")
else:
    print("Tu calificación es: 'F' ")
    
   