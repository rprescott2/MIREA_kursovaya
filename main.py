import random

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt



df = pd.read_excel("Экспорт_сотрудников_2023_09_26T12_11_08_ЧМ.xlsx")
df = df.iloc[1:, :]
df['5. Дата рождения'] = df['5. Дата рождения'].apply(lambda  row: row if row != 2023 else random.randint(0, 43) + 1960)
by_dates = {"до 30, удалёнка": 0,
            "до 30, офис": 0,
            "30-50, удалёнка": 0,
            "30-50, офис": 0,
            "50+, удалёнка": 0,
            "50+, офис": 0}

g1 = [0, 0, 0]
g2 = [0, 0, 0]

for row in df.to_dict('records'):
    if row['Тип '] == 'удаленка':
        if 2023 - row['5. Дата рождения'] < 30:
            by_dates['до 30, удалёнка'] += 1
            g1[0] += 1
        elif 2023 - row['5. Дата рождения'] < 50:
            by_dates['30-50, удалёнка'] += 1
            g1[1] += 1
        else:
            by_dates['50+, удалёнка'] += 1
            g1[2] += 1
    else:
        if 2023 - row['5. Дата рождения'] < 30:
            by_dates['до 30, офис'] += 1
            g2[0] += 1
        elif 2023 - row['5. Дата рождения'] < 50:
            by_dates['30-50, офис'] += 1
            g2[1] += 1
        else:
            by_dates['50+, офис'] += 1
            g2[2] += 1

print(by_dates)
# width = 0.3
# x = np.arange(3)
# plt.bar(3 - width/2, g1, width=width, label='Удалёнка')
# plt.bar(3 + width/2, g2, width=width, label='Офис')
# # plt.set_xticklabels(["До 30", "30-50", "50+"])
# plt.legend()
# plt.show()
