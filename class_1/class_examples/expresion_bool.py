# and -- Intersección
# or -- Unión

# El programa me debe decir si tengo que levantarme para ir al trabajo
# Trabajar de lunes-viernes
# Todos los días entra al trabajo a las 8am
# Miércoles entra al trabajo a las 9am
# Programa dará aviso de levantarse 1 hora antes del ingreso

dias_de_semana = ["L", "M", "W", "J", "V"]
dia = input("¿Qué día es?: ")
hora = input("¿Qué hora es?: ")

if dia in dias_de_semana and hora == "7" and dia != "W":
    print("Levantate para entrar a las 8 am")
elif dia == "W" and hora == "8":
    print("Levantate para entrar a las 9am")
else:
    print("Ya llegó tarde al trabajo!")
