from behave import given, when, then
from pages.login_page import LoginPage
from pages.caduser_page import CadastroPage
from faker import Faker
from selenium.webdriver.support.ui import WebDriverWait
from utils.screenshot import salvar_print  # <- Import da função de print

fake = Faker()

@given("que acessei o login")
def step_abrir_tela_login(context):
    context.login_page = LoginPage(context.driver)
    context.login_page.driver.get(context.login_page.URL)

@when("clico no botão para acessar o cadastro")
def step_ir_para_tela_cadastro(context):
    context.login_page.clicar_botao_ir_cadastro()
    salvar_print(context.driver, "clicou_ir_para_cadastro")

@when("preencho as informações")
def step_preencher_informacoes(context):
    nome = fake.name()
    email = fake.email()
    senha = "admin"

    context.usuario_cadastrado = {
        "nome": nome,
        "email": email,
        "senha": senha
    }

    context.cadastro_page = CadastroPage(context.driver)
    context.cadastro_page.cad_user_adm(nome, email, senha)
    salvar_print(context.driver, "preencheu_infos_cadastro")

@then('devo ver a mensagem "Cadastro realizado com sucesso"')
def step_verificar_mensagem_cadastro(context):
    mensagem = context.cadastro_page.verificar_mensagem_sucesso()
    salvar_print(context.driver, "validou_msg_sucesso")
    assert mensagem is not None, "❌ Nenhuma mensagem de sucesso foi exibida"
    assert "Cadastro realizado com sucesso" in mensagem, f"❌ Mensagem inesperada: '{mensagem}'"

@then("devo ser redirecionado para a área logada")
def step_redirecionado_para_area_logada(context):
    from selenium.webdriver.support.ui import WebDriverWait

    context.url_esperada = "https://front.serverest.dev/admin/home"

    try:
        WebDriverWait(context.driver, 10).until(
            lambda driver: driver.current_url == context.url_esperada
        )

        url_atual = context.driver.current_url

        print(f"\n✅ A correlação está correta:")
        print(f"🔸 URL armazenada: {context.url_esperada}")
        print(f"🔸 URL atual da home: {url_atual}\n")

        assert url_atual == context.url_esperada, \
            f"❌ Redirecionamento incorreto. URL atual: {url_atual}"

    except Exception as e:
        raise AssertionError(f"❌ Não foi redirecionado corretamente: {str(e)}")
    finally:
        salvar_print(context.driver, "redirecionado_area_logada")

@then("posso ver meu usuario logado")
def step_validar_usuario_logado(context):
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC

    nome_esperado = context.usuario_cadastrado["nome"].strip()
    print(f"🕵️‍♂️ Aguardando nome do usuário na tela: {nome_esperado}")

    try:
        elemento = WebDriverWait(context.driver, 10).until(
            EC.presence_of_element_located((
                By.XPATH,
                f"//h1[starts-with(normalize-space(.), 'Bem Vindo')]"
            ))
        )
        texto_completo = elemento.text.strip()
        nome_exibido = texto_completo.replace("Bem Vindo", "").strip()

        print(f"✅ Usuário gerado: {nome_esperado}")
        print(f"✅ Nome exibido na tela: {nome_exibido}")
        assert nome_esperado.lower() == nome_exibido.lower(), \
            f"❌ Nome do usuário logado não confere: esperado '{nome_esperado}', exibido '{nome_exibido}'"
    except Exception as e:
        raise AssertionError(f"❌ Erro ao validar o usuário logado: {str(e)}")
    finally:
        salvar_print(context.driver, "usuario_logado")
