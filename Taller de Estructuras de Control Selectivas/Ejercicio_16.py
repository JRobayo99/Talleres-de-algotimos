import math
a=float(input("Ingrese la variable A: "))
b=float(input("Ingrese la variable B: "))
c=float(input("Ingrese la variable C: "))
d= (b**2)-(4*a*c)
if(d==0):
    X1= -b/(2*a)
    X2= -b/(2*a)
    tt=a*X1**2+b*X2+c
    print("El valor es de a*x**2+b*x+c: ""{:0}".format(tt))
if(d>0):
    X1=(-b+ math.sqrt(b**2-4*a*c)/(2*a))
    X2= (-b - math.sqrt(b**2-4)/(2*a))
    tt=a*X1**2+b*X2+c
    print("El valor es de a*x**2+b*x+c: ""{:0}".format(tt))
if(d<0):
    print("no tiene solución")