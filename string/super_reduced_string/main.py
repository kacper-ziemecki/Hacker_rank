  #!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superReducedString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def superReducedString(s):
  napis = s 
  while(True):
    indeks = -1
    usuwanie = False
    for element in napis[1:]:
      indeks += 1
      if(element == napis[indeks]):
        napis = napis[:indeks] + napis[indeks + 2:]
        usuwanie = True
        print(napis)
        break
    if(not usuwanie):
      return
if(__name__ == '__main__'):
    s = input()
    result = superReducedString(s)
