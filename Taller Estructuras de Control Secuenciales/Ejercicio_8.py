la= int (input("Ingrese la longuitud del lado a: "))
lb= int (input("Ingrese la longuitud del lado b: "))
lc= int (input("Ingrese la longuitud del lado c: "))
sm= (la+lb+lc)/2
l1=sm-la
l2=sm-lb
l3=sm-lc
area= (sm*l1*l2*l3)**(1/2)
print ("El área del tringulo de acuerdo a sus longuitudes es: " "{:.4f}".format(area))