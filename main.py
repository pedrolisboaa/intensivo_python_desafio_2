import pandas as pd
import plotly.express as px

"""1 - Importação da base de dados."""
base_de_dados = pd.read_csv('telecom_users.csv')

"""2 - Veisualização da base de dados
    Lembra o tado que não serve para nada, te atrapalha
"""
# axis -> 0 = linha; axis -> 1 = coluna
base_de_dados = base_de_dados.drop('Unnamed: 0', axis=1)

""" 
    3 - Tratando os dados
    Resolver que estao reconhecido de forma errada
    resolver os valores vazios
"""
base_de_dados['TotalGasto'] = pd.to_numeric(
    base_de_dados['TotalGasto'], errors='coerce')
# print(base_de_dados.info())


# Excluíndos colunas com valores vázios
base_de_dados = base_de_dados.dropna(how="all", axis=1)
# Linhas que possui pelo um valor vazio
base_de_dados = base_de_dados.dropna(how="any", axis=0)


""" 
    4 - Analise de dados
"""
print(base_de_dados["Churn"].value_counts())
# Sem formatar
# print(base_de_dados['Churn'].value_counts(normalize=True))
# Formattado
print(base_de_dados['Churn'].value_counts(normalize=True).map("{:.2%}".format))


""" 
    5 - Análise detalhada - descobrir as causa do cancelamento
    # comparar cada coluna da base de dados com a coluna Chrun
"""

# criar o gráfic
# para cada coluna da minha tabela criar uma gráfico

for coluna in base_de_dados.columns:
    grafico = px.histogram(base_de_dados, x=coluna, color='Churn', text_auto=True)
    grafico.show()
    
# Exibir o grafico


