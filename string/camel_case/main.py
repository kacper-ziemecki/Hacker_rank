def solve():
  napis = input()
  slowa = 1
  duza_liczba = "QWERTYUIOPASDFGHJKLZXCVBNM"
  for element in napis:
    if(element in duza_liczba):
      slowa += 1 
  print(slowa)

solve()