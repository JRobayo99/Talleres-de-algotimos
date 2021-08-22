dian=int(input("Ingresa tu dia de nacimiento: "))
mesn= int(input("Ingrese tu mes de nacimiento: "))
añon= int(input("Ingrese el año de nacimietno: "))
añoac = int(input("Ingrese el año actual: "))
if((mesn==11 and dian>=22)or(mesn==12 and dian<=21)):
    print ("Signo Zodiacal: Sagitario")
if((mesn==12 and dian>=22)or(mesn==1 and dian<=20)):
    print ("Signo Zodiacal: Capricornio")
if((mesn==1 and dian>=21)or(mesn==2 and dian<=19)):
    print ("Signo Zodiacal: Aucario")
if((mesn==2 and dian>=20)or(mesn==3 and dian<=19)):
    print ("Signo Zodiacal: Picis")
if((mesn==3 and dian>=21)or(mesn==4 and dian<=20)):
    print ("Signo Zodiacal: Aires")
if((mesn==4 and dian>=21)or(mesn==5 and dian<=21)):
    print ("Signo Zodiacal: Tauro")
if((mesn==5 and dian>=21)or(mesn==6 and dian<=21)):
    print ("Signo Zodiacal: Géminis")
if((mesn==6 and dian>=22)or(mesn==7 and dian<=22)):
    print ("Signo Zodiacal: Cáncer")
if((mesn==7 and dian>=23)or(mesn==8 and dian<=23)):
    print ("Signo Zodiacal: Leo")
if((mesn==8 and dian>=24)or(mesn==9 and dian<=22)):
    print ("Signo Zodiacal: Virgo")
if((mesn==9 and dian>=23)or(mesn==10 and dian<=22)):
    print ("Signo Zodiacal: Libro")
if((mesn==10 and dian>=23)or(mesn==11 and dian<=21)):
    print ("Signo Zodiacal: Escorpión")
edadact= añoac-añon
print("Su edad actual es de: ""{:.0f}".format(edadact))