import numpy as np
import pandas as pd
from pandas import DataFrame
#Utilizando o conjunto de dados MyAnimeList [1], calcule a média de `Score` para cada valor de `Type` e retorne os resultados ordenados em **ordem decrescente**.
# Bibliotecas para baixar dados da web e manipular arquivos ZIP
import requests, zipfile
from io import StringIO
import io

# # Especificar a URL que contém os dados
# url = 'https://github.com/Hernan4444/MyAnimeList-Database/archive/refs/heads/master.zip'

# # Baixar os dados da URL
# r = requests.get(url, stream=True)

# # Ler e extrair o arquivo ZIP
# z = zipfile.ZipFile(io.BytesIO(r.content))
# z.extractall()

# Carregar e limpar os dados
anime_data = pd.read_csv('MyAnimeList-Database-master/data/anime.csv')
anime_data_extracted = anime_data[anime_data['Score'] != 'Unknown'].copy()
anime_data_extracted['Score'] = pd.to_numeric(anime_data_extracted['Score'])



# # print(anime_data_extracted)
# print(anime_data_extracted.info)
# print("______________________________________________")
# print(anime_data_extracted.describe)



# print(anime_data_extracted["Type"].unique())
# print(anime_data_extracted["Type"].value_counts())
# print(anime_data_extracted["Type"].describe())

# df_series = anime_data_extracted.loc[:, ["Type", "Score"]]
# print(df_series)
# count_TV = (anime_data_extracted["Type"] == "TV").sum()
# TV_series = anime_data_extracted.loc[
#     anime_data_extracted['Type'] == "TV", 
#     "Score"
# ]

# print(TV_series.mean())
# print(TV_series.sum()/count_TV)

# print(df_series.head())
# print(df_series.dtypes)
# print(df_series.isnull().sum())

# df = pd.DataFrame(anime_data_extracted[["Type", "Score"]] == "TV")
# print(df.describe())
# df_series = anime_data_extracted.loc[:, ["Type", "Score"]]

# Type = df_series["Type"].unique()
# print(Type.shape)

def homework(anime_data_extracted):
    # Write your answer here
    df_series = anime_data_extracted.loc[:, ["Type", "Score"]]
    Type = df_series["Type"].unique()
    list_notes_scorer = []
    tamanho = len(Type)
    for i in range(tamanho):
        X_series = anime_data_extracted.loc[
            anime_data_extracted['Type'] == Type[i], "Score"
        ]
        mean = X_series.mean()
        list_notes_scorer.append(mean)
    series = pd.Series(data=list_notes_scorer, index=Type)

    return series

your_answer = homework(anime_data_extracted)
print(your_answer)


# case_2_data = pd.DataFrame({
#     "Type": ["TV", "TV", "Movie", "Movie", "OVA"],
#     "Score": [8.0, 6.0, 9.0, 7.0, 5.0],
# })
# case_2_answer = homework(case_2_data)
# display(case_2_answer)