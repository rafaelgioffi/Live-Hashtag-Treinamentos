import webbrowser

import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

navegador = webdriver.Chrome()
try:
    navegador.get('https://click.petrobras.com.br')
    pyautogui.sleep(5)
    navegador.find_element(By.XPATH, '//*[@id="userNameInput"]').send_keys('r.gioffi')
    navegador.find_element(By.XPATH, '//*[@id="kmsiInput"]').click()
    navegador.find_element(By.XPATH, '//*[@id="nextButton"]').click()
except ValueError:
    print('Erro...', ValueError)

valor = input('[S]air? ')
if valor == 's' or valor == 'S':
    navegador.close()
else:
    pass