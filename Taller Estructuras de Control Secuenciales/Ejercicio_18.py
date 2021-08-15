pb = int (input("Ingresem la suma de pretsamo en bolivares: "))
ad = int (input("Ingrese el tiempo de pago de la deuda: "))
pbtu = pb/ad
adt = ad-1
pnt2 = (pb-(pbtu*adt))
ptb = (pnt2/pb)*100
irs = (pb*ad*4)/100
print("El porncetaje de pagos anules es igaules a: ""{:.0F}".format(ptb),("%"))
print("El monto de intereses pagados anualmente es de: ""{:.0F}".format(irs),("BS"))