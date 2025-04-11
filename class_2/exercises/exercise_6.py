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

## A partir del diccionario dado, con las credenciales predefinidas:

credenciales_usuario = {
                    "alice": "1234",
                    "bob": "qwerty",
                    "carol": "pass"
}

## Creamos un nuevo diccionario para autenticar cuáles de los usuarios 
## han validado sus credenciales, mediante un loop while

validacion_credenciales = {}

while len(validacion_credenciales) < len(credenciales_usuario):

    username = input("Ingrese su usuario, por favor: ")
    password = input("Ingrese su contraseña, por favor: ")

    if username in credenciales_usuario:
        if username in validacion_credenciales:
            print(f"{username} es válido.")
        elif credenciales_usuario[username] == password:
            print(f"Welcome, {username}!, ingreso exitoso.")

            validacion_credenciales[username] = True
        else:
            print("Contraseña incorrecta, por favor intente de nuevo")

    else:
        print("Nombre de usuario no encontrado. Inténtalo de nuevo.")
    print(validacion_credenciales)
    
print("Todos los usuarios han sido autenticados.")

       
        
        


