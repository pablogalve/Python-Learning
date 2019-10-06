frase1=input("digues una frase")
frase2=input("digues una altra frase")
long1=len(frase1)
long2=len(frase2)
print(long1)
print(long2)
if long1<long2:
  print("la segona frase es mes llarga que la primera")
if long2<long1:
  print("la primera frase es mes llarga que la segona")
if (long1==long2):
  print("les dues frases son igual de llargues")
