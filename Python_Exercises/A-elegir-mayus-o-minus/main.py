num=int(input("escriu un 1 per a una frase en minuscules que me has de donar en majuscules o 2 si la vols en majuscules primerament donada en minuscules"))
if (num==1):
  frase=input("Escriu una frase en majuscules")
  print(frase.lower())
else:
    frase=input("Escriu una frase en minuscules")
    print(frase.upper())