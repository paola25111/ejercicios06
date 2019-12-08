#ejercicio 08

import os
#declaracion

nombre,nro_tickets="",0
#inputvia os
nombre=os.sys.argv[1]
nro_tickets=int(os.sys.argv[2])
#pressecing
#si el nro de tickets supera los 50
#mostrar "ganaste un paneton
if (nro_tickets>50):
    print(nombre,"ganaste un paneton")
#fin_if
