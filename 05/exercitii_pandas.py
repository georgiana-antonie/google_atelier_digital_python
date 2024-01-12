import pandas as pd
import numpy as np

# dintr-o lista
# lista = [10, 20, 30, 40, 50]
# etichete = ['a', 'b', 'c', 'd', 'e']
# serie = pd.Series(lista, index=etichete)
# print(serie[['a', 'c', 'd']])

# dintr-un array numpy
# array_date = np.array([10, 20, 30, 40, 50])
# serie = pd.Series(array_date)
# print(serie)

# dintr-un dictionar
# dict_date = {'a': 10, 'b': 20, 'c': 30, 'd': 40, 'e': 50}
# serie = pd.Series(dict_date)
# print(serie)

data = {'Nume': ['Ana', 'Bogdan', 'Cristina' , 'Bogdan'],
        'Varsta': [25, 30, 22, 32],
        'Salariu': [50000, 60000, 45000, 23000]}
df = pd.DataFrame(data)
df['Experienta'] = [2, 5, 1, 3]
# print(df)
# df.set_index('Nume', inplace=True)
# print(df)
# print(df.loc['Bogdan'])
df.to_csv('nou.csv')
