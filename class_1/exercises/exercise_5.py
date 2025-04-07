"""Write a program that asks the user for a username and password.
Check if they match a predefined username and password,
then display whether the login was successful or not.
"""

# Taking user input
username = input("Please write your username: ")
password = input("Please write your password: ")

# Conditions

if username == "Student01" and password == "HelloWorld" :
    print("Login was successful")
else:
    print("Username and/or password are wrong")