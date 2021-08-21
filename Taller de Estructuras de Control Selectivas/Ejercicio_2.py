salrim=int(input("Ingrese el monto del salario mesual:"))
if (salrim<=900000):
    satlr = salrim*0.15
    ttst = satlr+salrim
    print("El salario neto es de : " "{:.0f}".format(ttst))
elif(salrim> 900000):
    satlr = salrim*0.12
    ttst = salrim+satlr
    print("El salario neto es de : " "{:.0f}".format(ttst))