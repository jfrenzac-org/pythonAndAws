"""
list.append()
list.extend()
list.sort()
list.copy()
len()
"""

# list.sort()

numeros_asc = [1, 2, 3, 4, 5]
numeros_desc = numeros_asc.copy()

numeros_desc.sort(reverse=True)

print(numeros_asc)
print(numeros_desc)
