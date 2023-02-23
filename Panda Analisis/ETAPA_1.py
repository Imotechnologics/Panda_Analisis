# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 07:34:18 2023

@author: DvildmonPsyAres
"""
import pandas as pd


# abrirmos la informacion del archivo de Totals
totals = pd.read_csv("totals.csv")
print("\ninformacion del archivo Estadisticas TOTALES 2021 - 2022:\n")
print(totals.info())
# funcion iloc
# print("\nOBSERVAMOS EL INDICE DE NUESTRO ARCHIVO\n")
# x = totals.iloc[0]
# print(x)

# abrirmos la informacion del archivo de ADVANCED
advanced = pd.read_csv("advanced.csv")
print("\ninformacion del archivo Estadisticas ADVANCED 2021 - 2022:\n")
print(advanced.info())
# funcion iloc
# print("\nOBSERVAMOS EL INDICE DE NUESTRO ARCHIVO\n")
# x2 = advanced.iloc[0]
# print(x2)

# Extraemos el PER
print("\n#Player Eficiency Rate\n")
PER = advanced["PER"]
print(PER)

# Extraemos el PER
print("\n#Player Eficiency Rate\n")
players = advanced["Player"]
print(players)

# print(x)
# x = advanced["Player"].tolist()
# x2 = advanced["PER"].tolist()
# data = {k: v for k, v in zip(x, x2)}
# series = pd.Series(data)
# Imprimimos la lista de los equipo y su presupuesto para contratos
# print("\nESTE ES EL DICCIONARIO DE PER:\n")
# PERDIC = series
# print(PERDIC)
# vista_claves = sorted(PERDIC.items(), key=lambda x: x[1])
# print(vista_claves)

print("Los jugadores con mas per")
# print(advanced["PER"].unique())
advanced = advanced[pd.to_numeric(advanced["PER"], errors="coerce").notnull()]
# Convertir la columna 'PER' en un dtype numérico
advanced["PER"] = advanced["PER"].astype(float)
# Obtener los 10 jugadores con el PER más alto
top_PER = advanced.nlargest(50, "PER")
# Imprimir el resultado
print(top_PER)

# Analizamos los 5 jugador con mejor PER
print("\nAnalizamos a los 5 jugadores con mas per\n")
toper1 = advanced.loc[128]
print("\n", toper1)
toper2 = advanced.loc[190]
print("\n", toper2)
toper3 = advanced.loc[396]
print("\n", toper3)
toper4 = advanced.loc[296]
print("\n", toper4)
toper5 = advanced.loc[405]
print("\n", toper5)
# Extraemos las areas de Interes que estamos dispuestos a analizar
# Filtrar los datos para obtener solo los de Ahmad Caver
Ahmad_caver = totals.loc[totals["Player"] == "Ahmad Caver"]

# Seleccionar las columnas relevantes
Ahmad_caver_stadisticas = Ahmad_caver[
    ["Player", "G", "PTS", "FG%", "3P%", "eFG%", "FT%", "TRB", "AST", "STL", "BLK"]
]

# Filtrar los datos para obtener solo los de Sekou Doumbouya
Sekou_Doumbuya = totals.loc[totals["Player"] == "Sekou Doumbouya"]

# Seleccionar las columnas relevantes
Sekou_Doumbuya_estadisticas = Sekou_Doumbuya[
    ["Player", "G", "PTS", "FG%", "3P%", "eFG%", "FT%", "TRB", "AST", "STL", "BLK"]
]

# Filtrar los datos para obtener solo los de Joe Johnson
Joe_Johnson = totals.loc[totals["Player"] == "Joe Johnson"]

# Seleccionar las columnas relevantes
Joe_Johnson_estadisticas = Joe_Johnson[
    ["Player", "G", "PTS", "FG%", "3P%", "eFG%", "FT%", "TRB", "AST", "STL", "BLK"]
]

# Filtrar los datos para obtener solo los de Jared Harper
Jared_Harper = totals.loc[totals["Player"] == "Jared Harper"]

# Seleccionar las columnas relevantes
Jared_Harper_estadisticas = Jared_Harper[
    ["Player", "G", "PTS", "FG%", "3P%", "eFG%", "FT%", "TRB", "AST", "STL", "BLK"]
]

# Filtrar los datos para obtener solo los de Nikola Jokić
Nikola_Jokic = totals.loc[totals["Player"] == "Nikola Jokić"]

# Seleccionar las columnas relevantes
Nikola_Jokic_estadisticas = Nikola_Jokic[
    ["Player", "G", "PTS", "FG%", "3P%", "eFG%", "FT%", "TRB", "AST", "STL", "BLK"]
]

import matplotlib.pyplot as plt

# Combinar las estadísticas de los jugadores en un solo DataFrame
players = pd.concat(
    [
        Ahmad_caver_stadisticas,
        Sekou_Doumbuya_estadisticas,
        Joe_Johnson_estadisticas,
        Jared_Harper_estadisticas,
        Nikola_Jokic_estadisticas,
    ]
)
print(players.dtypes)

data = players
df = players
df["G"] = pd.to_numeric(df["G"], errors="coerce")
df["PTS"] = pd.to_numeric(df["PTS"], errors="coerce")
df["FG%"] = pd.to_numeric(df["FG%"], errors="coerce")
df["3P%"] = pd.to_numeric(df["3P%"], errors="coerce")
df["eFG%"] = pd.to_numeric(df["eFG%"], errors="coerce")
df["FT%"] = pd.to_numeric(df["FT%"], errors="coerce")
df["TRB"] = pd.to_numeric(df["TRB"], errors="coerce")
df["AST"] = pd.to_numeric(df["AST"], errors="coerce")
df["STL"] = pd.to_numeric(df["STL"], errors="coerce")
df["BLK"] = pd.to_numeric(df["BLK"], errors="coerce")
print(players.dtypes)

# Crear el gráfico de dispersión de PTS vs TRB
# plt.scatter(players['PTS'], players['TRB'])
# for i in range(len(players)):
#    plt.text(players['PTS'].iloc[i], players['TRB'].iloc[i], players['Player'].iloc[i])
# plt.xlabel('Puntos (PTS)')
# plt.ylabel('Rebotes (TRB)')
# plt.title('Comparación de puntos y rebotes de los jugadores')
# plt.show()

players.plot(
    x="Player", y=["G", "FG%", "3P%", "FT%"], kind="bar", title="DIVERDSIDAD DE PUNTAJE"
)
