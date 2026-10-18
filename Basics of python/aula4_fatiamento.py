import numpy as np 

array_a = np.array([
    [7,8,5,23,32],
    [6,43,3,2,1]
    ])
#print("array_a indexaxdo:", array_a[0,1]) # indexing with a list of indices
#print ("array_a usando : ", array_a[:,2]) 

#print("----------------------------------")

#print("Array utilizando o método do fatiamento(slicing):", array_a[:, 0:3]) # slicing with a range of indices

sum= np.sum(array_a, axis=0) # sum of all elements in the array,
print("A soma é:", sum) # aqui a soma é por coluna, pois o axis=0 indica que a soma deve ser feita ao longo das linhas (ou seja, somando os elementos de cada coluna).
# 7 + 6, 8 + 43, 5 + 3, 23 + 2, 32 + 1



sum= np.sum(array_a, axis=1) # sum of all elements in the array,
print("A soma é:", sum) # aqui a soma é por linha, pois o axis=1 indica que a soma deve ser feita ao longo das colunas (ou seja, somando os elementos de cada linha). 
# 7 + 8 + 5 + 23 + 32 = 75
# 6 + 43 + 3 + 2 + 1 = 55


## Ao utilzar as funções universais em matrizes bidimensionais é necessário especificar o eixo (axis) em que as operações irão ocorrer.


