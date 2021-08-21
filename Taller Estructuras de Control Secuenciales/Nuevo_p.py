print("--Dia reservación--")
print ("1)lunes")
print ("2) martes")
print ("3) miercoles")
print ("4)jueves")
print ("5) viernes")
print ("6) Sabado")
print ("7) Domingo")
dia_dr= int(input("Selelcciona el dia para tu reservacion: ")) 
if dia_dr==1 or dia_dr==3 or dia_dr==5:
  print ("Este dia solo tenemos caopcidad para 80 personas")
  print ("Desea reservar este dia: ")
  print ("1) Si")
  print ("2) No")
  esd_1= int(input("Selecciona 1 para reservar ese dia y 2 para no: "))
  if (esd_1==1):
      print("Reservación hecha")
  elif (esd_1==2):
      print("Vuelve a seleccionar el dia para tu reservación")
elif dia_dr==2 or dia_dr==4 or dia_dr==6 or dia_dr==7:
    print ("Este dia tenemos cacidad para 100 personas")
    print ("Desea reservar este dia: ")
    print ("1) Si")
    print ("2) No")
    esd_1= int(input("Selecciona 1 para reservar ese dia y 2 para no: "))
    if (esd_1==1):
         print("Reservación hecha")
    elif (esd_1==2):
         print("Vuelve a seleccionar el dia para tú reservación4")