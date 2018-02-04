num= float(input("Escriba el numero límite: "))
while num <= 0:
    num = float(input("El límite debe ser mayor que 0. Inténtelo de nuevo: "))

numero = float(input("Escriba un número: "))
suma = 0
suma += numero

while suma < num:
    numero = float(input("Escriba otro número: "))
    suma += numero

print()
print "Ha superado el límite. La suma de los números positivos introducidos es", str(suma) + "."
