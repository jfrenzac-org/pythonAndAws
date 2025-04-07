"""Write a program that asks the user for a score (0 to 100) and prints the
 corresponding letter grade based on the following scale:

90 or more: "A"

80 to 89: "B"

70 to 79: "C"

60 to 69: "D"

Below 60: "F""
"""

user_score = int(input("Ingrese el puntaje en una escala de 0 - 100: "))

try:
    user_score == int(user_score)
except:
    print("Solo se pueden introducir números entre 0 - 100 ")   
if user_score > 100 or user_score < 0:
    print("Sólo se pueden introducir números entre 0 - 100 ")
elif user_score <= 100 and user_score >= 90:
    print(f"La nota correspondiente al puntaje {user_score} es: A")
elif user_score < 90 and user_score >= 80:
    print(f"La nota correspondiente al puntaje {user_score} es: B")
elif user_score < 80 and user_score >= 70:
    print(f"La nota correspondiente al puntaje {user_score} es: C")
elif user_score < 70 and user_score >= 60:
    print(f"La nota correspondiente al puntaje {user_score} es: D")
else:
    print(f"La nota correspondiente al puntaje {user_score} es: F")
