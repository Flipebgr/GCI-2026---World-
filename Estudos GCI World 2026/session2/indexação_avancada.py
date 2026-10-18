import numpy as np

array1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(array1)

print("A forma da matriz é:", array1.shape)
# print(array1[0,2])
# print(array1.ndim)
print(array1[[0,1], [1,2]])




# array2 = np.arange(0,12, 2) #no.arange cria um array com valores de 0 a 12, com passo de 2
# print(array2)

# print(array2[[1,4,-1]])
# print(array2.ndim) #ndim retorna o número de dimensões do array

array3 = np.arange(20).reshape(4,5)
print(array3.ndim)
print(array3.shape)
print(array3)

 
print(array3[[1,1,2,2], [-1,-2,-3,-5]])
print(array3[array3 % 2 == 0 ])

arr4 = array3 > 10
print(arr4)