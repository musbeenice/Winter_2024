# Вторая задача к двадцатому занятию

import pandas as pd


def total_num(df):
    total = 0
    for i in df.index:
        for j in df.columns:
            if isinstance(df.loc[i, j], (int, float)):
                total += df.loc[i, j]
    print(format(total, ".2f"))


some_df = pd.DataFrame({
    "position": ["sofa", "wardrobe", "lamp"],
    "i_n": ["272490", "171251", "207600"],
    "price": [74.99, 34.99, 9.99]
})
total_num(some_df)
