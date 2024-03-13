# Вторая задача к двадцать третьему занятию

import psycopg2
import pandas as pd

con = psycopg2.connect(
    database="postgres",
    user="postgres",
    password="",
    host="127.0.0.1",
    port="5433"
)

cur = con.cursor()
cur.execute('''SELECT *
FROM book
ORDER BY book_id''')

rows = cur.fetchall()

df = pd.DataFrame(columns=["book_id", "title", "author", "price", "amount", "total", "author_id"],
                  index=range(1, len(rows[0]) + 1))
x = 1
for row in rows:
    df.loc[x] = row
    x += 1

print(df)

con.close()
