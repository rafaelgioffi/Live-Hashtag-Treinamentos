import displayfunction
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd

# Abrir o Chrome...
# para o opera seria webdriver.Opera() e assim por diante...
print('Atualizando as cotações na internet...')
navegador = webdriver.Chrome(r"C:\Users\Rafael\chromedriver.exe")
navegador.minimize_window()

# Abrir um site...
navegador.get("https://www.google.com.br")

# Achar um elemento e focar no campo de busca e digitar o que buscar
# Para achar o elemento, basta inspecionar o elemento, selecionar, clicar com o botão direito no elemento encontrado, copiar e copiar o XPATH
navegador.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div[2]/div[2]/input').send_keys('cotação dólar')

# Clica no 'Pesquisa Google'
navegador.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[1]').click()

# navegador.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div[2]/div[2]/input').send_keys(
#     Keys.ENTER)

# Pega o valor do campo "data-value"
dolar = navegador.find_element(By.XPATH, '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')
dolar = float(dolar.replace(',', '.'))
print(f'Dólar atualizado! R${dolar:.2f}')

navegador.get("https://www.google.com.br")
navegador.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div[2]/div[2]/input').send_keys('cotação euro')
navegador.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[1]').click()
euro = navegador.find_element(By.XPATH, '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')
euro = float(euro.replace(',', '.'))
print(f'Euro atualizado! R${euro:.2f}')

navegador.get("https://www.melhorcambio.com/ouro-hoje")
ouro = navegador.find_element(By.XPATH, '//*[@id="comercial"]').get_attribute('value')
ouro = float(ouro.replace(',', '.'))
print(f'Ouro atualizado! R${ouro:.2f}')


navegador.get("https://www.google.com.br")
navegador.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div[2]/div[2]/input').send_keys('cotação bitcoin')
navegador.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[1]').click()
btc = navegador.find_element(By.XPATH,'//*[@id="crypto-updatable_2"]/div/div[5]/div[2]/input').get_attribute('value')
btc = float(btc)
print(f'Bitcoin atualizado! R${btc:.2f}')


navegador.get("https://www.google.com.br")
navegador.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div[2]/div[2]/input').send_keys('cotação ethereum')
navegador.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[1]').click()
eth = navegador.find_element(By.XPATH, '//*[@id="crypto-updatable_2"]/div/div[5]/div[2]/input').get_attribute('value')
eth = float(eth)
print(f'Ethereum atualizado! R${eth:.2f}')

# Atualiza na planilha...
tabela = pd.read_excel('Produtos.xlsx')
# print(tabela)
# Localiza a coluna Moeda pelo valor (dolar, euro e etc) e altera o valor de forma dinâmica
tabela.loc[tabela['Moeda'] == 'Dólar', 'Cotação'] = dolar
tabela.loc[tabela['Moeda'] == 'Euro', 'Cotação'] = euro
tabela.loc[tabela['Moeda'] == 'Ouro', 'Cotação'] = ouro

tabela.loc[13, 5] = dolar

print('Cotação atualizada na planilha...')

# Calcula o novo preço de compra...
tabela['Preço de Compra'] = tabela['Preço Original'] * tabela['Cotação']

# Calcula a nova margem...
tabela['Preço de Venda'] = tabela['Preço de Compra'] * tabela['Margem']

print(tabela)

# Exportar tudo para uma nova planilha...
tabela.to_excel('Produtos.xlsx', index=False)
print('Base de dados atualizada!')

# fecha o navegador...
navegador.quit()
navegador.close()
