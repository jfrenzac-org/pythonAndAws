"""Number List Builder (While Loop + List)
Task:
Ask the user to input numbers (as integers).
Add each number to a list.
Stop asking when the user types "done".
Then, print the list of numbers and their total sum."""

"""Goal: Use a while loop to collect input and store it in a list."""

num_sum = 0
while True:
    num_list = []    
    try:
        num = input("Ingrese un número entero: ")
        if num.lower() == "done":
            break
        else:
            num_list.append(int(num)) 
            num_sum += int(num)    
    except:
        print("Sólo se pueden ingresar números enteros")
    
print(f"la suma de los números ingresados es: {num_sum}")