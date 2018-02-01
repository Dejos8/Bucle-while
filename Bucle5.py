#coding: utf­8
num = int(input("Escriba un número: "))
suma = 0
while num > 0:
    suma += num
    num = int(input("Escriba otro número: "))

print "La suma de los números positivos introducidos es", str(suma) + "."

