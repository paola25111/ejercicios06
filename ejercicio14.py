#ejercicio 14

import os
#declaracion
cliente,numero_tickes="",0
cliente=os.sys.argv[1]
numero_ticke=int(os.sys.argv[2])
#pressecing
#si el cliente tiene mas de 14  tickes
#mostrar entra al sorteo de caso contario mostrar no entra al sorteo
if (numero_tickes>25):
    print(cliente,"entra al sorteo")
else:
    print(cliente,"no entra al sorteo")

#fin_if
