## """
## Write a program that asks the user for their age and classifies
 ## them into groups:

## 0-12 years: Child

## 13-19 years: Teenager

## 20-64 years: Adult

## 65 or more: Senior
# 
# 
Age=int(input("Por favor, introduce tu edad: "))
if Age <0:
    print("Edad no válida, ingresa tu edad real")
elif Age <13:
    print("Oh, !Si eres un child!")
elif 12<Age <20:
    print("Ah, !ya eres todo un teenager!")
elif 19<Age<65:   
    print("!Ya eres un adulto!")            
else: 
    print("!Ya estás en la edad Senior!")
