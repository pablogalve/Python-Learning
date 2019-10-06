num=int(input("Digues un numero per als elements de la llista"))
i=0
llista=[]
while i<num:
  element=input("Introdueix un element a la llista")
  llista.append(element)
  i=i+1
print (llista)
buscar=input("Introdueix l'element a buscar")
cont=llista.count(buscar)
if buscar in llista:
  print(buscar + " esta a la llista i surt " + str(cont) + " vegades")

else:
  print(buscar + " no esta a la llista")