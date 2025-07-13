from utils.highlighter import highlight_element
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    URL = "https://front.serverest.dev/login"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # Locators
    input_email = (By.CSS_SELECTOR, "[data-testid='email']")
    input_senha = (By.CSS_SELECTOR, "[data-testid='senha']")
    btn_entrar = (By.CSS_SELECTOR, "[data-testid='entrar']")
    btn_ir_para_cadastro = (By.CSS_SELECTOR, '[data-testid="cadastrar"]')
    txt_login = (By.CSS_SELECTOR, "h1.font-robot")
    txt_nao_cadastrado = (By.CSS_SELECTOR, "small.message.form-text")
    img_logo = (By.CSS_SELECTOR, "img.imagem")
    msg_email_obrigatorio = (By.CSS_SELECTOR, "div.alert:nth-of-type(1) span")
    msg_senha_obrigatorio = (By.CSS_SELECTOR, "div.alert:nth-of-type(2) span")

    def validar_elementos_visuais(self):
        secoes = {
            "Campos de input": {
                "Input Email": self.input_email,
                "Input Senha": self.input_senha
            },
            "Botões": {
                "Botão Entrar": self.btn_entrar
            },
            "Textos": {
                "Título Login": self.txt_login,
                "Texto 'Não é cadastrado?'": self.txt_nao_cadastrado
            },
            "Imagem": {
                "Logo": self.img_logo
            }
        }

        for titulo_secao, elementos in secoes.items():
            for nome, locator in elementos.items():
                try:
                    el = self.wait.until(EC.presence_of_element_located(locator))
                    highlight_element(self.driver, el)
                    assert el.is_displayed(), f"{nome} não está visível"
                    if "Input" in nome or "Botão" in nome:
                        assert el.is_enabled(), f"{nome} não está habilitado"
                except Exception as e:
                    raise AssertionError(f"❌ Falha ao validar {nome}: {str(e)}")

    def preencher_email(self, email):
        campo = self.wait.until(EC.element_to_be_clickable(self.input_email))
        campo.clear()
        campo.send_keys(email)

    def preencher_senha(self, senha):
        campo = self.wait.until(EC.element_to_be_clickable(self.input_senha))
        campo.clear()
        campo.send_keys(senha)

    def clicar_botao_login(self):
        botao = self.wait.until(EC.element_to_be_clickable(self.btn_entrar))
        botao.click()

    def clicar_botao_ir_cadastro(self):
        botao = self.wait.until(EC.element_to_be_clickable(self.btn_ir_para_cadastro))
        botao.click()

        # Espera a tela de cadastro carregar (pelo campo de nome, por exemplo)
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.ID, "nome"))
        )

    def verificar_mensagem_erro(self, mensagem):
        try:
            mensagem = mensagem.lower().strip('"\'')
            mensagens_visiveis = []
            elementos = self.wait.until(
                EC.presence_of_all_elements_located(
                    (By.XPATH, "//div[contains(@class,'alert')]//span")
                )
            )
            mensagens_visiveis = [
                el.text.lower() for el in elementos if el.is_displayed()
            ]
            if ", " in mensagem:
                partes = [p.strip() for p in mensagem.split(",")]
                return all(
                    any(p in msg for msg in mensagens_visiveis) for p in partes
                )
            return any(mensagem in msg for msg in mensagens_visiveis)
        except Exception:
            self.driver.save_screenshot("erro_validacao_mensagem.png")
            return False



