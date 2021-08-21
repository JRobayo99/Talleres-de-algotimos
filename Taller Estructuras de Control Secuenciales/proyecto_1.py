class Menu(): #Clsse Menu
    cant=0
    total=0
    def Desayuno(self):#Metodo Desayuno
        cant=input("Ingrese el némero de persona: ")
        total = cant*35
        print("El toal al pagar es: %s" % total)
    def Comida(self):#Metodo Comida
        cant=input("Ingrese el némero de persona: ")
        total = cant*50
        print("El toal al pagar es: %s" % total)
    def Cena(self):#Metodo Cena
        cant=input("Ingrese el némero de persona: ")
        total = cant*40
        print("El toal al pagar es: %s" % total)
m = Menu()
print("Menu")
print ("1) Desayuno")
print ("2) Comida")
print ("3) Cena")
opc=input("Selecciona: ")
if opc == 1:
    m.Desayuno()
elif opc==2:
    m.Comida()
elif opc == 3:
    m.Cena("raspao")

