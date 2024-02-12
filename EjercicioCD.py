import math

capacidad_disco_gb = int(input("Ingrese la capacidad del disco duro en GB: "))
capacidad_disco_mb = capacidad_disco_gb * 1024
capacidad_cd_mb = 700
cds_necesarios = math.ceil(capacidad_disco_mb / capacidad_cd_mb)

print(f"Numero de Cds necesarios:, {cds_necesarios}")



