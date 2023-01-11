import pandas as pd

# Passo 1: Importar a base de dados
tabela = pd.read_csv(r"C:\Users\isaias\Desktop\intensivao_de_python\aula_2\telecom_users.csv")

# Passo 2: Visualizar a base de dados
tabela = tabela.drop('Unnamed: 0', axis=1)
#print(tabela)

# Passo 3: Tratamento de dados
tabela['TotalGasto'] = pd.to_numeric(tabela['TotalGasto'], errors='coerce')
print(tabela.info())