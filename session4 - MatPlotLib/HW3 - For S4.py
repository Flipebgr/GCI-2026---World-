# Sua tarefa é realizar uma análise de Pareto (análise de decil) em um conjunto de dados do MyAnimeList [1], um banco de dados de anime popular contendo informações sobre mais de 17.000 títulos de anime.

# Utilizando os dados baixados e pré-processados ​​(ver Seção 1), anime_dataescreva uma função que execute os seguintes passos:

# Classificar animes pela métrica fornecida:

# Ordene os animes em ordem decrescente com base nos valores da coluna especificada por metric_column.
# Grupo Anime em n Partes iguais:

# Sem alterar a ordem de classificação, divida os animes em n grupos de tamanho igual.
# n é um número natural (inteiro positivo).
# Use pd.qcut()a classificação dos valores da métrica (com method='first') para lidar com o agrupamento. Isso evita problemas com valores duplicados.
# Calcule a proporção para cada grupo:

# Para cada grupo, calcule qual a porcentagem do total geral (de metric_column) que esse grupo representa.
# Isso é conhecido como análise de decil quando n = 10 mas funciona para qualquer valor válido n .
# Classificar grupos e etiquetar:

# Ordene os grupos em ordem decrescente de proporção.
# Identifique-os como "Group 1", "Group 2", ..., "Group n".
# Retorne o resultado como um pandas.Series.

# Contexto:
# O Princípio de Pareto afirma que aproximadamente 80% dos efeitos provêm de 20% das causas. No contexto dos animes, um pequeno número de animes extremamente populares pode ser responsável pela grande maioria da audiência total. Esse princípio é amplamente utilizado em negócios, marketing e análise de dados.



import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import requests
import zipfile
import io

# Download MyAnimeList data from GitHub
# url = 'https://github.com/Hernan4444/MyAnimeList-Database/archive/refs/heads/master.zip'
# r = requests.get(url, stream=True)
# z = zipfile.ZipFile(io.BytesIO(r.content))
# z.extractall()

# Load the anime data
anime_data_raw = pd.read_csv('MyAnimeList-Database-master/data/anime.csv')
# print(f"Raw dataset shape: {anime_data_raw.shape}")
# anime_data_raw.head()

# Preprocessing — Do NOT modify this cell
columns_to_keep = ['MAL_ID', 'Name', 'Score', 'Type', 'Episodes',
                   'Members', 'Completed', 'Watching', 'Dropped', 'Popularity']
anime_data = anime_data_raw[columns_to_keep].copy()

# Remove rows where key metric columns have missing or zero values
anime_data = anime_data.dropna(subset=['Members', 'Completed', 'Watching'])
anime_data = anime_data[(anime_data['Members'] > 0) &
                        (anime_data['Completed'] > 0) &
                        (anime_data['Watching'] > 0)]
anime_data = anime_data.reset_index(drop=True)
# print(f"Dataset shape after preprocessing: {anime_data.shape}")
# print(anime_data.head()) ##Exibindo na tela as 5 primeiras linhas do data frame 

# organized_by = anime_data.sort_values(by="Completed", ascending=False)
# # print(organized_by)

# groups = pd.qcut(organized_by["Completed"].rank(method='first'), q=5)
# # print(groups)

# qnt_groups = organized_by['Completed'].groupby(groups).sum()
# # print(qnt_groups)

# total_general = organized_by['Completed'].sum()
# total_general
# percent_by_group = (qnt_groups/total_general) 
# # new_df = percent_by_group.reindex(index=[1,2,3,4,5])

# percent_by_group.index = range(1, 6)
# percent_by_group.index.name = "Grupo"
# print(percent_by_group)

def homework(anime_data, metric_column, n):
    organized_by = anime_data.sort_values(by=metric_column, ascending=False)
    groups = pd.qcut(organized_by[metric_column].rank(method='first'), q=n)
    qnt_groups = organized_by[metric_column].groupby(groups).sum()

    total_general = organized_by[metric_column].sum()

    percent_by_group = (qnt_groups/total_general)

    percent_by_group = percent_by_group.sort_values(ascending=False)

    percent_by_group.index = [
    f"Group {i}" for i in range(1, n + 1)
    ]

    my_result = percent_by_group
    return my_result



result = homework(anime_data, "Completed", 5)
print(result)

# # Run this cell after completing homework().
# your_answer = homework(anime_data, "Completed", 10)
# display(your_answer)


# case_2_data = pd.DataFrame({
#     "Completed": [40, 30, 20, 10],
# })
# case_2_answer = homework(case_2_data, "Completed", 2)
# display(case_2_answer)

# case_3_data = pd.DataFrame({
#     "Members": [60, 50, 40, 30, 20, 10],
# })
# case_3_answer = homework(case_3_data, "Members", 3)
# display(case_3_answer)