import numpy as np 

array_a = np.array([6,7,8]) 
#print (array_a[2])

a = [1, 4, 6, 12]
a = np.array(a) # Para converter uma lista para um array numpy, basta passar a lista como argumento para a função np.array().
print("a:", a)
#print("type of a:", type(a)) #class: numpy.ndarray


b = [2, 4 ,5 ,6]
b = np.array(b) # Para converter uma lista para um array do numpy, basta passar a lista como argumento para a função np.array().
print("b:",b)


# a_list = a.tolist() # Para converter um array do numpy para uma lista, basta chamar o método tolist() do array
# print("a_list:", a_list)
# print("type of a_list:", type(a_list)) #class: list

## Arithmetic operations with numpy arrays 

## Addition 
soma = np.add(a,b)
print("Soma:", soma)

# ou como a e b já estão em np.arrays, podemos apenas somá-los diretamente:
add = a + b
print("soma2:", add)

## Subtraction
sub = np.subtract(a,b)
print("Subtração:", sub)

##Multiplication
mult = np.multiply(a,b)
print("Multiplicação:", mult)

## division
div = np.divide(a,b)
print("Divisão:", div)

