#coding: utf­8
num1= int(input("Escriba un número: "))
num2 = int(input("Escriba un número mayor que " + str(num1) + ": "))

while num2 > num1:
    num1 = num2
    num2= int(input("Escriba un número mayor que " + str(num1) + ": "))

print(num2, "no es mayor que", str(num1) + ".")
print("Programa terminado")


