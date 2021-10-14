def migratoryBirds(arr):
    lista = {}
    for element in arr:
        try:
            lista[element] += 1
        except:
            lista[element] = 1
    maks = 0
    liczba = 0
    for element in lista:
        if(lista[element] > maks):
            maks = lista[element]
            liczba = element
    return liczba

print(migratoryBirds([1,4,4,4,5,3]))