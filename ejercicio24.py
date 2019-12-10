#ejercicio 24

import os
#declaracion
cliente,numero_tickes="",0
cliente=os.sys.argv[1]
numero_tickes=int(os.sys.argv[2])
#pressecing
#si el cliente tiene mas de 14  tickes
#mostrar entra al sorteo de caso contario mostrar no entra al sorteo
if (numero_tickes>14):
    print(cliente,"entra al sorteo")
else:
    print(cliente,"no entra al sorteo")
    #fin_if
if(numero_tickes>12):
    print(cliente,"tiene una segunda oportunidad")
#OUTPUT
print("##############################")
print("#sorteo de tickets#")
print("###############################")
print("#entra al sorteo:",numero_tickes)
print("#no entra al sorteo:",numero_tickes)
print("#tiene una segunda oportunidad:",numero_tickes)
