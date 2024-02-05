import requests
from bs4 import BeautifulSoup
import pandas as pd

dictionar = {'Nr. crt.': [],
            'Judet': []}

for i in range(10, 15):
    r = requests.get(f'https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-{str(i)}-decembrie-ora-13-00-2/')
    link = BeautifulSoup(r.text, 'html.parser')

    title = link.find_all('div', attrs={'class': 'entry-content'})
    for tr_index in title[0].find_all('table', limit=1):
        for tr in tr_index.find_all('tr'):
            for td_index in tr.find_all('td', limit=3):
                print(td_index)
                if td_index < 43:
                    dictionar['Nr. crt.'].append(td_index + 1)
                    row_value_split = td_value.split(' ')
                    number = row_value_split[-2]
                    del row_value_split[0]
                    del row_value_split[-3:]
                    judet = str(row_value_split[0])
                    dictionar['Judet'].append(judet)
                    dictionar[f'1{str(i)}.12.2021'].append(number)
                if row_index == 43:
                    dictionar['Nr. crt.'].append(44)
                    dictionar['Judet'].append('judet')
                    row_value_split = row_value.split(' ')
                    dictionar[f'1{str(i)}.12.2021'].append(row_value_split[-3])
                if row_index == 44:
                    dictionar['Nr. crt.'].append(45)
                    dictionar['Judet'].append('TOTAL')
                    row_value_split = row_value.split(' ')
                    dictionar[f'1{str(i)}.12.2021'].append(row_value_split[-3])

df = pd.DataFrame(dictionar)
print(df)
df.to_csv('covid.csv')