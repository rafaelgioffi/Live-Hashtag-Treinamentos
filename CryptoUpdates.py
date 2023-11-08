from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import pandas as pd

local = "E:\\OneDrive\\RGSW Corp\\"

# Opções para não exibir o navegador...
chrome_options = Options()
chrome_options.add_argument("--headless")

navegador = webdriver.Chrome(executable_path=r'C:\Users\Rafael\chromedriver.exe', chrome_options=chrome_options)

navegador.get("https://coinmarketcap.com/pt-br/currencies/bombcrypto/")
bcoin = navegador.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/div[2]/div/div[3]/div/div[1]/div[2]/div[3]/div/div/div/div/div[2]/div[2]/input').get_attribute('value')
print(f'Valor do BCOIN ==> R${bcoin}')

navegador.get('https://coinmarketcap.com/currencies/cryptocars/')
ccar = navegador.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/div[2]/div/div[3]/div/div[1]/div[2]/div[3]/div/div/div/div/div[2]/div[2]/input').get_attribute('value')
print(f'Valor do CCAR ==> R${ccar}')

navegador.get('https://coinmarketcap.com/pt-br/currencies/step-hero/')
step = navegador.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/div[2]/div/div[3]/div/div[1]/div[2]/div[3]/div/div/div/div/div[2]/div[2]/input').get_attribute('value')
print(f'Valor do STEP HERO ==> R${step}')

bomb = 'PLANILHA BOMB CRYPTO 2022.xlsm'
ccar = 'PLANILHA CCAR 2022.xlsm'
print(bomb)

tabela = pd.read_excel(bomb)
tabela.loc[13, 5] = bcoin

navegador.quit()
navegador.close()