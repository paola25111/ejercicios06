#ejercicio 21
#declarar
producto,cant,precio="",0,0.0
monto_bruto,monto_total=0.0,0.0
dscto=0.0
producto=input("Ingrese el producto")
cant=int(input("Ingrese cantidad:"))
precio=float(input("Ingrese preco:"))
dscto=0.0

#prossecing
monto_bruto=cant*precio
#calcular el decuento
#identificar el producto
if (producto=="papa"):
    producto="papa"
if (producto=="sal"):
    producto="papa"
if (producto=="carne"):
    producto="carne"

#efectuar decuento
if (producto=="papa"):
    #si se compro mas de 15 productos , aplicar el 20%
    if (cant>15):
        dscto=monto_bruto*0.2
    else:
        dscto=monto_bruto*0.1
if (producto=="sal"):
    dscto=monto_bruto*0.05
if (producto=="carne"):
    dscto=monto_bruto*0.07
monto_total=monto_bruto-dscto

#OUTPUT
print("##############################")
print("#BOLETADE VENTA#")
print("###############################")
print("#Monto Bruto:",monto_bruto)
print("#Monto Total:",monto_total)
