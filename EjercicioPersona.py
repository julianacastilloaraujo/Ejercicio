altura = float(input("Digite su altura:"))
if altura <= 1.50:
    print("Persona de Altura baja")
elif altura > 1.51 and altura <= 1.70:
    print("Persona de Altura media")
elif altura > 1.71 and altura <= 1.90:
    print("Persona Alta")
elif altura > 1.91 and altura <= 2.30:
    print("Persona Muy Alta")
else:
    print("Persona Demasiado Alta")
