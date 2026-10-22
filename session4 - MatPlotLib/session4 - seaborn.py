import seaborn as sns
import matplotlib as mp
import matplotlib.pyplot as plt
import pandas as pd


df = pd.read_csv("session4 - MatPlotLib/day.csv")
# print(df.head())


df["Season"] = df["season"].map({
    1: "Winter",
    2: "Spring",
    3: "Summer",
    4: "Autum"
}
)

df["Working Day"] = df["workingday"].map({
    0: "No",
    1: "Yes",
})

plt.figure(figsize=(10,5))


#------------------------Plotagem de barra usando o seaborn--------------------------------#
# sns.barplot(
#     data=df,
#     x="Working Day",
#     y = "cnt",
#     hue = "Season",
#     estimator="mean",
#     errorbar=None
# )

# plt.title("Media de alugueis por dias trabalhos na semana")
# plt.xlabel("Dia útil")
# plt.ylabel("Meida de alugueis")

# plt.tight_layout()
# plt.show()

#---------------------------Coeficiente de correlação---------------------------#

numeric_df = df[[
    "temp",
    "hum",
    "windspeed",
    "casual",
    "registered",
    "cnt",

]]

corr_matrix = numeric_df.corr()






plt.figure(figsize=(10,5))


sns.heatmap(
    corr_matrix,
    annot=True,
    cmap="coolwarm",
    fmt = ".2f",
    center=0,
    square=True,
    linewidths=0.5
)

plt.title("Matriz de correlação Heatmap")
plt.tight_layout()
plt.show()