tf=int(input("Ingrese la tempratura en grados Fahrenheit: "))
if(tf > 85):
    print("Natación")
elif(70 < tf and tf<=85):
    print("Tenis")
elif(31 < tf and tf<=70):
    print("Golf")
elif(9<tf and tf<=32):
    print("Esquí")
elif(tf<=10):
    print("Marcha")   