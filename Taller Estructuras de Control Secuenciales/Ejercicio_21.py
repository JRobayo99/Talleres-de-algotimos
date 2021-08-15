pc=int(input("Precio de la compuatdora: "))
cc= int(input("Costo de las cuotas de la computadora: "))
pvu= pc*0.01
tp= cc+pvu
tt=(tp/pc)*100
print("El total de procentaje cobrado por cada cuota es de: ""{:.0F}".format(tt),("%"))
