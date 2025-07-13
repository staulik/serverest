from utils.browser_setup import setup_browser
from behave import given, when, then
from pages.login_page import LoginPage
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
        #logger.info("Página de login carregada com sucesso")
    except Exception as e:
        logger.error(f"Falha ao abrir navegador: {str(e)}")
        raise

@then('os textos, campos e imagem devem estar visíveis')
def step_validar_elementos(context):
    try:
        context.login.validar_elementos_visuais()
       # logger.info("Validação visual concluída com sucesso")
    except Exception as e:
        logger.error(f"Falha na validação visual: {str(e)}")
        context.driver.save_screenshot("erro_elementos.png")
        raise

@when('eu preencho o email "{email}" e senha "{senha}"')
def step_preencher_credenciais(context, email, senha):
    try:
        # Remove aspas extras se existirem
        email = email.strip('"\'') if email.strip('"\'').lower() not in ['""', "''", 'vazio'] else ""
        senha = senha.strip('"\'').strip() if senha.strip('"\'').lower() not in ['""', "''", 'vazio'] else ""

        #logger.info(f"Preenchendo - Email: '{email}' | Senha: '{senha}'")

        if email:
            context.login.preencher_email(email)
        else:
            context.driver.find_element(*LoginPage.input_email).clear()

        if senha:
            context.login.preencher_senha(senha)
        else:
            context.driver.find_element(*LoginPage.input_senha).clear()
    except Exception as e:
        logger.error(f"Falha ao preencher credenciais: {str(e)}")
        raise

@when('clico no botão de login')
def step_clicar_login(context):
    try:
        context.login.clicar_botao_login()
        time.sleep(1)  # Espera reduzida pois agora temos WebDriverWait
        #logger.info("Botão de login clicado")
    except Exception as e:
        logger.error(f"Falha ao clicar no botão: {str(e)}")
        raise

@then('devo ver "{mensagem_erro}"')
def step_verificar_mensagem(context, mensagem_erro):
    try:
        mensagem_erro = mensagem_erro.strip('"\'')
        assert context.login.verificar_mensagem_erro(mensagem_erro), \
            f"Mensagem '{mensagem_erro}' não encontrada!"
        #logger.info(f"Mensagem exibida corretamente: '{mensagem_erro}'")
    except Exception as e:
        logger.error(f"Falha ao verificar mensagem: {str(e)}")
        context.driver.save_screenshot("erro_mensagem.png")
        raise




