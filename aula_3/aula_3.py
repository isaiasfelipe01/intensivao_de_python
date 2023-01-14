from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import pandas as pd

navegador = webdriver.Firefox()

# passo 1: Pegar a cotação do dolar

navegador.get('https://www.google.com')
navegador.find_element('xpath', '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys('cotação dólar')
navegador.find_element('xpath', '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)
sleep(5)
cotacao_dolar = navegador.find_element('xpath', '/html/body/div[7]/div/div[10]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div/div/div[3]/div[1]/div[1]/div[2]/span[1]').get_attribute('data-value')
print(cotacao_dolar)

# Passo 2: Cotação do euro

navegador.get('https://www.google.com')
navegador.find_element('xpath', '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys('cotação euro')
navegador.find_element('xpath', '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)
sleep(5)
cotacao_euro = navegador.find_element('xpath', '/html/body/div[7]/div/div[10]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div/div/div[3]/div[1]/div[1]/div[2]/span[1]').get_attribute('data-value')
print(cotacao_euro)

# Passo 3: Pegar a cotação do ouro

navegador.get('https://www.melhorcambio.com/ouro-hoje')
sleep(5)
cotacao_ouro = navegador.find_element('xpath', '//*[@id="comercial"]').get_attribute('value')
cotacao_ouro = cotacao_ouro.replace(',', '.')
print(cotacao_ouro)

# Passo 4: Importar a base de dados

tabela = pd.read_excel(r'C:\Users\isaias\Desktop\intensivao_de_python\aula_3\Produtos.xlsx')
print(tabela)

# Passo 5: Recalcular os preços


navegador.quit()