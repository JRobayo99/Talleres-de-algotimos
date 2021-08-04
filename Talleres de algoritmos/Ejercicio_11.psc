Algoritmo Pormedio_Notas
	Escribir "Ingrese las notas de los parciales que equivalen al 55%."
	Leer notas51, notas52, notas53
	Escribir "Ingrese el promedio de notas que equivalente al 30%."
	Leer  notas30
	Escribir "Ingrese el promedio de notas que equivalente al 15%."
	Leer  notas15
	notasf<-(notas51+notas52+notas53)/3
	porcent1<-(notasf*0.55)
	porcent2<-(notas30*0.30)
	porcent3<-(notas15*0.15)
	caf<-porcent1+porcent2+porcent3
	Escribir "La calificación final de la materia es: " caf
	
FinAlgoritmo
