Num1=int(input("Ingrese el total de vetas del departamento 1 : "))
Num2=int(input("Ingrese el total de vetas del departamento 2 : "))
Num3=int(input("Ingrese el total de vetas del departamento 3 : "))
numt= Num1+Num2+Num3
numpv= (Num1/numt)*100
numpv2= (Num2/numt)*100
numpv3= (Num3/numt)*100
if(numpv>=33):
    salario= 908000
    spsm = salario*0.20
    tts = spsm+salario
    print("El departamento 1 es quien gana el bono a asu salario y su sueldo neto es de: ""{:.0f}".format(tts))
elif(numpv< 33):
    salario= 908000
    print("Los trbajadores no alcanzaron la bonificación deseada su salario neto es de: "+str(salario))
if (numpv2>=33):
    salario= 908000
    spsm = salario*0.20
    tts = spsm+salario
    print("El departamento 2 es quien gana el bono a asu salario y su sueldo neto es de: " "{:.0f}".format(tts))
elif(numpv2< 33):
    salario= 908000
    print("Los trabajadores no alcanzaron la bonificación deseada su salario neto es de: "+str(salario))
if (numpv3>=33):
    salario= 908000
    spsm = salario*0.20
    tts = spsm+salario
    print("El departamento 3 es quien gana el bono a asu salario y su sueldo neto es de: ""{:.0f}".format(tts))
elif(numpv3< 33):
    salario= 908000
    print("Los trbajadores no alcanzaron la bonificación deseada su salario neto es de: "+str(salario))