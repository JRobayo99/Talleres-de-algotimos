lnt= int(input("El precio del lo de naranjas: "))
dona=int(input("La canitidad de docenas de naranjas: "))
vd= int(input("Ventas a detallistas: "))
dcp1= lnt/dona
dcp = dcp1+lnt
gp= (vd/dcp)*100
print("El porcentaje de ganacia es igual a: ""{:.0F}".format(gp),("%"))