# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 07:50:02 2023

@author: sanchez f
"""

import pandas as pd
import matplotlib.pyplot as plt

# abrirmos la informacion del archivo de Totals
totals = pd.read_csv("totals.csv")
print("\ninformacion del archivo Estadisticas TOTALES 2021 - 2022:\n")
print(totals.info())

# Extraemos las areas de Interes que estamos dispuestos a analizar
# Filtrar los datos para obtener solo los de Trae Young
Trae_Young = totals.loc[totals["Player"] == "Trae Young"]

# Seleccionar las columnas relevantes
Trae_Young_stadisticas = Trae_Young[
    ["Player", "G", "PTS", "FG%", "3P%", "eFG%", "FT%", "TRB", "AST", "STL", "BLK"]
]

# Filtrar los datos para obtener solo los de DeMar DeRozan
DeMar_DeRozan = totals.loc[totals["Player"] == "DeMar DeRozan"]

# Seleccionar las columnas relevantes
DeMar_DeRozan_estadisticas = DeMar_DeRozan[
    ["Player", "G", "PTS", "FG%", "3P%", "eFG%", "FT%", "TRB", "AST", "STL", "BLK"]
]

# Filtrar los datos para obtener solo los de Jayson Tatum
Jayson_Tatum = totals.loc[totals["Player"] == "Jayson Tatum"]

# Seleccionar las columnas relevantes
Jayson_Tatum_estadisticas = Jayson_Tatum[
    ["Player", "G", "PTS", "FG%", "3P%", "eFG%", "FT%", "TRB", "AST", "STL", "BLK"]
]

# Filtrar los datos para obtener solo los de LaMelo Ball
LaMelo_Ball = totals.loc[totals["Player"] == "LaMelo Ball"]

# Seleccionar las columnas relevantes
LaMelo_Ball_estadisticas = LaMelo_Ball[
    ["Player", "G", "PTS", "FG%", "3P%", "eFG%", "FT%", "TRB", "AST", "STL", "BLK"]
]

# Filtrar los datos para obtener solo los de Ivica Zubac
Ivica_Zubac = totals.loc[totals["Player"] == "Ivica Zubac"]

# Seleccionar las columnas relevantes
Ivica_Zubac_estadisticas = Ivica_Zubac[
    ["Player", "G", "PTS", "FG%", "3P%", "eFG%", "FT%", "TRB", "AST", "STL", "BLK"]
]
# print("\nInformacion de Archivo Top Ten Top Rate: \n")
# Combinar las estadísticas de los jugadores en un solo DataFrame
players = pd.concat(
    [
        Trae_Young_stadisticas,
        DeMar_DeRozan_estadisticas,
        Jayson_Tatum_estadisticas,
        LaMelo_Ball_estadisticas,
        Ivica_Zubac_estadisticas,
    ]
)
print(players)


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
# players.plot(x='Player', y=['G'], kind = 'bar', title = 'JUEGOS JUGADOS')
# players.plot(x='Player', y=['PTS'], kind = 'bar', title = 'PUNTAJE')
# players.plot(x='Player', y=['FG%', '3P%', 'FT%'], kind = 'bar', title = 'DIVERDSIDAD DE PUNTAJE')
# players.plot(x='Player', y=['TRB', 'AST'], kind = 'bar', title = 'REBOTES CAPTURADOS(TRB)/ASISTENCIAS(AST)')
# players.plot(x='Player', y=['STL', 'BLK'], kind = 'bar', title = 'ROBOS DE BALON(STL)/TAPONES(BLK)')
# Extraemos las areas de Interes que estamos dispuestos a analizar
# Seleccionar las columnas relevantes
Trae_Young_OFENSIVA = Trae_Young[["Player", "G", "TRB", "AST", "STL", "BLK"]]
DeMar_DeRozan_OFENSIVA = DeMar_DeRozan[["Player", "G", "TRB", "AST", "STL", "BLK"]]
Jayson_Tatum_OFENSIVA = Jayson_Tatum[["Player", "G", "TRB", "AST", "STL", "BLK"]]
LaMelo_Ball_OFENSIVA = LaMelo_Ball[["Player", "G", "TRB", "AST", "STL", "BLK"]]
Ivica_Zubac_OFENSIVA = Ivica_Zubac[["Player", "G", "TRB", "AST", "STL", "BLK"]]

print("\nInformacion de Archivo Top Ten Top Rate: \n")
# Combinar las estadísticas de los jugadores en un solo DataFrame
defensiva = pd.concat(
    [
        Trae_Young_OFENSIVA,
        DeMar_DeRozan_OFENSIVA,
        Jayson_Tatum_OFENSIVA,
        LaMelo_Ball_OFENSIVA,
        Ivica_Zubac_OFENSIVA,
    ]
)
print(defensiva)
import matplotlib.pyplot as plt

# Crear tabla
df = defensiva
table = pd.plotting.table(plt.gca(), df, loc="upper center")

# Configurar el tamaño de la tabla y la fuente
table.auto_set_font_size(False)
table.set_fontsize(10)

# Desactivar ejes y ticks
plt.axis("off")

# Configurar tamaño de la figura y la resolución
fig = plt.gcf()
fig.set_size_inches(150, 6)  # ajustar el tamaño de la figura como desees
fig.set_dpi(100)  # ajustar la resolución como desees

# Guardar imagen en archivo
plt.savefig("tabla_DEFENSIVA.png", bbox_inches="tight")

# players.plot(x='Player', y=['TRB', 'AST', 'STL', 'BLK'], kind = 'bar', figsize=(10, 10), title = 'REBOTES CAPTURADOS(TRB)/ASISTENCIAS(AST)/ROBOS DE BALON(STL)/TAPONES(BLK)')
