Lect=int(input("Lectura acutual del medidor: "))
lecta= int(input("Lectura pasda  del medidor: "))
lectt= Lect-lecta
if (lectt>=0 and lectt<=100):
    ttl=4600*lectt
    print("El cosnto que debe pagar por el recibo de energia electrica y el servicio de aseo es de: ""{:.0f}".format(ttl))
if (lectt>=101 and lectt<=300):
    ttl=80000*lectt
    print("El cosnto que debe pagar por el recibo de energia electrica y el servicio de aseo es de: ""{:.0f}".format(ttl))
if (lectt>=301 and lectt<=500):
    ttl=10000*lectt
    print("El cosnto que debe pagar por el recibo de energia electrica y el servicio de aseo es de: ""{:.0f}".format(ttl))
if (lectt>=501):
    ttl=120000*lectt
    print("El cosnto que debe pagar por el recibo de energia electrica y el servicio de aseo es de: ""{:.0f}".format(ttl))
