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
import os 

# url = "https://archive.ics.uci.edu/static/public/275/bike+sharing+dataset.zip"

# response = requests.get(url)

# with zipfile.ZipFile(io.BytesIO(response.content)) as z:
#     z.extractall()

#     print("Dataset foi baixado e extraído com sucesso")

#Arquivos -> day.csv Daily aggregated data, cada linha representa 1 ano de informação
#hour.csv -> Hourly data 
df = pd.read_csv("session4 - MatPlotLib/day.csv")
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
# bin_edges = np.arange(0,9500,500) 

# plt.figure(figsize=(10,5))
# plt.hist(df["cnt"], bins=bin_edges, edgecolor="black") #bins = quantidade de barras, edgecolor= Cor das bordas

# plt.title("Quantidade de vezes que os aluguei foram semelhates ao longo do tempo")
# plt.xlabel("Total de alugeis por dia ")
# plt.ylabel("Vezes")

# plt.grid(True)
# plt.show()

# plt.hsit(x, range=()) -> demarcar onde sera o foco do histograma, muito util quando se tem outliers no grafico, e que focar em uma determinada área
# ----------------------------------------EXERCICIO HISTOGRAMA-----------------------------------------------------------------------#
# Solution
# plt.figure(figsize=(10, 4))


# # 10 bins
# plt.subplot(2,1,1)
# plt.hist(df["cnt"], bins = 10, edgecolor="black")

# plt.title("Frequencia de alugueis X dia")
# plt.xlabel("Frequencia de aluguel")
# plt.ylabel("vezes que ocorreu")

# plt.grid(True)


# # 30 bins
# plt.subplot(2,1,2)
# plt.hist(df["cnt"], bins=30, edgecolor="black")
# plt.title("Frequencia de alugueis X dia")
# plt.xlabel("Frequencia de aluguel")
# plt.ylabel("vezes que ocorreu")
# plt.grid(True)

# plt.tight_layout()
# plt.show()

#---------------------------------------EXERCICIO 5.3.1.1----------------------------------------------------------------------------#

# Solution

# import matplotlib.dates as mdates

# # Ensure datetime format
# df["dteday"] = pd.to_datetime(df["dteday"])

# # Create year-month variable
# df["year_month"] = df["dteday"].dt.to_period("M")

# # Group by year-month and compute average rentals
# monthly_avg = df.groupby("year_month")["cnt"].mean() #agrupa por mês e tira a média de cada um. Onde a média de cada mês
# # é a soma de alugueis por dia, dividido pela quantidade de dias do mês



# # Convert PeriodIndex back to timestamp for plotting
# monthly_avg.index = monthly_avg.index.to_timestamp()

# # Plot
# plt.figure(figsize=(12, 5))
# plt.plot(monthly_avg.index, monthly_avg.values, marker='o')
# plt.title("Media de vendas x mes")
# plt.xlabel("mes")
# plt.ylabel("media mensal")


# # Monthly ticks
# plt.gca().xaxis.set_major_locator(mdates.MonthLocator())
# plt.gca().xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m"))


# plt.xticks(rotation = 45)

# plt.tight_layout()
# plt.show()

# -----------------------------------------BOXPLOT---------------------------------------------------------#
# plt.boxplot(df["cnt"], vert=False)
# plt.show()


# -----------------------------------------SCATTER PLOT---------------------------------------------------------#
#como combinar duas variaveis

# plt.figure(figsize=(8,5))

# plt.scatter(df["temp"], df["cnt"], alpha=0.6) # usamos o alpha igual a 0.6 para deixarmos os pontos levemente transparentes
# # o alhpa varia de 0 a 1, quanto menor, mais transparente fica


# plt.title("Temperatua vs total de alugueis", fontsize=14)
# plt.xlabel("Temperatuza normalizada", fontsize=12)
# plt.ylabel("Alugueis totais", fontsize=12)

# plt.xticks(fontsize=10)
# plt.yticks(fontsize=10)

# plt.show()

# -----------------------------------------BUBBLE CHART---------------------------------------------------------#
# Extensão do scatter plot, permite que uma terceira variável afete o tamanho do ponto

# plt.figure(figsize=(8,5))

# parametro = df["cnt"] / 20 
# plt.scatter(
#     df["temp"],
#     df["hum"],
#     s = parametro,
#     alpha=0.5,
#     color="Blue",
#     edgecolors="black"
# )



# plt.title("Temperatua x humidade x quantidade de algueis")
# plt.xlabel("temperatura")
# plt.ylabel("Humidade")

# plt.grid(True, linestyle = "--")
# plt.tight_layout()

# plt.show()


# -----------------------------------------PLOT WITH CATEGORICS DATA---------------------------------------------------------#



# season_map = {
#     1: "Spring",
#     2: "Summer",
#     3: "Autumn",
#     4: "Winter"
# }

# season_avg =  (
#     df.assign(Season=df["season"].map(season_map)) # o map é utilizado para conseguirmos troca os valores numéricos da coluna pela sua devida estação climatica
#     # já o assign serve para criar ou substituir colunas em um novo df, nesse caso criando
#     .groupby("Season")["cnt"]
#     .mean()
#     .reindex(season_map.values()) #groupby vai agrupoar os registros com o mesmo valor(mesma estação), depois ["cnt"] seleciona a tabela de contagem de alugueis e tira a media de cada grupo
# )

# plt.figure(figsize=(10,5))
# plt.bar(season_avg.index, season_avg.values, edgecolor="black", linewidth=1.5) #.values e .index fazem o seguinte -> .values de um dict retorna uma visualização dos valores nele armazenado
# #e o reindex faz a reorganização da series de acordo com o valores fornecido pelo dict

# plt.title("Media de alugueis por temporada")
# plt.xlabel("Temporada")
# plt.ylabel("Media aluguel")
# plt.show()

# -----------------------------------------PLOT WITH CATEGORICS DATA 2---------------------------------------------------------#

# Step 1: Calculate averages by season
casual_avg = df.groupby("season")["casual"].mean()
registered_avg = df.groupby("season")["registered"].mean()

# Step 2: Create x positions
x = np.arange(len(casual_avg)) #Pega a quantidade de elementos da series (casual.avg)
# -> Fazemos isso para criar as coordenadas para posicionar as barras
width = 0.35 #largura de cada barra

plt.figure(figsize=(8, 5))

# Step 3: Plot bars side by side
plt.bar(x - width/2, casual_avg.values, width, label="Casual") #define onde as barras do grupo casual vai ficar posicionado
plt.bar(x + width/2, registered_avg.values, width, label="Registered") # define onde as barras do grupo registrado vai ficar posicioando

# Step 4: Formatting
plt.title("Average Rentals by Season", fontsize=14)
plt.xlabel("Season", fontsize=12)
plt.ylabel("Average Rentals", fontsize=12)

plt.xticks(x, ["Winter", "Spring", "Summer", "Fall"])  # corrected
plt.legend(title="User Type")

plt.grid(axis="y", linestyle="--", alpha=0.5) #define a grade no eixo y, as linhas no estilo tracejado e o alpha de transparencia 0.5

plt.show()