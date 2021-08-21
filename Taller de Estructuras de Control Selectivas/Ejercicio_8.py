P=int(input("Ingresa la varibale P: "))
Q= int(input("Ingrese la varianle Q: "))
tt= (P**3)+(Q**4)-(2*P**2)
if(tt<680):
    print (str(P) ,"y  " +str(Q)," no satisfacen la expresión")
elif(tt>680): 
    print (str(P) ,"y  " +str(Q)," satisfacen la expresión")