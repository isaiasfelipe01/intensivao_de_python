from selenium import webdriver
from selenium.webdriver.common.keys import Keys

navegador = webdriver.Firefox()

# passo 1: Pegar a cotação do dolar

navegador.get('https://www.google.com')
navegador.find_element('xpath', '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys('cotação dólar')
navegador.find_element('xpath', '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)
cotacao_dolar = navegador.find_element('xpath', '/html/body/div[7]/div/div[10]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div/div/div[3]/div[1]/div[1]/div[2]/span[1]').get_attribute('data-value')
print(cotacao_dolar)
