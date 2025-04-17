"""
Ejercicio 3: Unir dos listas
Enunciado:
Define una función que reciba dos listas y las combine en una sola usando
el método extend(). La función debe retornar la lista resultante.

"""
def join_list (list1, list2):
    list1.extend(list2)
    return list1

list1 = input("Enter the items of the first list separated by a space: ").split()
list2 = input("Enter the items of the second list separated by a space: ").split()

print(f"The extended list is: {join_list(list1, list2)}")
    
    