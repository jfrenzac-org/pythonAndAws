"""Description:
Create a program that accepts a list of numbers from the user (comma-separated) and calculates the
sum of only the odd numbers in that list.

Concepts Covered: Lists, for loops, input, print"""

#Recibo del usuario la lista de números
user_num_list = input("Ingrese la lista de números separados por una coma: ")

#Separo los valores ingresado por comas
str_num_list = ((user_num_list.split(',')))

#Creo la variable que almacena la sumatoria
sum_temp = 0

#Este ciclo recorre todos los valores ingresados
for num in str_num_list:
    #Este try me ayuda a ignorar los valores no numéricos ingresados por el usuario
    try:
        #Convierto a int el valor ingresado por el usuario
        num = int(num.strip())
        #Obtengo el residuo para saber si el número es o no par
        if num%2 == 1:
            sum_temp += num
    except:
        print(f"{num} no es un número válido. Solo se pueden ingresar números")

#Imprimo el resultado de la suma
print(f" La suma de los valores impares de los números ingresados es: {sum_temp}")

