gal=int(input("Galones a depositar de gasolina: "))
lts = gal*3.785
tp = lts*50000
print("De Galones a litros son: ""{:.2F}".format(lts), ("lt"))
print("El precio a pagar por los galones depositados es de: ""{:.0F}".format(tp), ("COP"))