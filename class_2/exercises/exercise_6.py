"""
Password Checker (While Loop + Input + Dictionary)

Task:
Create a dictionary with usernames as keys and passwords as values.
Ask the user to input their username and password.
Keep prompting until the user provides correct credentials.

"""

"""Goal: Use a while loop to keep checking user input
until the correct username and password are entered."""

# Your code here

## A partir del diccionario dado, como credenciales predefinidas:
credentials_user = {
                    ".alice": ".1234",
                    ".bob": ".qwerty",
                    ".carol": ".pass"
}

while True:
    username = input("Ingrese su usuario, por favor: ")
    password = input("Ingrese su contraseña, por favor: ")

    if username in credentials_user and credentials_user[username] == password:
        print("Ingreso exitoso")
        break
    else:
        print("Sus datos no corresponden, por favor intente de nuevo.")
        


