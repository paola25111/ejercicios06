#ejercicio 15

import os
#declaracion

alumno,total_de_creditos="",0
alumno=os.sys.argv[1]
total_de_creditos=int(os.sys.argv[2])
#pressecing
if (total_de_creditos>24):
    print(alumno,"puede matricularse")
else:
    print(alumno,"no cuenta con los suficientess creditos")
#fin_if
