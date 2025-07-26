from utils.browser_setup import setup_browser
from behave import given, when, then
from pages.login_page import LoginPage
from utils.screenshot import salvar_print  # certifique-se de importar corretamente
import logging
import time

logging.basicConfig(level=logging.CRITICAL)
logger = logging.getLogger(__name__)

@given('que estou na tela de login')
def step_abrir_login(context):
    try:
        context.driver = setup_browser()
        context.driver.get("https://front.serverest.dev/login")
        context.driver.maximize_window()
        context.login = LoginPage(context.driver)
        salvar_print(context.driver, "01_tela_login")
    except Exception as e:
        logger.error(f"Falha ao abrir navegador: {str(e)}")
        raise

@then('os textos, campos e imagem devem estar visíveis')
def step_validar_elementos(context):
    try:
        context.login.validar_elementos_visuais()
        salvar_print(context.driver, "02_elementos_visiveis")
    except Exception as e:
        logger.error(f"Falha na validação visual: {str(e)}")
        context.driver.save_screenshot("erro_elementos.png")
        raise

@when('eu preencho o email "{email}" e senha "{senha}"')
def step_preencher_credenciais(context, email, senha):
    try:
        email = email.strip('"\'') if email.strip('"\'').lower() not in ['""', "''", 'vazio'] else ""
        senha = senha.strip('"\'').strip() if senha.strip('"\'').lower() not in ['""', "''", 'vazio'] else ""

        if email:
            context.login.preencher_email(email)
        else:
            context.driver.find_element(*LoginPage.input_email).clear()

        if senha:
            context.login.preencher_senha(senha)
        else:
            context.driver.find_element(*LoginPage.input_senha).clear()

        salvar_print(context.driver, "03_credenciais_preenchidas")
    except Exception as e:
        logger.error(f"Falha ao preencher credenciais: {str(e)}")
        raise

@when('clico no botão de login')
def step_clicar_login(context):
    try:
        context.login.clicar_botao_login()
        time.sleep(1)
        salvar_print(context.driver, "04_botao_login_clicado")
    except Exception as e:
        logger.error(f"Falha ao clicar no botão: {str(e)}")
        raise

@then('devo ver "{mensagem_erro}"')
def step_verificar_mensagem(context, mensagem_erro):
    try:
        mensagem_erro = mensagem_erro.strip('"\'')
        assert context.login.verificar_mensagem_erro(mensagem_erro), \
            f"Mensagem '{mensagem_erro}' não encontrada!"
        salvar_print(context.driver, "05_mensagem_erro_exibida")
    except Exception as e:
        logger.error(f"Falha ao verificar mensagem: {str(e)}")
        context.driver.save_screenshot("erro_mensagem.png")
        raise





