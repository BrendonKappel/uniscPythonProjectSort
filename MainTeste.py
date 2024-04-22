import sys

import numpy as np
from numpy import random as rd
import matplotlib.pyplot as plt

import Sort.Sort
from utils.Utils import all_sort

sys.setrecursionlimit(10000000)
# Para testar: Lista de números em ordem aleatória.
vetor1 = np.array([8, 5, 1, 7, 9, 4, 10, 3, 6, 2])
bublle = all_sort(1, vetor1)
shell = all_sort(2, vetor1)
quick = all_sort(3, vetor1)
insertion = all_sort(4, vetor1)
merge = all_sort(5, vetor1)
selection = all_sort(6, vetor1)


# Para testar: Uma lista que já está ordenada.
vetor2 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# Para testar: Uma lista classificada em ordem decrescente.
vetor3 = np.array([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])
# Para testar: Uma lista contendo elementos repetidos.
vetor4 = np.array([8, 5, 1, 7, 9, 4, 10, 3, 6, 2, 8, 5, 1])
# Para testar: Uma lista vazia.
vetor5 = np.array([])
# Para testar: Uma lista contendo apenas um elemento.
vetor6 = np.array([5])

vetor7 = np.array([6, 9, 6, 7, 6, 5, 6, 6, 2, 6])

vetor8 = rd.randint(0, 10000, 1000)

# é só teste, depois da pra criar uma classe separada
algoritmos = ['Bubble Sort', 'Shell Sort', 'Quick Sort', 'Insertion Sort', 'Merge Sort', 'Selection Sort']
tempos = [bublle, shell, quick, insertion, merge, selection]  # tempos de execução em segundos

# Criar o gráfico de barras
plt.bar(algoritmos, tempos, color='skyblue')

# Adicionar rótulos e título
plt.xlabel('Algoritmos de Ordenação')
plt.ylabel('Tempo de Execução (s)')
plt.title('Comparação de Tempos de Execução de Algoritmos de Ordenação')

# Rotacionar os rótulos do eixo x para melhor legibilidade
plt.xticks(rotation=45, ha='right')

# Mostrar o gráfico
plt.tight_layout()
plt.show()


