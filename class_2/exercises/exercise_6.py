"""
Password Checker (While Loop + Input + Dictionary)

Task:
Create a dictionary with usernames as keys and passwords as values.
Ask the user to input their username and password.
Keep prompting until the user provides correct credentials.

"""

"""Goal: Use a while loop to keep checking user input
until the correct username and password are entered."""

users = {"alice": "1234", "bob": "qwerty", "carol": "pass"}

while True:
    user = input("Ingrese el usuario: ")
    password = input("Ingrese la contraseña")
    
    try:
        if users[user] == password:
            print("Acceso correcto")
            break
    except:
        print("Usuario o contraseña equivocados")
