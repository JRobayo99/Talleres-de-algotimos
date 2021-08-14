line = input().split(" ") 
a,b,c= line
a=int(a)
b=int(b)
c=int(c)
af=int(input("Nota del examnen final de matemáticas: "))
line2 = input().split(" ") 
a2,b2= line2
a2=int(a2)
b2=int(b2)
bf=int(input("Nota del examnen final fisica: "))
line3 = input().split(" ") 
a3,b3,c3= line3
a3=int(a3)
b3=int(b3)
c3=int(c3)
cf=int(input("Nota del examnen final quimica: "))
dp = ((a+b+c)/3)*0.10
dcp= ((a2+b2)/2)*0.20
qc = ((a3+b3+c3)/3)*0.15
pm = af*0.90
pf = bf*0.80
pq = cf*0.85
fm = dp+pm
ff = dcp+pf 
fq = qc+pq
print ("El promedio me matemáticas es de: ""{:.2F}".format(fm))
print("El promedio de fisica es de: ""{:.2F}".format(ff))
print("El promdedio de química esde : ""{:.2F}".format(fq))