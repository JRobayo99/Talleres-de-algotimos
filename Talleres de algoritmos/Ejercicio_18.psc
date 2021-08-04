Algoritmo pedir_nombre
	Escribir "Ingresa el primer nombre"
	Leer name_1
	Escribir "Ingresa el segundo nombre"
	Leer name_2
	Escribir "Ingresa el primer apellido"
	Leer ltname_1
	Escribir "Ingresa el segundo apellido"
	Leer ltname_2
    N1<-SubCadena(name_1,1,1)
	N2<-SubCadena(name_2,1,1)
	NT1<-SubCadena(ltname_1,1,1)
	NT2<-SubCadena(ltname_2,1,1)
	Escribir "Tus iniciales son: " N1 N2 NT1 NT2 
FinAlgoritmo
