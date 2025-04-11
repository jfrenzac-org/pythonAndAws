"""Number List Builder (While Loop + List)
Task:
Ask the user to input numbers (as integers).
Add each number to a list.
Stop asking when the user types "done".
Then, print the list of numbers and their total sum."""

# Your code here

## Creamos una lista vacía para almacenar los valores y declaramos a listo com palabra clave.

mi_lista = []

palabra_clave = ("listo").lower()

## mediante un loop while y las sentencias Try - except verificamos la valides de los datos 
## para almacenarlos en la lista.

while True:
    entrada = input("Ingrese un número entero (o escriba 'listo' para terminar): ")
    if entrada.lower() == palabra_clave:
        break
    try:
        numero = int(entrada)
        mi_lista.append(numero)
        
    except ValueError:

        print("Este no es un dato válido. Por favor vuelva a intentarlo: ")
        
    
print("La lista de numeros es:", mi_lista)
print("Suma Total: ", sum(mi_lista))



## """Goal: Use a while loop to collect input and store it in a list."""
