Algoritmo Distancia_vehiculos_minutos
	Escribir "Escribir la velocidad del vehiculo que va adelante en Km/h " 
	Leer vh1
	Escribir "Escribir la velocidad del vehiculo que  por detras  en Km/h " 
	Leer vh2 
	Escribir "Distancia entre los vehiculos en Kilometros" 
	leer di
	vht<-(vh2-vh1)
	t<- di/vht
	tm <- t*60
	Escribir "El tiempo en minutos en que el segundo vehiculo alcanza al primero es: " tm " minutos"	
FinAlgoritmo
