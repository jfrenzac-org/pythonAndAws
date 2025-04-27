"""Description:
Write a program that takes a number as input and prints the multiplication
 table for that number from 1 to 10.

Concepts Covered: for loops, input, print, range"""

String=input("Escriba un nùmero ")

#print(int(String))

for i in range(1,11,1):
    print(String+"x"+str(i)+"="+str(int(String)*i))
   
     