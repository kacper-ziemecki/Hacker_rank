import math
def permutacje(napis, indeks):
  napis = napis[indeks: len(napis)] 
  lista_wynik = []
  maks_dluogosc_jednego = math.floor(len(napis) / 2)
  for dlugosc in range(1, maks_dluogosc_jednego + 1):
    napis_jeden = napis[:dlugosc] 
    napis_dwa = napis[dlugosc: len(napis)]
    if(napis_jeden == napis_dwa):
      lista_wynik.append([napis_jeden, napis_dwa])
  
  if(not lista_wynik):
    return None
  maks_dlugosc = 0
  maks_lista = []
  for element in lista_wynik:
    if(len(element[0]) >= maks_dlugosc):
      maks_dlugosc = len(element[0]) 
      maks_lista = element 
  return maks_lista

def solve():
  napis = input()
  przestawienia = 0  
  indeks = -1
  for element in napis:
    print("indeks: " + str(indeks))
    if(indeks < len(napis)):
      indeks += 1
      najwiekrzy_sub = permutacje(napis, indeks)
      if(najwiekrzy_sub):
        przestawienia += len(najwiekrzy_sub[0])
        indeks += len(najwiekrzy_sub[0]) * 2 
      else:
        przestawienia += 1
        # print(przestawienia)
  print(przestawienia)
      
solve()