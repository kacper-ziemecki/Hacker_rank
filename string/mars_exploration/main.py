def solve():
  napis = input()
  ilosc_sos = len(napis) / 3 
  wszystkie_zmiany = 0
  for indeks in range(0, len(napis), 3):
    dany_napis = napis[indeks: indeks + 3]#zmienić
    zmiany = 0
    poprawny_sos = "SOS"
    indeks = -1
    for element in dany_napis:
      indeks += 1 
      if(element != poprawny_sos[indeks]):
        zmiany += 1
    wszystkie_zmiany += zmiany
  print(wszystkie_zmiany)

solve()
