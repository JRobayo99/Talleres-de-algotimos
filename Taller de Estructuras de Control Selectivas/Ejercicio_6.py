cifras=input("Ingresar las variables A,B,C D: ").split()
a,b,c,d= cifras
a=int(a)
b=int(b)
c=int(c)
d=int(d)
m= a *1000
ce= b*100
de = c*10
un = d*1
tts= m+ce+de+un
n=round(tts,-2)
print("El número de rendondeado es: "+str(n))
