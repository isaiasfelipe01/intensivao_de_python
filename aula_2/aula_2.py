import pandas as pd
import plotly.express as px

# Passo 1: Importar a base de dados
tabela = pd.read_csv(r"C:\Users\isaias\Desktop\intensivao_de_python\aula_2\telecom_users.csv")

# Passo 2: Visualizar a base de dados
tabela = tabela.drop('Unnamed: 0', axis=1)
#print(tabela)

# Passo 3: Tratamento de dados
tabela['TotalGasto'] = pd.to_numeric(tabela['TotalGasto'], errors='coerce')

tabela = tabela.dropna(how='all', axis=1)
tabela = tabela.dropna(how='any', axis=0)
print(tabela.info())

# Passo 4: Análise inicial
print(tabela['Churn'].value_counts())
print(tabela['Churn'].value_counts(normalize=True).map('{:.1%}'.format))

# Passo 5: Análise detalhada - descobrir a causa do cancelamento
grafico = px.histogram(tabela, x='Aposentado', color='Churn')
grafico.show()
