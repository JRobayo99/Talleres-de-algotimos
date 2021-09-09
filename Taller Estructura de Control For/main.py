archivo = open('pasises.txt', 'r')
#imprima la posicion de colombia
""""
lista=[]
for i in archivo:
  lista.append(i)
  a="".join(lista)
  print(a.strip())
  lista=[] 
"""
"""
lista=[]
for i in archivo:
  a=i.index(":")
  for r in range(a+2,len(i)):
    lista.append(i[r])
  a="".join(lista)
  print(a.strip())
  lista=[] 
"""
"""

lista=[]
ciudad=[]
paises=[]
for i in archivo:
  a=i.index(":")
  for r in range(0,a):
    lista.append(i[r])
  a="".join(lista)
  paises.append(a)
  lista=[]
  b=i.index(":")
  for t in range(b+2,len(i)):
    lista.append(i[t])
  b="".join(lista)
  ciudad.append(b)
  lista=[]
print(i,t)
"""


#Imprima todos los paises
"""
lista=[]
for i in archivo:
  a=i.index(":")
  for r in range(0,a):
    lista.append(i[r])
  a="".join(lista)
  print(a)
  lista=[]
"""
#Imprima todas las Capitales
"""
lista=[]
for i in archivo:
  a=i.index(":")
  for r in range(a+2,len(i)):
    lista.append(i[r])
  a="".join(lista)
  print(a.strip())
  lista=[]
"""
#Imprimir todos los paises que inicien con la letra C
""""
lista=[]
paises=[]
for i in archivo:
  a=i.index(":")
  for r in range(0,a):
    lista.append(i[r])
  a="".join(lista)
  paises.append(a)
  lista=[]
for i in paises:
  if(i[0]=="C"):
    print(i)
"""
#imprima todas las capitales que inicien con la leta B
"""
lista=[]
ciudad=[]
for i in archivo:
  a=i.index(":")
  for r in range(a+2,len(i)):
    lista.append(i[r])
  a="".join(lista)
  ciudad.append(a)
  lista=[]
for i in ciudad:
  if(i[0]=="B"):
    print(i.strip())  
"""

#imprima la posicion del pais de Mexico
"""
c=0
lista=[]
for i in archivo:
  lista.append(i)
  a=" ".join(lista)
  c=c+1 
  if(a=="México: Cuidad de México\n"):
    break
  lista=[]   
print(("La posición de Mexico es la"),c)
"""

#imprima la posicion del pais de Uganda
"""
c=0
lista=[]
for i in archivo:
  lista.append(i)
  a=" ".join(lista)
  c=c+1 
  if(a=="Uganda: Kampala\n"):
    break
  lista=[]   
print(("La posición de Uganda es la"),c)
"""




#Cuente e imprima cuantas ciudades inician con la letra M 
""""
lista=[]
num=0
ciudad=[]
for i in archivo:
  a=i.index(":")
  for r in range(a+2,len(i)):
    lista.append(i[r])
  a="".join(lista)
  ciudad.append(a)
  lista=[]
for ciu in ciudad:
  if(ciu[0]=="M"):
   num=num+1
for i in ciudad:
  if(i[0]=="M"):
    print(i.strip())

print("De todas la cuidades capitales en el mundo las que empienzan por la letra M son: "+str(num))
"""
#Cuente e imprima los paises en la lista
"""
pais=[]
lista=[]
num=0

for i in archivo:
  a=i.index(":")
  for r in range(0+a):
    lista.append(i[r])
  a="".join(lista)
  pais.append(a)
  lista=[]

  num=num+1


print("El número total de paises en el plaenta tierra es de: ",(num), " paises")
"""  
#Imprima todos los paises y capitales, cuyo inicio sea con la letra U
"""
paises=[]
listad2=[]
capitales=[]
lista=[]
for i in archivo:
  a=i.index(":")
  for r in range(0,a):
    lista.append(i[r])
  a="".join(lista)
  paises.append(a)
  lista=[]
  a=i.index(":")
  for r in range(a+2,len(i)):
    lista.append(i[r])
  a="".join(listad2)
  capitales.append(a)
  listad2=[]
for i in paises:
  if(i[0]=="U"):
    print(i)
for i in capitales:
  if(i[0]=="U"):
    
 
    print(i)
"""
#Busque e imprima el pais de Venezuela y su capital
"""
lista=[]
for i in archivo:
  lista.append(i)
  a=" ".join(lista)
  if(a=="Venezuela: Caracas\n"):
    break
  lista=[]   
print(a)
"""
#Buesque e imprima la Capiltal de Colombia
"""
lista=[]
for i in archivo:
  a=i.index(":")
  for r in range(a+2,len(i)):
    lista.append(i[r])
  a="".join(lista)
  if(a=="Bogotá\n"):
    break
  lista=[]
print(a.strip())
"""
#Busque e imprima la Cuidad de Singapur
"""
lista=[]
for i in archivo:
  a=i.index(":")
  for r in range(a+2,len(i)):
    lista.append(i[r])
  a="".join(lista)
  if(a=="Singapur\n"):
    break
  lista=[]
print(a.strip())
"""
#Agregue un país que no esté en la lista 
"""
lista=[]
lista.append("Yugoslavia\n")
for i in archivo:
  a=i.index(":")
  for r in range(0,a):
    lista.append(i[r])
  a="".join(lista)
  print(a)
  lista=[]
"""
#El alcalde de Antananarivo contrato a algunos alumnos de la Universidad Ean para corregir el archivo de países.txt, ya que la capital de Madagascar NO es rey julien es Antananarivo, espero que el alcalde se vaya contento por su trabajo. Utilice un For para cambiar ese Dato
"""
lista=[]
lista1=[archivo]
for i in archivo:
  for r in range(lista1):
  
   if lista1[i]== "Madagascar: rey julien\n":
    lista1[i]= "Madagascar: Antananarivo\n"
  print(lista1)
    
  lista.append(i)
  a="".join(lista)
  lista=[] 
"""  
#Cuente e imprima las ciudades que su pais inicie con la letra E
"""
lista=[]
paises=[] 
num=0
lista2=[]
ciudades=[] 
for i in archivo:
  if(i[0]=="E"):
    a=i.index(":")
    for r in range(a+2,len(i)):
      lista.append(i[r])
    a="".join(lista)
    ciudades.append(a)
    lista=[]
for i in ciudades:
    for i in archivo:
      a=i.index(":")
      for r in range(a+2,len(i)):
        lista2.append(i[r])
      a="".join(lista2)
      ciudades.append(a)
      lista2=[]
    if(num==11):
      break
    num=num+1
    print(num, i.strip())
"""    
archivo.close()
