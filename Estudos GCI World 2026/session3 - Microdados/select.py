import pandas as pd
from pandas import Series, DataFrame


## | -> significa OR
## & -> significa AND

dados = {
    "NUM_ANO" : [2024, 2024, 2024, 2024, 2024],
    "CO_CURSO" : [101, 231, 125, 183, 332],
    "CO_IES" : [569, 569, 569, 569, 569],
    "CO_MODALIDADE" : [1, 1, 1, 1, 2],

}

df = pd.DataFrame(dados)
print(df.head())

print("--------------------------------------")
# print(df.loc[:,"CO_CURSO"])
print(df[(df["CO_MODALIDADE"] == 1) & (df["CO_CURSO"] == 101)])

df.loc[
    (df["CO_MODALIDADE"] == 1 ) 
    & 
    (df["CO_CURSO"] == 101)
]

# print(df.iloc[0:2, 0:4]) # iloc só aceita números inteiros como indice
# print(df["CO_CURSO"]) #loc aceita números e rótulos como indice 

# print(df.at[1, "CO_CURSO"])

# print(df.iat[4,1])

