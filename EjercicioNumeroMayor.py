num1 = float(input("Digite su numero 1:"))
num2 = float(input("Digite su numero 2:"))
num3 = float(input("Digite su numero 3:"))
if num1 > num2 and num1 > num3:
    print(f"El numero mayor es {num1}")
elif num2 > num1 and num2 > num3:
    print(f"El numero mayor es {num2}")
else:
    print(f"El numero mayor es {num3}")
