h1=int(input("Ingrese el nuemro horas trbajadas en el mes: "))
s1=int(input("Ingrese el monto minimo por hora de acuerdo al salrio minimo legal vigente: "))
sp = h1*s1
desc= sp*0.2
snt= sp-desc
print("El el salario sin descuento del 20%: "+str(sp))
print("El salario neto es de: ""{:.0f}".format(snt))