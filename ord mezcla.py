def partirLista(lista, inicio, fin):
    parte = []
    pos = inicio
    while pos < fin:
        parte.append(lista[pos])
        paso = 1
        pos = pos + paso
    return parte


def merge(arrayA, arrayB):
    arrayC = []
    a = 0
    b = 0

    while a < len(arrayA) and b < len(arrayB):
        if arrayA[a] < arrayB[b]:
            arrayC.append(arrayA[a])
            paso = 1
            a = a + paso
        else:
            arrayC.append(arrayB[b])
            paso = 1
            b = b + paso

    while a < len(arrayA):
        arrayC.append(arrayA[a])
        paso = 1
        a = a + paso

    while b < len(arrayB):
        arrayC.append(arrayB[b])
        paso = 1
        b = b + paso

    return arrayC


def mergesort(array):
    n = len(array)
    if n <= 1:
        return array

    mitad = n // 2
    arrayUno = partirLista(array, 0, mitad)
    arrayDos = partirLista(array, mitad, n)

    arrayUno = mergesort(arrayUno)
    arrayDos = mergesort(arrayDos)

    return merge(arrayUno, arrayDos)


numeros = [14, 7, 3, 12, 9, 11, 6, 2]

print(f'Lista original: {numeros}')

ordenada = mergesort(numeros)

print(f'Lista ordenada: {ordenada}')