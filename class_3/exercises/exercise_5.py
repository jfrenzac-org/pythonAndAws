"""
Ejercicio 5: Buscar palabra en texto
Enunciado:
Crea una función que reciba un texto largo y una palabra, y determine
si esa palabra está contenida dentro del texto. La función debe devolver True o False.

"""
def search_word(text, user_word):
    text = text.strip()
    words_in_text = []
    words_in_text.extend(text.split())
    for word in words_in_text:
        if user_word.lower() == word.lower():
            return True
        else:
            return False
    
text = input("Ingrese el texto base: ").strip()
word = input("Ingrese la palabra a buscar dentro del texto: ").strip()  

print(search_word(text, word))