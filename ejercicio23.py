#ejercicio 23

import os
#declaracion

cliente,total_compras="",0.0
cliente=os.sys.argv[1]
total_compras=float(os.sys.argv[2])
#pressecing
if (total_compras>70):
    print(cliente,"gano canasta")
else:
    print(cliente,"para la proxima oportunidad")
#fin_if
if (total_compras>60):
    print(cliente,"tien una segunda oportunidad")

#OUTPUT
print("##############################")
print("#compras#")
print("###############################")
print("#total de compras:",total_compras)

