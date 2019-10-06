num=int(input("Digues un num per la llargaria de la llista"))
i=0
llista=[]
while (i<num):
  paraula=input("Introdueix una paraula per la llista")
  llista.append(paraula) 
  i=i+1
  
print (llista)
buscar=input("introduce un nombre de la lista para buscarlo")
llista.index(buscar)
print(buscar)