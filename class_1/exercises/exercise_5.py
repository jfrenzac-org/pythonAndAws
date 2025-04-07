"""Write a program that asks the user for a username and password.
Check if they match a predefined username and password,
then display whether the login was successful or not.
"""

users_db = {"usuario 1":"clave1", "usuario 2":"clave2", "usuario 3":"clave3"}

user_input = input("Ingrese su usuario: ")
user_password = input("Ingre su contraseña: ")

users = users_db.keys()

if user_input in users:
    if user_password == users_db[user_input]:
        print("Ha ingresado con éxito! ")
    else: 
        print("Contraseña incorrecta! ")
else:
    print(f"El usuario {user_input} no se encuentra en la base de datos ")