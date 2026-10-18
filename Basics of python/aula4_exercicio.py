import numpy as np 

def normalize(a):
    normalizado = (a - a.min()) / (a.max() - a.min())
    return normalizado

array1 = np.array([10,20,30,40])

resultado = normalize(array1)
print(resultado)