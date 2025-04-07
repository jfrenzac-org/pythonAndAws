"""
Write a program that asks the user for their age and classifies
 them into groups:

0-12 years: Child

13-19 years: Teenager

20-64 years: Adult

65 or more: Senior
"""

# Taking user input
age_group = float(input("Please write the age in numbers (0-100+) to determine age group classification: "))

# Conditions
# it is still possible that the user writes a negative number, so else print an "error message"
if  0 <= age_group <= 12:
    print("Child")
    print("________") 
elif 13 <= age_group <= 19:
    print("Teenager")
    print("________")  
elif 20 <= age_group <= 64:
    print("Adult")
    print("________")
elif age_group >= 65:
    print("Senior")
    print("________")
else:
    print("You did not enter a valid number, please revise your answer")