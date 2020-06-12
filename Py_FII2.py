# -*- coding: utf-8 -*-
"""
Created on Tue May 19 23:51:29 2020

@author: Jefferson Pedro
jeffersonpedro@gmail.com
Coleta dados de todos os FIIs do site FundsExplorer e salva em arquivo csv pronto para trabalhar no panda

"""
import requests
from bs4 import BeautifulSoup
import pandas as pd

# Coletar dados dos FIIs site Funds Explorer

page = requests.get('https://www.fundsexplorer.com.br/ranking')
soup = BeautifulSoup(page.text, 'html.parser')
table = soup.find("table", attrs={"id":"table-ranking"})

# titulo das variaveis
title_data = table.thead.find_all("th")

# dados dos fundos
table_data = table.tbody.find_all("td")

# separando apenas dados, retira as tags
number_rows = int(len(table_data)/len(title_data))

elements_data = [[0]*len(title_data) for i in range(number_rows)]

i = 0
 
for x in range(number_rows):
    for y in range(len(title_data)):
        elements_data[x][y] = table_data[i].getText()
        i +=1

#criando dataframe

title = ['codigo', 'setor', 'preco_atual', 'liquidez_diaria', 'dividendo',
           'dividendyield', 'DY(3M)_acumulado', 'DY(6M)_acumulado', 
           'DY(12M)_acumulado', 'DY(3M)_media', 'DY(6M)_media', 
           'DY(12M)_media', 'DY_ano', 'variacao_preco', 'rent_periodo', 
           'rent_acumulada', 'patri_liq', 'VPA', 'P/VPA', 'DY_patri', 
           'var_patri', 'rent_patri_periodo', 'rent_patri_acumu',
           'vacancia_fisica', 'vancancia_financeira', 'quantidade_ativos']

data = elements_data
df = pd.DataFrame(data)
df.columns = title

for names in title:
    for i in range(len(df['codigo'])):
        if (type(df[names][i]) == str):
            df[names][i] =df[names][i].replace('.','').replace('R$ ','').replace('%','').replace(',','.')

#salvando dataframe
df.to_csv('dados_FIIs_FundsExplorer.csv', index=False, encoding='utf-32')

