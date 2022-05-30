def timSort(lista):
    for i in range(len(lista)):
        for j in range(i):
            if lista[i] < lista[j]:
                lista[i], lista[j] = lista[j], lista[i]
    return lista

lista = [54,26,93,17,77,31,44,55,20]
print(timSort(lista))

def murgeSort(lista):
    if len(lista) > 1:
        meio = len(lista) // 2
        esquerda = lista[:meio]
        direita = lista[meio:]
        murgeSort(esquerda)
        murgeSort(direita)
        i = j = k = 0
        while i < len(esquerda) and j < len(direita):
            if esquerda[i] < direita[j]:
                lista[k] = esquerda[i]
                i += 1
            else:
                lista[k] = direita[j]
                j += 1
            k += 1
        while i < len(esquerda):
            lista[k] = esquerda[i]
            i += 1
            k += 1
        while j < len(direita):
            lista[k] = direita[j]
            j += 1
            k += 1
    return lista

lista = [54,26,93,17,77,31,44,55,20]
print(murgeSort(lista))

def quicksort(lista):
    if len(lista) > 1:
        pivo = lista[0]
        menores = [x for x in lista[1:] if x <= pivo]
        maiores = [x for x in lista[1:] if x > pivo]
        return quicksort(menores) + [pivo] + quicksort(maiores)
    return lista

lista = [54,26,93,17,77,31,44,55,20]
print(quicksort(lista))
