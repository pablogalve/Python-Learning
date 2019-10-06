num_par = int(input("Introdueix el número de paraules que ha de tenir la llista"))
llista=[]
i=0
while i<num_par:
  paraula=input("Introdueix la paraula que vols escriure a la llista")
  llista.append(paraula)
  i=i+1
print(llista)

num_par2 = int(input("Introdueix el número de paraules que ha de tenir la llista"))
llista2=[]
j=0
while j<num_par2:
  paraula2=input("Introdueix la paraula que vols escriure a la llista")
  llista2.append(paraula2)
  j=j+1
print(llista2)

j=0
veces=0
while j<num_par2:
  veces=llista.count(llista2[j])
  while veces!=0:
    llista.remove(llista2[j])
    veces=veces-1
  j=j+1

print(llista)