import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

shopCar = {
    "Marca": [
        "BMW", "BMW",
        "Audi", "Audi",
        "Porsche", "Porsche",
        "Ferrari", "Ferrari"
    ],

    "Modelo": [
        "M2 Competition", "M3 Competition",
        "RS3", "RS6",
        "911 Carrera", "718 Cayman",
        "Roma", "296 GTB"
    ],

    "Vendas_2024": [
        120, 95,
        110, 80,
        75, 60,
        35, 25
    ],

    "Vendas_2025": [
        145, 115,
        130, 100,
        90, 85,
        40, 35
    ]
}

df = pd.DataFrame(shopCar)


# VendasPorMarca2024 = df.groupby("Marca")["Vendas_2024"].mean()
# VendasPorMarca2025 = df.groupby("Marca")["Vendas_2025"].mean()

# x = np.arange(len(VendasPorMarca2024))
# width = 0.35

# plt.figure(figsize=(10,5))
# plt.bar(x - width/2, VendasPorMarca2024.values, width, label="2024", edgecolor="black")
# plt.bar(x + width/2, VendasPorMarca2025.values, width, label="2025", edgecolor="black")

# plt.title("Comparação de vendas por modelo 2024 x 2025", fontsize=14)
# plt.xlabel("modelo", fontsize = 12)
# plt.ylabel("Vendas", fontsize = 12)
# plt.legend(title="Ano") #adicionar uma legenda do tipo de carro 

# plt.xticks(x, ["BMW","Audi", "Porsche", "Ferrari"])
# plt.grid(axis="y",linestyle="--", alpha=0.5)
# plt.show()


# labels = ['Bmw', 'Porsche', 'Audi', 'Ferrari']
# sizes = [20,30,10,40]
# colors = ['Blue', 'Gold','Silver','Red']
# explode = [0,0.1,0,0]


# plt.pie(x=sizes,
#         explode=explode,
#         labels=labels,
#         colors=colors,
#         autopct='%1.1f%%',
#         shadow=True,
#         startangle=90
#         )

# plt.show()


#---------------------PLOT BAR VENDAS X MODELO-----------------------------------#


vendas_agregadas = df.groupby("Marca")[["Vendas_2024", "Vendas_2025"]].sum()
vendas_agregadas["total"] = (vendas_agregadas["Vendas_2024"] + vendas_agregadas["Vendas_2025"])

modelos = df.groupby("Modelo")[["Vendas_2024", "Vendas_2025"]].sum()

# Calcular total de vendas por modelo
modelos["total"] = (
    modelos["Vendas_2024"] +
    modelos["Vendas_2025"]
)
x = np.arange(len(modelos))
width = 0.35

plt.figure(figsize=(12,5))
plt.bar(x, modelos["total"].values, width, label="Modelos", edgecolor="black") #plt.bar(x, valores numéricos que determinam a altura das barrar, largura das barras)

plt.title("vendas totais por modelo (2024-2025)")
plt.xlabel("Modelo")
plt.ylabel("Quantidade total de vendas")

plt.xticks(x,modelos.index, rotation=45, ha="right")


plt.grid(axis="y", linestyle="--", alpha=0.5)
plt.tight_layout() #ajusta aotumaticamente os valore das figuras
plt.show()