#Core libraries
import pandas as pd
import numpy as np 

#Visualization libraries
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import seaborn as sns # "Irmão elegante do matplotlib"

# import requests
# import zipfile  
# import io 

# url = "https://archive.ics.uci.edu/static/public/275/bike+sharing+dataset.zip"

# response = requests.get(url)

# with zipfile.ZipFile(io.BytesIO(response.content)) as z:
#     z.extractall()

#     print("Dataset foi baixado e extraído com sucesso")

#Arquivos -> day.csv Daily aggregated data, cada linha representa 1 ano de informação
#hour.csv -> Hourly data 
df = pd.read_csv("day.csv")
print(df.head())


# print(df.describe())

# plt.figure(figsize=(12,6))

# #First subplot
# plt.subplot(2,1,1)
# plt.plot(df["cnt"])
# plt.title("Aluguel de bikes x dia ao longo de 2 anos ")
# plt.xlabel("Dias")
# plt.ylabel("Alugueis totais por dia")
# plt.grid(True)

# #Second subplot
# plt.subplot(2,1,2)
# plt.plot(df["temp"])
# plt.title("Temperatura x dia ")
# plt.xlabel("Dias")
# plt.ylabel("Temperatura")
# plt.grid(True)

# plt.tight_layout()
# plt.show()

# --------------------------------------------------------------------------------------------------#
df["dteday"] = pd.to_datetime(df["dteday"])

# plt.figure(figsize=(12,6))
# plt.plot(df["dteday"], df["cnt"])

# plt.title("Algueis ao longo do tempo")
# plt.xlabel("Data")
# plt.ylabel("Aluguel")

# plt.gca().xaxis.set_major_locator(mdates.MonthLocator()) #pega o grafico atual no eixo x e definir um locator, isto é, um objeto que determina as posições dos marcadores principais (marcador x, nesse caso)
# plt.gca().xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m")) #define como os marcadores irão aparecer

# plt.xticks(rotation=45) #define a rotação do locator do eixo x, para não colidirem um com o outro
# plt.tight_layout() #usado para ajustar o espaçamento de um gráfico
# plt.show()

# --------------------------------------------------------------------------------------------------#

# plt.figure(figsize=(12,6))

# plt.plot(df["dteday"], df["casual"], label="Usuários casuais")
# plt.plot(df["dteday"], df["registered"], label="Usuários registrados")

# plt.title("User casual x user registrado ao longo do tempo")
# plt.xlabel("date")
# plt.ylabel("Numero de alugueis")

# plt.gca().xaxis.set_major_locator(mdates.MonthLocator())
# plt.gca().xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m"))

# plt.xticks(rotation=45)

# plt.legend()
# plt.grid(True)

# plt.tight_layout()
# plt.show()

# -----------------------------------------HISTOGRAMA---------------------------------------------------------#
# O histograma mostra a quantidae de vezes que determinado acontecimento ocorreu
bin_edges = np.arange(0,9500,500) 

plt.figure(figsize=(10,5))
plt.hist(df["cnt"], bins=bin_edges, edgecolor="black") #bins = quantidade de barras, edgecolor= Cor das bordas

plt.title("Quantidade de vezes que os aluguei foram semelhates ao longo do tempo")
plt.xlabel("Total de alugeis por dia ")
plt.ylabel("Vezes")

plt.grid(True)
plt.show()

# plt.hsit(x, range=()) -> demarcar onde sera o foco do histograma, muito util quando se tem outliers no grafico, e que focar em uma determinada área
