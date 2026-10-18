import pandas as pd 
import numpy as np
import numpy.random as np_random
from pandas import Series, DataFrame



# series = Series([12,20,30,21,3,45], index=['a','b','c','d','e','f'])
# print(series['c'])

# print(series.index)
# print(series.values)


shopCar = {
    'ID': [1,2,3,4],
    'model': ['BMW', 'Audi', 'Ferrrari', 'Pagani'],
    'HP' : [360,400, 680, 880],
    'price' : [230000, 400000, 1000000, 7850000]
}

df = DataFrame(shopCar)
df = df.set_index('ID')
# print(df)


print(df.head())