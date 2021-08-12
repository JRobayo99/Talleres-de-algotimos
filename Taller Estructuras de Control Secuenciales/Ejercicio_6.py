nat= int(input("Ingrese el número de alumnos totales: "))
naf= int(input("Ingrese el número de mujeres: "))
nah= int (input("Ingrese el número de  hombres: "))
ph = (nah*100)/nat
pf = (naf*100)/nat
print("el porcentaje de mujeres en el grupó es de un: ""{:.0f}".format(pf),"%")
print("el porcentaje de hombres en el grupó es de un: ""{:.0f}".format(ph) ,"%")