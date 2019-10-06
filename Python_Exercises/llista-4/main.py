num=int(input("Digues un numero per als elements de la llista"))
i=0
llista=[]
while i<num:
  element=input("Introdueix un element a la llista")
  llista.append(element)
  i=i+1
print (llista)

par1=input("Digues una paraula a eliminar de la llista")

i=0
while (i<num):
  if llista[i]==par1:
    llista.remove(par1)
  i=i+1
  
print (llista)