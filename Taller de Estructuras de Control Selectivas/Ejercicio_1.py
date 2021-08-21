Inve=int(input("Ingrese la cnatidad de dinero que desea invertir: "))
inrs= int(input("Ingrese el procentaje de intereses por mes: " ))
mpth = int (input("El núumero de meses que desea dejar sus intereses:  " ))
tintm = Inve*(inrs/100)
totri = tintm*mpth
ttll= totri+Inve
if (totri >= 100000):
    print("A supoerado los 100000 COP ¿Desea reinvetirlos?")
    print("Lleva hasta el momento un total de:" "{:.0f}".format(ttll)," COP")
elif(totri < 100000):
    print("La cantidad de dinero no es la sufieciente para reinvertirse: ")
    print("Lleva hasta el momento un total de:" "{:.0f}".format(ttll)," COP")
