cantidad_d=int(input("Ingrese la caantidad total de la compra de repuestos: "))
if(cantidad_d>=5000000):
    porcemp = cantidad_d*0.55
    porcbnc = cantidad_d*0.30
    porfab = cantidad_d*0.15
    intporcemp = porfab*0.20
    ttfab= intporcemp+porfab
    print("El porcentaje que invierte ls empresa en la compra es de: ""{:.0f}".format(porcemp))
    print("El porcentaje que invierte el banco por la compra es de: ""{:.0f}".format(porcbnc))
    print("El porcentaje que invierte el fabricante sumando los intereses al credito es de: ""{:.0f}".format(ttfab))
elif(cantidad_d<5000000):
    porcemp = cantidad_d*0.70
    porfab = cantidad_d*0.30
    intporcemp = porfab*0.20
    ttfab= intporcemp+porfab
    print("El porcentaje que invierte ls empresa en la compra es de: ""{:.0f}".format(porcemp))
    print("El porcentaje que invierte el fabricante sumando los intereses al credito es de: ""{:.0f}".format(ttfab))