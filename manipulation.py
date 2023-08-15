import pandas as pd
import sqlite3

con = sqlite3.connect('banco.db')

q = pd.read_sql('SELECT * FROM prod', con, index_col='id')
df = pd.DataFrame(q, columns=['name', 'preco', 'description'])
print(df.sort_values('preco'))
# print(df)