"""Write a program that asks the user for a username and password.
Check if they match a predefined username and password,
then display whether the login was successful or not.
"""


Usuario="Esteban"
Clave="1234"


Usuario_Get=input("Escriba su usuario: ")
Clave_Get=input("Escriba su clave: ")


if(Usuario_Get==Usuario and Clave_Get==Clave):
    print("Login Successful ")
else:
    print("Clave o Usuario incorrecto")