import pyautogui, pyperclip, time, pandas
import pygetwindow
from IPython import display

pyautogui.PAUSE = 1  # espera 1 segundo entre cada ação...

# usar o teclado
pyautogui.hotkey("win", "r")
pyautogui.write("chrome")
pyautogui.press("enter")
pyautogui.press("tab")
pyautogui.press("enter")

# pyautogui.hotkey("ctrl", "t")
# pyperclip usa os caracteres especiais...
pyperclip.copy("https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga")
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")

pyautogui.sleep(5)

# clica 2x na pasta Exportar
pyautogui.click(x=312, y=297, clicks=2)

pyautogui.sleep(2)
# clica no arquivo "vendas - Dez"
pyautogui.click(x=371, y=383)

pyautogui.sleep(1)
# clica nos 3 pontinhos...
pyautogui.click(x=1725, y=190)

# clica em "Download"
pyautogui.sleep(1)
pyautogui.click(x=1516, y=620)

pyautogui.sleep(3)
pyperclip.copy(r"C:\Users\Rafael\AppData\Local\Temp\Vendas - Dez.xlsx")
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")

pyautogui.sleep(2)

existe = pyautogui.getActiveWindowTitle()
print(existe)
if existe == 'Confirmar Salvar como':
    print('Caiu no existe...')
    pyautogui.sleep(1)
    pyautogui.press("s")
    pyautogui.sleep(3)
    pyautogui.click(x=1371, y=383)

tabela = pandas.read_excel(r"C:\Users\Rafael\AppData\Local\Temp\Vendas - Dez.xlsx")
# display.display(tabela)

# selecionar uma coluna inteira
faturamento = tabela['Valor Final'].sum()
qtd_prod = tabela['Quantidade'].sum()

# print(faturamento,' - ',qtd_prod)

# Enviar email...
pyautogui.hotkey('ctrl', 't')
pyperclip.copy('https://mail.google.com/mail/u/0/#inbox')
pyautogui.hotkey('ctrl', 'v')
pyautogui.press("enter")
pyautogui.sleep(5)

#clicar em Nova mensagem
pyautogui.click(x=90, y=216)
# pyautogui.sleep(1)
pyautogui.click(x=1304, y=425)
# pyautogui.sleep(1)
pyautogui.write('teste@teste.com')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.write(r'Relatório de Vendas')
pyautogui.press('tab')

# Corpo do E-mail
texto = f"""
Prezados, bom dia
O faturamento de ontem foi de R$: {faturamento:,.2f}
A quantidade de produtos foi de: {qtd_prod:,.0f}


Atenciosamente,
Lira Python
"""

pyperclip.copy(texto)
pyautogui.hotkey('ctrl', 'v')

# Clicar em anexar arquivo...
pyautogui.click(1421, 946)
pyperclip.copy(r"C:\Users\Rafael\AppData\Local\Temp\Vendas - Dez.xlsx")
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")
pyautogui.sleep(10)

# Enviar o e-mail...
pyautogui.hotkey('ctrl', 'enter')

pyautogui.sleep(2)

# print(pyautogui.position())
pyautogui.hotkey("alt", "f4")
# pyautogui.hotkey("alt", "tab")
