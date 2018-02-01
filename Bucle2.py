#coding: utf­8
num1 = float(input("Escriba un número: "))
num2 = float(input("Escriba un número mayor que " + str(num1) + ": "))

while num2 > num1:
    num2 = float(input("Escriba otro número mayor que " + str(num1) + ": "))

print()
print(num2, "no es mayor que", str(num1) + ".")
print("Programa terminado")


