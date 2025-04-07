"""Write a program that asks the user for a score (0 to 100) and prints the
 corresponding letter grade based on the following scale:

90 or more: "A"

80 to 89: "B"

70 to 79: "C"

60 to 69: "D"

Below 60: "F""
"""

# Taking user input
score = int(input("Please write a score from 0 to 100 and we will determine the student's grade: "))

# Conditions
# it is still possible that the user writes a negative number, so else print an "error message"
if   score >= 90:
    print("The grade is A")
    print("________") 
elif 80 <= score <= 89:
    print("The grade is B")
    print("________")  
elif 70 <= score <= 79:
    print("The grade is C")
    print("________")
elif 60 <= score <= 69:
    print("The grade is D")
    print("________")
elif 0 <= score <= 60:
    print("The grade is E")
    print("________")
else:
    print("You did not enter a valid number, please revise your answer")