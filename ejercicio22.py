#ejercicio 12

import os
#declaracion

alumno,curso_aprobado,curso_desaprobado,recuperacion="",0,0
alumno=os.sys.argv[1]
curso_aprobado=int(os.sys.argv[2])
curso_desaprobado=int(os.sys.argv[3])
recuperacion=int(os.sys.argv[4])
#pressecing
#si el curo tiene 13 de nota
#mostrar curso aprobado

if (curso_aprobado>=13):
    print(alumno,"aprobado")
else:
    print(alumno,"desaprobado")
#fin_if
if (recuperacion>=11):
    print(alumno,"recuperacion")

#OUTPUT
print("##############################")
print("#CURSOS#")
print("###############################")
print("#curso aprobado:",curso_aprobado)
print("#curso desaprobado:",curso_desaprobado)
print("#curso recupercion:",recuperacion)
