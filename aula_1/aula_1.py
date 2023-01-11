import pyautogui
import pyperclip
from time import sleep

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
pyautogui.click(x=508, y=350, clicks = 2)
sleep(3)
# passo 3: Exportar o relatório 
pyautogui.click(x=500, y=447)
pyautogui.click(x=1673, y=210)
# passo 4: Calcular os indicadores
# passo 5: Enviar um e-mail para a diretoria