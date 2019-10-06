num=int(input("Digues quants elements vols a la llista:"))
i=0
llista=[]
while (i<num):
  element=input("Digues un numero que vols afegir a la llista")
  llista.append(element)
  i=i+1

print("La teva llista de numeros es " + str(llista))

num2=int(input("Digues un numero per a sumar als de la llista"))
longi=len(llista)
j=0
llista2=[]
while (j<=