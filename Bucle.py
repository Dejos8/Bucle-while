#coding: utf­8
uno = int(input("Escriba un número: "))
dos = int(input("Escriba un número mayor que  " + str(uno) + ": "))

while dos <= uno:
    print(dos, "no es mayor que", str(uno) + ". Inténtelo de nuevo:")
    dos = int(input())

print "Los números que ha escrito son", uno, "y", dos
print("Programa terminado")
