# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 11:00:17 2023

@author: Imotechnologics
"""
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt

Teams = pd.read_csv("Equipos.csv")
print("\ninformacion del archivo Teams:\n")
print(Teams.info())
# Limpiamos nuestra Base de Datos de Removiendo Entradas de otras Ligas.
Teams = Teams.drop(Teams[Teams["Lg"] == "NBA/BAA"].index)
Teams = Teams.drop(Teams[Teams["Lg"] == "NBA/ABA"].index)
# Teams.plot(x='Franchise', y=['G', 'W', 'L'], kind = 'bar', figsize=(25, 25), title = 'JUEGOS JUGADOS (G)|JUEGOS GANADOS (W)|JUEGOS PERDIDOS (L)')

print("Equipos en mas Play Offs")
Top_10_playoffs = Teams.nlargest(10, "Plyfs")
pd.set_option("display.max_columns", None)
pd.set_option("display.max_rows", None)
data = Top_10_playoffs
df = Top_10_playoffs
df["W/L%"] = pd.to_numeric(df["G"], errors="coerce")
print(Top_10_playoffs.info())

# fig, ax = plt.subplots(figsize=(10, 10))
# for i, v in enumerate(Top_10_playoffs['G']):
#    ax.text(i-0.2, v+50, str(v), fontsize=10)
# Top_10_playoffs.plot(x='Franchise', y=['L'], kind='bar', ax=ax)
# Top_10_playoffs.plot(x='Franchise', y=['Div', 'Conf', 'Champ'], kind = 'bar', figsize=(10, 15), title = 'Ganadores de DIVISION de CONFERENCIA y CAMPEONATOS DE LIGA')
# Top_10_playoffs.plot(x='Franchise', y=['Lg', 'W/L%', 'Lg', 'W/L%','Lg', 'W/L%','Lg', 'W/L%','Lg', 'W/L%','Lg', 'Champ',], kind = 'bar', figsize=(10, 15), title = 'W/L% PORCENTAJE DE VICTORIAS')


# fig, ax = plt.subplots(figsize=(10, 10))

# Top_10_playoffs.plot(x='Franchise', y=['W', 'L'], kind='bar', ax=ax)
# ax.set_title('Juegos Ganados (W) y Juegos Perdidos (L) por Equipo')
# ax.set_xlabel('Equipo')
# ax.set_ylabel('Cantidad')

# Agregar líneas horizontales para el total de W y L
# total_w = Top_10_playoffs['W'].sum()
# total_l = Top_10_playoffs['L'].sum()
# ax.axhline(total_w, color='r', linestyle='--', label=f'Total W = {total_w}')
# ax.axhline(total_l, color='b', linestyle='--', label=f'Total L = {total_l}')

# Agregar texto con los valores correspondientes en cada barra
# fig, ax = plt.subplots(figsize=(10, 8))

# Graficar la tabla Top_10_playoffs
# Top_10_playoffs.plot(x='Franchise', y=['W', 'L'], kind='bar', ax=ax)

# Agregar el valor total de W encima de cada barra
# for i, v in enumerate(Top_10_playoffs['W']):
#    ax.text(i-0.2, v+50, str(v), fontsize=10)

# Agregar el valor total de L encima de cada barra
# for i, v in enumerate(Top_10_playoffs['L']):
#    ax.text(i+0.1, v+50, str(v), fontsize=10)

# Configurar los títulos y etiquetas de los ejes
# ax.set_title('JUEGOS GANADOS Y PERDIDOS', fontsize=14)
# ax.set_xlabel('EQUIPO', fontsize=12)
# ax.set_ylabel('JUEGOS', fontsize=12)

# Mostrar el gráfico
# plt.show()


# Imprimir el resultado
# print(Top_10_playoffs)
# Top_10_playoffs.plot(x='Franchise', y=['W', 'L'], kind = 'bar', figsize=(10, 10), title = '|JUEGOS GANADOS (W)|JUEGOS PERDIDOS (L)')
# Top_10_playoffs.plot(x='Franchise', y=['G'], kind = 'bar', figsize=(10, 10), title = 'JUEGOS JUGADOS')
# Crear tabla
# df = Top_10_playoffs
# table = pd.plotting.table(plt.gca(), df, loc='upper center')

# Configurar el tamaño de la tabla y la fuente
# table.auto_set_font_size(False)
# table.set_fontsize(10)

# Desactivar ejes y ticks
# plt.axis('off')

# Configurar tamaño de la figura y la resolución
# fig = plt.gcf()
# fig.set_size_inches(30, 6)  # ajustar el tamaño de la figura como desees
# fig.set_dpi(100)  # ajustar la resolución como desees

# Guardar imagen en archivo
# plt.savefig('topplayoffs.png', bbox_inches='tight')
