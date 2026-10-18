import pandas as pd 
import requests, zipfile 
from io import StringIO
import io 


z = zipfile.ZipFile(path)

# for arquivo in z.namelist():
#     print(arquivo)

with zipfile.ZipFile(path) as z:
    #print(z.namelist())
    print ("------------------------------------------------------------------------------")

    with z.open("Microdados_Enade_Licenciaturas_2025_defeso/2.DADOS/microdados2025_arq1.txt") as arquivo:
        df = pd.read_csv(
        arquivo,
        sep = ";",  
        encoding = "latin1",
        nrows = 1000
        )


print(df.head())
print ("------------------------------------------------------------------------------")
print(df.shape)
print ("------------------------------------------------------------------------------")
df.info()
print ("------------------------------------------------------------------------------")
print(df.dtypes)
print ("------------------------------------------------------------------------------")
print(df.isnull().sum())


# print ("------------------------------------------------------------------------------------------------------------------------------------------------------------")

# with zipfile.ZipFile(path) as f:
#     with f.open("Microdados_Enade_Licenciaturas_2025_defeso/1.LEIA-ME/Dicionário_arquivos_variáveis_microdados_Enade_Licenciaturas_2025.xlsx") as arquivo:
#         df2 = pd.read_excel(
#             arquivo,
#             nrows = 1000
#             )

# print(df2.head())

# print(df["CO_IES"].nunique()) df["CO_IES"] seleciona uma coluna do dataframe, retornando um series. O método nunique() é aplicado a essa série para contar o número de valores únicos presentes na coluna "CO_IES". O resultado é o número de instituições de ensino superior distintas representadas nos dados.
# print(df["CO_CURSO"].nunique()) o mesmo exemplo anterior, porém agora para a coluna "CO_CURSO"    
# print(df["CO_IES"].value_counts().head(10)) aqui a gente verifica a frequencia de cada valor único na coluna "CO_IES" e retorna os 10 valores mais frequentes, juntamente com suas contagens. Isso nos dá uma ideia de quais instituições de ensino superior aparecem com mais frequência nos dados.
df_ufpa = df[df["CO_IES"] == 569]
print(df_ufpa.head())
print(df_ufpa.shape)
