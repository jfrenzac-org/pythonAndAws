##"""Write a program that asks the user for a username and password.
##Check if they match a predefined username and password,
##then display whether the login was successful or not.
##"""

## Mostrar las credenciales pre definidas
USUARIO_PREDEFINIDO = "MIGUELRENZA"
CONTRASEÑA_PREDEFINIDA = "12228"

## Solicitar credenciales al usuario
usuario = input("Introduce tu nombre de usuario: ")
contraseña = input("Introduce tu contraseña: ")

if usuario.upper() == USUARIO_PREDEFINIDO and contraseña == CONTRASEÑA_PREDEFINIDA:
    
    print("Ingreso Exitoso.")

else:

    print(" Tus datos no coinciden, verificalos e intentalo de nuevo.")
