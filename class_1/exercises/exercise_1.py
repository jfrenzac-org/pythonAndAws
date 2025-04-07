# Write a program that asks the user for a number and classifies it as
# positive, negative, or zero.

#Creo un ciclo try para analizar si el usuario ingresa un número
try:
    string_num = input("Ingrese un número entero ")
    #Convierto el input del usuario en tipo int
    num = int(string_num)
    #Analizo los 3 posibles casos:; negativo, cero y positivo
    if num < 0:
        print(f"El número {num} es negativo")
    elif num == 0:
        print(f"El número ingresado es igual a cero")
    else:
        print(f"El número {num} es positivo")
#Con este except manejo los valores no numéricos ingresados por el usuario        
except:
    print("Solo se pueden ingresar números")  
    
