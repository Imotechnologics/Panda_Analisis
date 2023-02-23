# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 04:27:35 2023

@author: Imotechnologics
"""
import pandas as pd

# abrirmos la informacion del archivo de ADVANCED
advanced = pd.read_csv("advanced.csv")
print("\ninformacion del archivo Estadisticas ADVANCED 2021 - 2022:\n")
print(advanced.info())

print("\nLos jugadores con mas Juegos Jugados\n")
# print(advanced["G"].unique())
advanced = advanced[pd.to_numeric(advanced["G"], errors="coerce").notnull()]
# Convertir la columna 'G' en un dtype numérico
advanced["G"] = advanced["G"].astype(float)
# Obtener los 50 jugadores con mas Juegos Jugados
more_games = advanced.nlargest(50, "G")
# Imprimir el resultado
print(more_games)


print("\nLos jugadores con mas PER y entr los que tienen mas Juegos Jugados\n")
# print(advanced["G"].unique())
more_games = more_games[pd.to_numeric(advanced["PER"], errors="coerce").notnull()]
# Convertir la columna 'G' en un dtype numérico
more_games["PER"] = more_games["PER"].astype(float)
# Obtener los 50 jugadores con mas Juegos Jugados
more_PER_more_games = more_games.nlargest(10, "PER")
# Imprimir el resultado
print(more_PER_more_games)

import matplotlib.pyplot as plt

# Crear tabla
table = pd.plotting.table(plt.gca(), df, loc="upper center")

# Configurar el tamaño de la tabla y la fuente
table.auto_set_font_size(False)
table.set_fontsize(10)

# Desactivar ejes y ticks
plt.axis("off")

# Configurar tamaño de la figura y la resolución
fig = plt.gcf()
fig.set_size_inches(20, 6)  # ajustar el tamaño de la figura como desees
fig.set_dpi(100)  # ajustar la resolución como desees

# Guardar imagen en archivo
plt.savefig("tabla_DEFENSIVA.png", bbox_inches="tight")

# more_PER_more_games.plot(x='Player', y=['G', 'PER'], kind = 'barh', figsize=(15, 10), title = 'Juegos Jugados vs PER')
