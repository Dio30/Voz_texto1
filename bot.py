from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
import smtplib
from datetime import datetime
import email.message

fuso_horario = datetime.now()

# site 1
chrome_options = Options()
chrome_options.add_argument("--headless")  # Executar em modo headless
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument("--window-size=1500x3200")

service = Service()

driver = webdriver.Chrome(service=service, options=chrome_options)

def take_screenshot(driver, url, file_name, sleep):
    driver.get(url)
    time.sleep(sleep)
    driver.save_screenshot(file_name)
    driver.quit()
    print(f'Captura de tela no site {url} no arquivo {file_name} salva com sucesso!')

# site 2
chrome_options1 = Options()
chrome_options1.add_argument("--headless")  # Executar em modo headless
chrome_options1.add_argument('--disable-dev-shm-usage')
chrome_options1.add_argument("--no-sandbox")
chrome_options1.add_argument("--window-size=1500x3300")

service1 = Service()
driver1 = webdriver.Chrome(service=service1, options=chrome_options1)

def take_screenshot1(driver, url, file_name, sleep):
    driver.get(url)
    time.sleep(sleep)
    driver.save_screenshot(file_name)
    driver.quit()
    print(f'Captura de tela no site {url} no arquivo {file_name} salva com sucesso!')

def multi_paginas_screen():
    take_screenshot(driver=driver, url='https://visao-geral-picking-putaway-brsc02.streamlit.app/', file_name='picking-putaway.png', sleep=30)
    take_screenshot1(driver=driver1, url='https://gestao-brsc02.streamlit.app/gerencial', file_name='gerencial.png', sleep=20)

def enviar_email():
    multi_paginas_screen()
    
    corpo_email = f"""
    <p>Bom dia, tudo bem?</p>
    <p>Seguem em anexo um print diário feito às {fuso_horario.strftime('%H:%M:%S')}, mostrando como estão os indicadores no HeatMap e em Movimentações no Picking e Putaway</p>
    <p>Qualquer dúvida, estou à disposição!</p>
    """
    
    msg = email.message.EmailMessage()
    msg['Subject'] = f"Captura de Tela do dia {datetime.now().strftime('%d/%m/%Y')}"
    msg['From'] = 'dione.padilha@mercadolivre.com'
    msg['To'] = 'dione.padilha@mercadolivre.com'
    password = 'xcim euun ygad qjef'
    msg.add_header('Content-Type', 'text/html')
    msg.set_content(corpo_email, subtype='html')

    # Anexar imagem 1
    with open('picking-putaway.png', 'rb') as f:
        img_data = f.read()
    msg.add_attachment(img_data, maintype='image', subtype='png', filename='picking-putaway.png')

    # Anexar imagem 2
    with open('gerencial.png', 'rb') as f:
        img_data = f.read()
    msg.add_attachment(img_data, maintype='image', subtype='png', filename='gerencial.png')

    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(msg['From'], password)
        server.send_message(msg)
        print('Email enviado')

enviar_email()