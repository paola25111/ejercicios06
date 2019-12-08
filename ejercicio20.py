#ejercicio 20
import os
#declaracion

cliente,costo_entreda="",0.0,
cliente=os.sys.argv[1]
costo_entreda=float(os.sys.argv[2])
#pressecing
#si el costo es mayor a 40
#mostrar zona vip
#en caso contrario zona corriente
if (costo_entreda>40):
    print(cliente,"zona vip")
else:
    print(cliente,"zona corriente")
#fin_if
