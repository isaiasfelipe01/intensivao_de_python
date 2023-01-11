import pyautogui
import pyperclip
from time import sleep
import pandas as pd


# passo 1: Entrar no sistema da empresa

pyautogui.PAUSE = 1
pyautogui.press('win')
pyautogui.write("firefox")
pyautogui.press('enter')
pyautogui.click(x=1685, y=95) # maximizando a nova aba
sleep(2)
pyperclip.copy('https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga')
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('enter')


# passo 2: Navegar até o local do relatório

sleep(4)
pyautogui.click(x=508, y=350, clicks = 2) # abrindo o aquivo para dowload
sleep(3)


# passo 3: Exportar o relatório 

pyautogui.click(x=500, y=447) # selecionando o arquivo
pyautogui.click(x=1673, y=210) # preparando para dowload
pyautogui.click(x=1460, y=719) # baixando o arquivo
sleep(5)
pyautogui.click(x=766, y=562) # selecionando a pasta
sleep(10)


# passo 4: Calcular os indicadores

tabela = pd.read_excel(r"C:\Users\isaias\Downloads\Vendas - Dez.xlsx")
print(tabela) # trazendo a base de dados

faturamento = tabela['Valor Final'].sum()
quantidade = tabela['Quantidade'].sum()
print(faturamento)
print(quantidade)


# passo 5: Enviar um e-mail para a diretoria
sleep(3)
pyautogui.hotkey('ctrl', 't')
pyperclip.copy('https://mail.google.com/mail/u/0/#inbox')
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('enter')
sleep(5)
pyautogui.click(x=94, y=219) # escrevendo e-mail

pyautogui.write('boxwater272@gmail.com')
pyautogui.press('tab')
pyautogui.press('tab')

pyperclip.copy('Relatório de vendas')
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('tab')

texto = f'''
Prezados, bom dia

O faturamento de ontem foi: {faturamento:.2f}
A quantidade de de produtos foi: {quantidade}

Abraços
'''
pyperclip.copy(texto)
pyautogui.hotkey('ctrl', 'v')

pyautogui.hotkey('ctrl', 'enter')
