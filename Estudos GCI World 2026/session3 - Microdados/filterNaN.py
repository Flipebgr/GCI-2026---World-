import pandas as pd 
import numpy as np 
from pandas import Series, DataFrame


f1Data = { 
    "TEAM" : ["Mercedes", "Ferraria", "Red Bull Motors", "Hass Formula one team"],
    "PILOTS" : ["Kimi Antoneli and Geroge Russel", "Lewis Hamilton and Charles Leclerc", "Max Verstapen and Lean Lawson", "Rafael Camara and ?"],
    "POSITION" : [1,3,2,4],
    "POINTS" : [220, 100, 198, None]
}

df = pd.DataFrame(f1Data)

nulos = df.isnull().sum() #O isnull verifica a quantidade de valores ausentes por coluna, gerando valores true se for valor ausente e false se for presente. O sum faz a soma por coluna
print(nulos)
organized = df.sort_index()
print(organized)

print("________________________________________________________")
organized_by = df.sort_values(by="POSITION", ascending=True)
print(organized_by)


print("________________________________________________________")
print(df)


# df = pd.DataFrame(tabela)
# df = pd.DataFrame(tabela)
# df = pd.DataFrame(tabela)

