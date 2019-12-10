#ejercicio 17
import os
#declaracion
nombre,edad="",0.0
nombre=os.sys.argv[1]
edad=float(os.sys.argv[2])
#pressecing
#si la edad es mayor o igual a 65 años
#mostrar apto para pension
if (edad>=65):
    print(nombre,"apto para pension")
else:
    print(nombre,"no apto para pension")
#fin_if
