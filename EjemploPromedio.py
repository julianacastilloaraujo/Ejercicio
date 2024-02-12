parcial1 = float(input("parcial 1 -> "))
parcial2 = float(input("parcial 2 -> "))
parcial3 = float(input("parcial 3 -> "))
parcial4 = float(input("parcial 4 -> "))
proyectofinal = float(input("proyecto final -> "))
finaldetrabajos = float(input("final de trabajos -> "))

promedio55 = (parcial1 + parcial2 + parcial3 + parcial4)/55
promedio30 = proyectofinal/30
promedio15 = finaldetrabajos/15


resultado = (promedio55 + promedio30 + promedio15/100)
print("El resultado es: ", resultado)