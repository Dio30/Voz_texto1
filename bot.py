from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

# site 1
chrome_options = Options()
chrome_options.add_argument("--headless")  # Executar em modo headless
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--window-size=1500x3200")

service = Service(ChromeDriverManager().install())

driver = webdriver.Chrome(service=service, options=chrome_options)

def take_screenshot(driver, url, file_name, sleep):
    driver.get(url)
    time.sleep(sleep)
    driver.save_screenshot(file_name)
    driver.quit()
    print(f'Captura de tela no site {url} no arquivo {file_name} com sucesso!')

# site 2
chrome_options1 = Options()
chrome_options1.add_argument("--headless")  # Executar em modo headless
chrome_options1.add_argument("--disable-gpu")
chrome_options1.add_argument("--window-size=1500x3300")

service1 = Service(ChromeDriverManager().install())
driver1 = webdriver.Chrome(service=service1, options=chrome_options1)

def take_screenshot1(driver, url, file_name, sleep):
    driver.get(url)
    time.sleep(sleep)
    driver.save_screenshot(file_name)
    driver.quit()
    print(f'Captura de tela no site {url} no arquivo {file_name} com sucesso!')

def multi_paginas_screen():
    take_screenshot(driver=driver, url='https://visao-geral-picking-putaway-brsc02.streamlit.app/', file_name='picking-putaway.png', sleep=20)
    take_screenshot1(driver=driver1, url='https://gestao-brsc02.streamlit.app/gerencial', file_name='gerencial.png', sleep=20)

multi_paginas_screen()