import numpy as np

""""
Bubble Sort: troca elementos adjacentes até que a lista esteja ordenada.
"""
def bubble_sort(vetor):
    n = len(vetor)
    comparacoes, num_troca = 0, 0
    troca = True
    while troca:
        troca = False
        for i in range(n - 1):
            comparacoes += 1
            if vetor[i] > vetor[i + 1]:
                vetor[i], vetor[i + 1] = vetor[i + 1], vetor[i]
                troca = True
                num_troca += 1
        n -= 1
    return vetor, comparacoes, num_troca

""""
 Insertion Sort: percorre um vetor da esquerda para a direita, ordenando os elementos à esquerda à medida que avança.
"""
def insertion_sort(vetor):
    n = len(vetor)
    comparacoes, num_troca = 0, 0
    for index in range(1, n):
        currentValue = vetor[index]
        position = index
        comparacoes += 1
        while position > 0 and vetor[position - 1] > currentValue:
            vetor[position] = vetor[position - 1]
            position -= 1  # Ajuste aqui
            num_troca += 1
        vetor[position] = currentValue
    return vetor, comparacoes, num_troca

""""
Quick Sort:  divide a lista em torno de um elemento pivô e ordena recursivamente as sublistas resultantes
"""
def quick_sort(vetor):
    global comparacoes, num_troca
    comparacoes, num_troca = 0, 0
    quick_sort_helper(vetor, 0, len(vetor) - 1)

    return vetor, comparacoes, num_troca


def quick_sort_helper(vetor, first, last):
    global num_comparacoes, num_troca
    if first < last:
        splitpoint = partition(vetor, first, last)

        quick_sort_helper(vetor, first, splitpoint - 1)
        quick_sort_helper(vetor, splitpoint + 1, last)


def partition(vetor, first, last):
    global comparacoes, num_troca
    pivo = vetor[first]

    esquerda = first + 1
    direita = last

    done = False
    while not done:

        comparacoes += 1
        while esquerda <= direita and vetor[esquerda] <= pivo:
            esquerda = esquerda + 1
            comparacoes += 1
        comparacoes += 1
        while vetor[direita] >= pivo and direita >= esquerda:
            direita = direita - 1
            comparacoes += 1

        if direita < esquerda:
            done = True
        else:
            temp = vetor[esquerda]
            vetor[esquerda] = vetor[direita]
            vetor[direita] = temp
            num_troca += 1

    temp = vetor[first]
    vetor[first] = vetor[direita]
    vetor[direita] = temp

    return direita

""""
Merge Sort: divide a lista em metades, ordena cada metade e depois mescla as metades ordenadas.
"""
def merge_sort(vetor):
    global comparacoes, num_troca
    num_troca, comparacoes = 0, 0
    vetor = merge_sort_helper(vetor)
    return vetor, comparacoes, num_troca


def merge_sort_helper(vetor):
    global comparacoes, num_troca
    num_troca, comparacoes = 0, 0
    if len(vetor) <= 1:
        return vetor

    meio = len(vetor) // 2

    esquerda = merge_sort_helper(vetor[:meio])
    direita = merge_sort_helper(vetor[meio:])

    return merge(esquerda, direita)


def merge(esquerda, direita):
    global comparacoes, num_troca
    resultado = []
    i = j = 0

    while i < len(esquerda) and j < len(direita):
        comparacoes += 1
        if esquerda[i] < direita[j]:
            num_troca += 1
            resultado.append(esquerda[i])
            i += 1
        else:
            num_troca += 1
            resultado.append(direita[j])
            j += 1

    resultado.extend(esquerda[i:])
    resultado.extend(direita[j:])

    return np.array(resultado)

""""
Shell Sort: divide a lista em subgrupos menores e os ordena independentemente, reduzindo gradualmente a lacuna entre os 
elementos comparados.
"""
def shell_sort(vetor):
    global comparacoes, num_troca
    h = len(vetor) // 2
    comparacoes = 0
    num_troca = 0
    while h > 0:

        for startposition in range(h):
            gapInsertionSort(vetor, startposition, h)

        h = h // 2

    return vetor, comparacoes, num_troca


def gapInsertionSort(vetor, start, h):
    global comparacoes, num_troca
    for i in range(start + h, len(vetor), h):
        currentvalue = vetor[i]
        position = i
        comparacoes += 1

        while position >= h and vetor[position - h] > currentvalue:
            num_troca += 1
            vetor[position] = vetor[position - h]
            position = position - h

        vetor[position] = currentvalue

"""
Selection sort: passar sempre o menor valor do vetor para a primeira posição, depois o segundo menor valor para a 
segunda posição e assim sucessivamente.
"""
def selection_sort(vetor):
    n = len(vetor)
    comparacoes, num_troca = 0, 0

    for i in range(n):
        min = i
        for j in range(i + 1, n):
            comparacoes += 1
            if vetor[j] < vetor[min]:
                min = j

        if min != i:
            vetor[i], vetor[min] = vetor[min], vetor[i]
            num_troca += 1

    return vetor, comparacoes, num_troca

"""
Radix Sort: ordena os elementos processando seus dígitos individuais, em vez de comparar diretamente os valores 
dos elementos.
"""
def radix_sort(vetor):
    comparacoes, trocas = 0, 0
    return vetor, comparacoes, trocas

""""

Bucket Sort: divide a lista em compartimentos, distribui os elementos em cada compartimento com base em seu valor e, 
em seguida, ordena cada compartimento antes de combiná-los para obter a lista ordenada.
"""
def bucket_sort(vetor):
    comparacoes, trocas = 0, 0
    return vetor, comparacoes, trocas
