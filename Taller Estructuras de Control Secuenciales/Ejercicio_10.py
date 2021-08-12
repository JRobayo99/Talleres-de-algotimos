chel= float(input("La catidad de chelines para saber su precio en pesetas: "))
dracg= float(input("La cantida de dragmas griegos para saber su precion en francos: "))
psets= float (input("la cantidad de pesetas para su tasas de cambio en dolares y liras italianas es: ")) 
pst= chel*956.871
fr = (dracg*88.507)/(100*20.110)
lrt=(psets*100)/9.289
USD = psets/122.499
print("De chelines a pesetas son: "+str(pst), " Pesetas")
print ("De dragmas a francos so: " "{:.3F}".format(fr), " Francos FRA")
print ("De pesetas a liras italianas es: ""{:.3F}".format(lrt), " Liras ITA")
print ("Pesetas a dolores es: ""{:.3F}".format(USD), " USD")