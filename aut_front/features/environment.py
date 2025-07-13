import os
import allure
import logging
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from behave.model import Status
from utils.screenshot import salvar_print

def before_all(context):
    """Configuração limpa e funcional"""
    # 1. Configuração para silenciar TUDO
    os.environ['WDM_LOG'] = '0'
    os.environ['WDM_PRINT_FIRST_LINE'] = 'False'

    # 2. Opções do Chrome
    chrome_options = Options()
    chrome_options.add_argument('--log-level=3')
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--no-sandbox')

    # 3. Habilita o modo headless
    chrome_options.add_argument('--headless')  # Ativa o modo headless
    chrome_options.add_argument('--disable-gpu')  # Necessário em CI/CD

    # 4. Configuração do driver (forma moderna)
    service = Service()
    context.driver = webdriver.Chrome(service=service, options=chrome_options)

    # 5. Configuração do logging para mostrar APENAS o necessário
    logging.basicConfig(
        level=logging.INFO,
        format='%(message)s',
        force=True
    )


def after_step(context, step):
    """Screenshots (mantido original)"""
    if hasattr(context, "driver"):
        nome = f"{step.keyword}_{step.name[:50].replace(' ', '_')}"
        caminho = salvar_print(context.driver, nome)
        if os.path.exists(caminho):
            with open(caminho, "rb") as image_file:
                allure.attach(
                    image_file.read(),
                    name=f"{step.keyword}: {step.name}",
                    attachment_type=allure.attachment_type.PNG
                )


def after_all(context):
    """Encerramento"""
    if hasattr(context, "driver"):
        context.driver.quit()
