# Guard Clause  ---> Concepto

usuario = input("ingrese su usuario: ")
password = input("Ingrese la contraseña: ")

if password is None:
    print("Debe ingresar una contraseña")

if 2 == 2:
    print("verdadero")
elif 3 == 3:
    pass
else:
    pass
