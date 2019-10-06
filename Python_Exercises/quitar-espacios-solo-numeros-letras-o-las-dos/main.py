frase=input("Digues una frase")
frase=frase.replace(' ','')
print("Ara la torno sense espais")
print(frase)
if frase.isdigit():
  print("La frase nomes te numeros")
else:
  if frase.isalpha():
    print("La frase nomes te lletres")
  else:
    if frase.isalnum():
      print("La frase te numeros i lletres")