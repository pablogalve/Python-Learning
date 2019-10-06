num=int(input("Digues un numero per als elements de la llista"))
i=0
llista=[]
while i<num:
  element=input("Introdueix un element a la llista")
  llista.append(element)
  i=i+1
print (llista)

par1=input("Digues una paraula a substituir de la llista")
par2=input("Digues una paraula a afegir per substituir l'altra")

z=0
while z<num:
  if llista[z]==par1:
    llista.remove(par1)
    llista.insert(z, par2)
  z=z+1
print (llista)
