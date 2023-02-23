#https://www.basketball-reference.com/leagues/NBA_2022_totals.html
#descargando bases de datos en pandas
import pandas as pd

url = input("Dame la pgina de la base de datos: ")
#url = "https://www.basketball-reference.com/leagues/NBA_2022_totals.html"
table = pd.read_html(url)[0]
table.to_csv("new_table.csv", index=False)