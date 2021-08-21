montc=int(input("Ingrese el monto de la compra: "))
name = str(input("Ingrese el nombre del cliente: "))
if(montc < 50000):
    print("Nombre del cliente: "+str(name))
    print("No hay descuento")
    print("Monto a pagar: " +str(montc)," COP")
elif (montc >=50000 and montc< 100000):
    montt= montc*0.05
    montta= montc-montt
    print ("Nombre del cliente: "+str(name))
    print("Su momto de compra es: " +str(montc))
    print ("Su descuento por la compra es de: " "{:.0f}".format(montt), " COP")
    print ("Su valor a pagar es de: ""{:.0f}".format(montta)," COP")
elif (montc >=100000 and montc< 700000):
    montt= montc*0.11
    montta= montc-montt
    print ("Nombre del cliente: "+str(name))
    print("Su momto de compra es: " +str(montc))
    print ("Su descuento por la compra es de: " "{:.0f}".format(montt), " COP")
    print ("Su valor a pagar es de: ""{:.0f}".format(montta)," COP")
elif (montc >=700000 and montc< 1500000):
    montt= montc*0.18
    montta= montc-montt
    print ("Nombre del cliente: "+str(name))
    print("Su momto de compra es: " +str(montc))
    print ("Su descuento por la compra es de: " "{:.0f}".format(montt), " COP")
    print ("Su valor a pagar es de: ""{:.0f}".format(montta), " COP")
elif (montc >=1500000 ):
    montt= montc*0.25
    montta= montc-montt
    print ("Nombre del cliente: "+str(name))
    print("Su momto de compra es: " +str(montc))
    print ("Su descuento por la compra es de: " "{:.0f}".format(montt), " COP")
    print ("Su valor a pagar es de: ""{:.0f}".format(montta), " COP")