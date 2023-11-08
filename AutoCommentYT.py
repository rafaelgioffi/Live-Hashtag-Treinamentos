import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

link = 'https://www.youtube.com/watch?v=cckG5KndEiA'
texto = """Salve salve galera! Pra quem tem interesse em automação de tarefas no PC, tenho uma série no canal sobre o assunto com o AutoIT. É fácil de fazer! Dá um pulinho lá.. https://bit.ly/automacaodetarefas"""
tempo = 15
cont = 0

navegador = webdriver.Chrome("chromedriver.exe")
navegador.minimize_window()

navegador.get(link)

while True:
    try:
        navegador.find_element(By.XPATH, '//*[@id="input"]').send_keys(texto)
        navegador.find_element(By.XPATH, '//*[@id="input"]').send_keys('enter')
        if cont <= 1:
            print(f'Comentou {cont} vez...')
        if cont > 1:
            print(f'Comentou {cont} vezes...')
        cont += 1
    except:
        print('Campo não encontrado no site...')

    # finally:
    #     navegador.close()
    #     navegador.quit()

    pyautogui.sleep(tempo)