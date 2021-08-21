cat=int(input("Ingrese la categoria del trbajdor: "))
suel=int(input("Ingrese el sueldo bruto del trabajador: "))
if(cat==1):
    suelt1=suel* 0.10
    suelt= suelt1+suel
    print("Categoria: " +str(cat))
    print("Susueldo bruto con aumento es de: ""{:.0f}".format(suelt)," COP")
elif(cat==2):
    suelt1=suel* 0.15
    suelt= suelt1+suel
    print("Categoria: " +str(cat))
    print("Susueldo bruto con aumento es de: ""{:.0f}".format(suelt)," COP")
elif(cat==3):
    suelt1=suel* 0.20
    suelt= suelt1+suel
    print("Categoria: " +str(cat))
    print("Susueldo bruto con aumento es de: ""{:.0f}".format(suelt)," COP")
elif(cat==4):
    suelt1=suel* 0.40
    suelt= suelt1+suel
    print("Categoria: " +str(cat))
    print("Susueldo bruto con aumento es de: ""{:.0f}".format(suelt)," COP")
elif(cat==5):
    suelt1=suel* 0.60
    suelt= suelt1+suel
    print("Categoria: " +str(cat))
    print("Susueldo bruto con aumento es de: ""{:.0f}".format(suelt)," COP")
    