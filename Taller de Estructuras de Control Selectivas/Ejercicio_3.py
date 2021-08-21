dtos3= input().split()
a,b,c,d = dtos3
a= int(a)
b= int(b)
c= int(c)
d= int(d)
if (d==0):
    resul= (a-c)**2
    print("El resultado es de: "+str(resul))
elif (d>0):
    resul = ((a-b)**3)/d
    print("El resultado es de: "+str(resul))