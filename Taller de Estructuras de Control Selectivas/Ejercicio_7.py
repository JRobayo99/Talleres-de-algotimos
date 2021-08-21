distan_km=int(input("Digite la distancia recorrida en kilometros: "))
if(distan_km > 300 and distan_km <= 1000):
    cobro1= 70000
    cobrokm = (distan_km-300)*30000
    cott = cobro1+cobrokm
    print("El total a pagar por la distancia recorrida es: ""{:.0f}".format(cott))
elif (distan_km > 1000):
    cobro1= 150000
    cobrokm = (distan_km-1000)*9000
    cott = cobro1+cobrokm
    print("El total a pagar por la distancia recorrida es: ""{:.0f}".format(cott))
elif (distan_km<300):
    cobro1= 50000
    print("El total a pagar por la distancia recorrida es: ""{:.0f}".format(cobro1)) 