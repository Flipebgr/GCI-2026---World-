import numpy as np
import pandas as pd
from pandas import Series, DataFrame

f1Data = { 
    "TEAM" : ["Mercedes", "Ferraria", "Red Bull Motors", "Hass Formula one team"],
    "PILOTS" : ["Kimi Antoneli and Geroge Russel", "Lewis Hamilton and Charles Leclerc", "Max Verstapen and Lean Lawson", "Rafael Camara and ?"],
    "POSITION" : [1,3,2,4],
    "POINTS" : [220, 100, 198, None]
}

f1Cars = {
    "TEAM": [
        "Mercedes",
        "Ferraria",
        "Red Bull Motors",
        "Alpine Formula one team"
    ],
    "ENGINE": [
        "Mercedes",
        "Ferrari",
        "Honda RBPT",
        "Ferrari"
    ],
    "CHASSIS": [
        "W16",
        "SF-25",
        "RB21",
        "VF-25"
    ],
    "TOP_SPEED": [
        345,
        350,
        355,
        340
    ],
    "WINS": [
        3,
        1,
        5,
        0
    ]
}

df_Data = pd.DataFrame(f1Data)
df_Cars = pd.DataFrame(f1Cars)

# inner_join = pd.merge(df_Data, df_Cars, on="TEAM")
# # print('__________________________________________')
# left_join = pd.merge(df_Data, df_Cars, on="TEAM", how='left') # quando usamos o parametro "how" não significa que ele só usara a tabela especificada, mas sim que ela irá preservar a tabela especificada
# right_join = pd.merge(df_Data, df_Cars,on="TEAM", how='right')
# full_join = pd.merge(df_Data,df_Cars,on="TEAM",how='outer')

# print(left_join)

# print('__________________________________________')

# print(right_join)

# print('__________________________________________')

# print(full_join)

concatenados = pd.concat([df_Data,df_Cars], ignore_index=True, axis=1) #o ignore_index basicamente elimina as duplicatas dos indices, ele cria novamente os indices, organizando o index da concatenação
print(concatenados)
