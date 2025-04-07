"""Write a program that asks the user for a username and password.
Check if they match a predefined username and password,
then display whether the login was successful or not.
"""

#Creo la base de datos inicial
users_db = {"usuario 1":"clave1", "usuario 2":"clave2", "usuario 3":"clave3"}

#Almaceno el usuario y contraseña ingresados por el usuario
user_input = input("Ingrese su usuario: ")
user_password = input("Ingre su contraseña: ")

#Creo una lista con con las llaves de la BD inicial
users = users_db.keys()

#Evalúo si el usuario existe y si su contraseña coincide
if user_input in users:
    if user_password == users_db[user_input]:
        print("Ha ingresado con éxito! ")
    else: 
        print("Contraseña incorrecta! ") 
else:
    print(f"El usuario {user_input} no se encuentra en la base de datos ")