num = int(input("Introdueix el número de paraules que ha de tenir la llista"))
llista=[]
i=0
while i<num:
  paraula=input("Introdueix la paraula que vols escriure a la llista")
  llista.append(paraula)
  i=i+1
print(llista)
llista2=[]
leng=num
j=0
while num>0:
  llista2.append(llista[num-1])
  num=num-1

print("Aquesta es la llista al reves " +str(llista2))