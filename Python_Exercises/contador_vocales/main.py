def vowel_consonant_count(s):
  s=input("Digues una paraula")
    nv = 0
    nc = 0
    for lletra in s :
        if lletra in "aeiouAEIOU":
            nv = nv + 1
        else:
            nc = nc + 1
    return (nv , nc)
