horasal=input().split()
a1,a2,a3= horasal
a1= int(a1)
a2=int(a2)
a3=int(a3)
ht= a1+a2+a3
htv = (a1+a2+a3)-24
if(ht>23):
    ht = htv
print(""+str (ht))
