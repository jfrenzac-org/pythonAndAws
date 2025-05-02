"""Description:
You are given two lists: one with keys and the other with values.
Create a dictionary by pairing the elements of the two lists.

Concepts Covered: Lists, dictionaries, for loops, zip(), items()"""


Lista_keys=["abc","def","ghi","jkl","mno"]
Lista_values=[25,32,456,987,6]
Dict={}

#Sin usar zip()

def paring_list(Lista1,Lista2):

    
    if(len(Lista1)!=len(Lista2)):
        print(f"Las listas nos son del mismo tamaño. Hay {len(Lista1)} elementos en keys y {len(Lista2)} en values.")

    else:
        for i in range(len(Lista1)):
            Dict[Lista_keys[i]]=Lista_values[i]

    return Dict

    
print(paring_list(Lista_keys,Lista_values))

#Usando zip(). Aparea las listas hasta la posición que se apareable sin importar tamaño listas

Dict=dict(zip(Lista_keys,Lista_values))
print(Dict)

