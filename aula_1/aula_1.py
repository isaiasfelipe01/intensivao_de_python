# passo 1: Entrar no sistema da empresa
import pyautogui
import pyperclip
from time import sleep

pyautogui.PAUSE = 1
pyautogui.press('win')
pyautogui.write("firefox")
pyautogui.press('enter')
pyperclip.copy('https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga')
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('enter')


# passo 2: Navegar até o local do relatório
sleep(8)
pyautogui.click(x=522, y=381, clicks = 2)
# passo 3: Exportar o relatório 
# passo 4: Calcular os indicadores
# passo 5: Enviar um e-mail para a diretoria