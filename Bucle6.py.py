num= float(input("Escriba el numero l�mite: "))
while num <= 0:
    num = float(input("El l�mite debe ser mayor que 0. Int�ntelo de nuevo: "))

numero = float(input("Escriba un n�mero: "))
suma = 0
suma += numero

while suma < num:
    numero = float(input("Escriba otro n�mero: "))
    suma += numero

print()
print "Ha superado el l�mite. La suma de los n�meros positivos introducidos es", str(suma) + "."
