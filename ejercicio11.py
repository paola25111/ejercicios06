#ejercicio 11

import os
#declaracion

nombre,puntaje_de_ingreso="",0
nombre=os.sys.argv[1]
puntaje_de_ingreso=int(os.sys.argv[2])
#pressecing
if (puntaje_de_ingreso>100):
    print(nombre,"ingreso")
else:
    print(nombre,"no ingreso")

#fin_if
