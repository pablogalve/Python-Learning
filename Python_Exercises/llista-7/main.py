num_par = int(input("Introdueix el número de paraules que ha de tenir la llista"))
llista=[]
i=0
while i<num_par:
  paraula=input("Introdueix la paraula que vols escriure a la llista")
  llista.append(paraula)
  i=i+1
print(llista)

llista2=[]
llista2=list(set(llista))
print("aquestos son els elements sense repetirse "+ str(llista2))