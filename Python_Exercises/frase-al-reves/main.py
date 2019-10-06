
frase=input("Digues una frase")
print("Ara la tornare al reves")
long=len(frase)
al_reves=""
for i in range(long):
  al_reves= al_reves +frase[long-1]
  long=long-1

print(al_reves)