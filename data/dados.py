import pandas as pd
import locale
from flask import request,render_template

locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')


# Por enquanto irei deixar assim, depois só a função irá retornar o DataFrame.
data = pd.read_csv("data/dados_assaltos_ficticios_simples.csv")

data['Data'] = pd.to_datetime(data['Data'])
data['Data_por_extenso'] = data['Data'].dt.strftime('%d de %B de %Y')
data['Ano'] = data['Data'].dt.year

def csv_to_dataframe():
    data = pd.read_csv("data/dados_assaltos_ficticios_simples.csv")
    data['Data'] = pd.to_datetime(data['Data'])
    data['Data_por_extenso'] = data['Data'].dt.strftime('%d de %B de %Y')
    data['Ano'] = data['Data'].dt.year    
    return data

# Funções para estatísticas.
def porcentagem_bairros():
    porcentagem_bairros = data['Bairro'].value_counts(normalize=True) * 100
    return porcentagem_bairros.round(2)

def data_com_mais_assaltos():
    dias_com_mais_assaltos = data['Data_por_extenso'].value_counts().to_dict()
    dicionario_fatiado = {chave: valor for chave, valor in dias_com_mais_assaltos.items() if valor > 2}
    return dicionario_fatiado

def carregar_dados_por_ano(ano):
    data = csv_to_dataframe()
    dados_filtrados = data[data['Ano'] == ano]
    # Transformar em uma lista de dicionários
    return dados_filtrados[['Latitude', 'Longitude', 'Ano']].to_dict(orient='records')

def data_adicionar_assalto(barrio,latitude,longitude,data_extenso):
    dados = {'Bairro': [barrio], 'Latitude': [latitude], 'Longitude': [longitude], 'Data_por_extenso': [data_extenso]}
    with open('data/dados_assaltos_ficticios_simples.csv', 'a') as arquivo_csv:
        arquivo_csv.write(dados['Data_por_extenso'][0] + ',' + dados['Bairro'][0] + ',Assalto,' + dados['Latitude'][0] + ',' + dados['Longitude'][0] + '\n')
    
    data = pd.read_csv("data/dados_assaltos_ficticios_simples.csv")

    data['Data'] = pd.to_datetime(data['Data'])
    data['Data_por_extenso'] = data['Data'].dt.strftime('%d de %B de %Y')
    data['Ano'] = data['Data'].dt.year
    