#coding: utf­8
num= int(input("Escriba un número : "))
while numero % 2 != 0:
    numero = int(input(str(num) + " no es un número par. Inténtelo de nuevo: "))
contador = 1
respuesta = input("¿Quiere escribir otro número par? (S/N) ")

while respuesta == "Y":
    num= int(input("Escriba un número par: "))
    while num % 2 != 0:
        num = int(input(str(num) + " no es un número par. Inténtelo de nuevo: "))
    cont += 1
    respuesta = input("¿Quiere escribir otro número par? (Y/N) ")

if cont== 0:
    print("No ha escrito ningún número par")
elif cont== 1:
    print("Ha escrito 1 número par")
else:
    print("Ha escrito", cont, "números pares.")

