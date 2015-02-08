GS = float(input("Velocidad GS: "))
MNRestantes = float(input("Millas restantes: "))

gsPM = GS / 60
subTotal = MNRestantes / gsPM
total = subTotal / 60

print ("Faltan " + str(subTotal) + " minutos aproximadamente")
print ("Faltan " + str(total) + " horas aproximadamente")

input()
