L1= int(input("Ingresa el numero de la lectura actual de consumo de energía: "))
L2 = int (input("Ingrese el numero de la lectura pasada de consumo energía: "))
Kwh = float (input("Cosoto de kilovatio por hora: "))
Tl = L1-L2
Tp = Tl*Kwh
print("El total apagar este mes de lectricidad es de: ""{:.0F}".format(Tp))