frutas = open('frutas.txt', 'r')
numeros= open('numeros.txt','r')
lista_frutas= [] #Llenar las lista con los datos del archivo frutas.txt
lista_numeros= []#Llenar las lista con los datos del archivo numeros.txt
for i in frutas:
 lista_frutas.append(i)

frutas.close()

for i in numeros:
  lista_numeros.append(i)

numeros.close()

#Realizar una funcion que elimine un caracter de todos los elementos de la lista





"""
Entradas:

lista->list->lista
elemento->str->elemento
Salidas:
lista->list->lista
"""
"""
def eliminar_un_caracter_de_toda_la_lista(lista:list,elemento:str)-> list:
  auxiliar=[]
  for i in lista:
    a=i.replace(elemento,"")
    auxiliar.append(a)
  return auxiliar

if __name__ == "__main__":
  #print(lista_frutas)
  lista_frutas_dos=eliminar_un_caracter_de_toda_la_lista(lista_frutas,"\n")
  lista_frutas_sin_m= eliminar_un_caracter_de_toda_la_lista(lista_frutas_dos,"m")
  print(lista_frutas_sin_m)
"""
#Realizar una funcion que retorne la copia de una funcion que pasa por parametro 

"""
Entradas:
lista->list->lista
Salidas:
lista->list->lista
"""
"""
def copia_lista(lista:list)-> list:
  return lista.copy()

if __name__ == "__main__":
  copia=copia_lista(lista_numeros)
  lista_nueva= eliminar_un_caracter_de_toda_la_lista(copia,"\n")
  print (copia_lista(lista_numeros))
"""
#numeros enteros
"""
Entradas:
lista->list->lista

Salidas:

lista->list->lista
"""
"""
def numeros_enteros(lista:list):
  auxiliar=[]
  auxiliar_dos=[]
  for i in lista:
    auxiliar.append(float(i))
  for i in auxiliar:
    auxiliar_dos.append(int(i))
  return auxiliar_dos
def copia_lista(lista:list)-> list:
   return lista.copy()
def eliminar_un_caracter_de_toda_la_lista(lista:list,elemento:str)-> list:
    auxiliar=[]
    for i in lista:
       a=i.replace(elemento,"")
       auxiliar.append(a)
    return auxiliar
if __name__=="__main__":
  copia=(copia_lista(lista_numeros))
  lista_nueva_2= eliminar_un_caracter_de_toda_la_lista(copia,"\n")
  print(numeros_enteros(lista_nueva_2))

"""
 
#Realizar una funcion que elimine un elemento de una lista

"""
Entradas:

lista.>list->lista
elemento->str->elemento

Salidas:

lista->list->lista
"""  
"""
def elimina_elemento_lista(lista:list,elemento:str)->list:
  auxiliar=[]
  for i in lista:
    a=i.replace(elemento,"")
    auxiliar.append(a)
  return auxiliar
if __name__ == "__main__":
  #print(lista_frutas)
  lista_frutas_dos=elimina_elemento_lista(lista_frutas,"\n")
  lista_frutas_sin_fresa=elimina_elemento_lista(lista_frutas_dos,"Fresa")
  print(lista_frutas_sin_fresa)
"""

#Retorna una lista con las palabras iniciales con la letra que pasa por parametro  
"""
Entradas:
letra->str->letra
lista->list->lista
Salidas:
lista->list->lista
"""
"""
def letra(letra:str,lista:list)->list:
  auxiliar=[]
  for i in lista:
     if i [0]== letra:
       auxiliar.append(i)
  return(auxiliar)
if __name__ == "__main__":
  lista_inicial=letra("M",lista_frutas)
  print(lista_inicial)
"""
#Realizar una funcion que retorne el tamaño de una lista   
"""
Entradas:
lista->list->lista
Salidas
lista->list->lista
"""
""" 
def tamano_lista(lista:list):
  auxiliar=[]
  tamano= len(lista)
  for i in lista:
   auxiliar.count(i==0)
  return tamano
if __name__=="__main__":
  print(tamano_lista(lista_numeros))
"""
   #RetornaUnEntero
#Retorna el tamaño de la lista y que tipo de datos estan dentro de la lista
"""
Entradas:
lista->list->lista
Salidas:
lista->list->lista
"""  
"""
def informacion_lista(lista:list):
  tamaño=len(lista)
  auxiliar=[]
  for i in lista:
    if (auxiliar.count(i)==0):
      auxiliar.append(type(i))
  return tamaño,auxiliar

print(informacion_lista(lista_frutas))
""" 
#Retornar una lista con los numero negativos  
"""
Entradas:
lista->list->lista
elemento->str-elemento
Salidas:
lista->list->lista
""" 
"""
def numeros_negativos(lista:list):
  auxiliar=[]
  auxiliar_dos=[]
  for i in lista:
    auxiliar.append(float(i))
  for i in auxiliar:
    if(i<0):
     auxiliar_dos.append(int(i))
  return auxiliar_dos
def copia_lista(lista:list)-> list:
   return lista.copy()
def eliminar_un_caracter_de_toda_la_lista(lista:list,elemento:str)-> list:
    auxiliar=[]
    for i in lista:
       a=i.replace(elemento,"")
       auxiliar.append(a)
    return auxiliar
if __name__=="__main__":
  copia=(copia_lista(lista_numeros))
  lista_nueva_2= eliminar_un_caracter_de_toda_la_lista(copia,"\n")
  print(numeros_negativos(lista_nueva_2))
"""

#realizar una funcion que retorne la posicion de un elemento que pasa por parametro

"""
def posicion_elemento(lista:list,elemento:str):
  auxiliar=[]
  for i in lista:
    if (str(i) == str(elemento)+"\n"):
      auxiliar.append(lista.index(i))
  return auxiliar

if __name__=="__main__":
  print(posicion_elemento(lista_frutas,"Fresa"))
"""
#realizar una funcion que agregue al final de archivo frutas una fruta
"""
def frutas_nuevo(elemento):

  frutas = open('frutas.txt', 'r')
  for i in frutas:
    lista_frutas.append(i)
  frutas.close()

  frutas = open('frutas.txt', 'w')

  for i in lista_frutas:
    frutas.write(i)

  frutas.write("\n"+str(elemento))
  frutas.close()  
"""  
#Realizar una funcion que cuente el numero de veces que se repite un elemento
"""  
def repetir(elemento):
  auxiliar=[]
  for i in elemento:

    for ii in auxiliar:
      if i == ii:
        c = 0
        auxiliar.append(c)
        c = "c" + i
    return c
"""
"""
if __name__ == "__main__":
  lista=[1,2,3,4,4]
  copy=copia_lista(lista)
  print(copy)
""" 