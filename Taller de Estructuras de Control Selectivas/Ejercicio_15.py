ed=float(input("Por favor indiquenos la edad de la personaen años: "))
apl=float(input("Ingrese el numero 1 si es hombre mayor de 15 años o más, 2 si es mujer de 15 años o más, 3 si no aplica el rango: "))
por=float(input("Ingrese el porcentaje de hemoglobina en sus examenes: "))
if(apl==3 and ed<=0.1):
    if(por>=13 and por <=26):
     print("No tiene anemia")
    else:
       print("Tiene anemia")
if(apl==3) and (ed>0.1 or ed<=0.6):
    if(por>=10 and por <=18 ):
     print("No tiene anemia")
    else:
       print("Tiene anemia")
if(apl==3) and (ed>0.6 or ed<=0.12):
    if(por>=11 and por <=15 ):
     print("No tiene anemia")
    else:
       print("Tiene anemia")
if(apl==3) and (ed>1 or ed<=5):
    if(por>=11.5 and por <=15 ):
     print("No tiene anemia")
    else:
       print("Tiene anemia")
if(apl==3) and (ed>5 or ed<=10):
    if(por>=12.6 and por <=15.5 ):
     print("No tiene anemia")
    else:
       print("Tiene anemia")
if(apl==3) and (ed>10 or ed<=15):
    if(por>=13 and por <=15.5 ):
     print("No tiene anemia")
    else:
       print("Tiene anemia")
if(apl==1) and (ed>=15):
    if(por>=14 and por <=18 ):
     print("No tiene anemia")
    else:
       print("Tiene anemia")
if(apl==2) and (ed>=15):
    if(por>=12 and por <=16 ):
     print("No tiene anemia")
    else:
       print("Tiene anemia")


