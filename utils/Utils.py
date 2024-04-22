from time import time
import timeit

from Sort.Sort import *


def all_sort(sort_type, vetor):
    novoVetor = vetor.copy()

    match sort_type:
        case 1:
            print("\nBUBBLE SORT")
            inicio = time()
            novoVetor, comparacoes, trocas = bubble_sort(novoVetor)
            total = time() - inicio
            print(f'{novoVetor}\n- Trocas: {trocas}\n- Comparações: {comparacoes}\n- Tempo de resposta: {total}')
            return total
        case 2:
            print("\nSHELL SORT")
            inicio = time()
            novoVetor, comparacoes, trocas = shell_sort(novoVetor)
            total = time() - inicio
            print(f'{novoVetor}\n- Trocas: {trocas}\n- Comparações: {comparacoes}\n- Tempo de resposta: {total}')
            return total
        case 3:
            print("\nQUICK SORT")
            inicio = time()
            novoVetor, comparacoes, trocas = quick_sort(novoVetor)
            total = time() - inicio
            print(f'{novoVetor}\n- Trocas: {trocas}\n- Comparações: {comparacoes}\n- Tempo de resposta: {total}')
            return total
        case 4:
            print("\nINSERTION SORT")
            inicio = time()
            novoVetor, comparacoes, trocas = insertion_sort(novoVetor)
            total = time() - inicio
            print(f'{novoVetor}\n- Trocas: {trocas}\n- Comparações: {comparacoes}\n- Tempo de resposta: {total}')
            return total
        case 5:
            inicio = time()
            print("\nMERGE SORT")
            inicio = time()
            novoVetor, comparacoes, trocas = merge_sort(novoVetor)
            total = time() - inicio
            print(f'{novoVetor}\n- Trocas: {trocas}\n- Comparações: {comparacoes}\n- Tempo de resposta: {total}')
            return total
        case 6:
            inicio = time()
            print("\nSELECTION SORT")
            inicio = time()
            novoVetor, comparacoes, trocas = selection_sort(novoVetor)
            total = time() - inicio
            print(f'{novoVetor}\n- Trocas: {trocas}\n- Comparações: {comparacoes}\n- Tempo de resposta: {total}')
            return total
        case 7:
            inicio = time()
            print("\nRADIX SORT")
            inicio = time()
            novoVetor, comparacoes, trocas = radix_sort(novoVetor)
            total = time() - inicio
            print(f'{novoVetor}\n- Trocas: {trocas}\n- Comparações: {comparacoes}\n- Tempo de resposta: {total}')
            return total
        case 8:
            inicio = time()
            print("\nBUCKET SORT")
            inicio = time()
            novoVetor, comparacoes, trocas = bucket_sort(novoVetor)
            total = time() - inicio
            print(f'{novoVetor}\n- Trocas: {trocas}\n- Comparações: {comparacoes}\n- Tempo de resposta: {total}')
            return total
        case _:
            pass


def test(vetor):
    for i in range(9):
        all_sort(i, vetor)
