#coding: utf­8
num1 = int(input("Escriba un numero: "))
num2 = int(input("Escriba un numero mayor que " + str(num1) + ": "))
while num1 >= num2:
    num2 = int(input(str(num2) + " no es mayor que " + str(num1) + ".otra vez: "))

num3 = float(input("Escriba un numero entre " + str(num1) + " y " + str(num2) + ": "))
cont = 0

while num1 <= num3 <= num2:
    cont += 1
    num3 = float(input("Escriba un numero entre " + str(num1) + " y " + str(num2) + ": "))



if cont == 0:

    print"No has escrito ningún numero entre", num1, "y", str(num2) + "."
if cont == 1:
    print "Has escrito 1 número entre", num1, "y", str(num2) + "."
else:
    print "Has escrito", cont, "numeros entre", num1, "y", str(num2) + "."
