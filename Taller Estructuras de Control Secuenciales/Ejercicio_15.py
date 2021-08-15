pf=int(input("Ingrese el valor del precio final: "))
pvp=int(input("Ingrese el valor del producto para PVP: "))
vf=(pf-pvp)/pf
vft = vf*100
print("El porcentaje del precio PVP es de: ""{:.2F}".format(vft),("%"))