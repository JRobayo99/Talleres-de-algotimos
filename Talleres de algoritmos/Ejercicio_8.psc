Algoritmo Cantidad_minutos
	Definir m Como Real
	Escribir "Ingrese el valor en minutos"
	leer m
	Hora1<- m/60
	Hora2<-trunc(Hora1)
	Hora3<- Hora1-Hora2
	Minutos1<-Hora3*60
	Minutos<-trunc(Minutos1)
	Escribir Hora2, " Horas"
	Escribir Minutos, "  Minutos"
	
FinAlgoritmo
