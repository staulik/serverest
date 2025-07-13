from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class CadastroPage:
    URL = "https://front.serverest.dev/cadastrar"

    txt_nome = (By.ID, "nome")
    txt_email = (By.ID, "email")
    txt_senha = (By.ID, "password")
    chk_administrador = (By.ID, "administrador")
    btn_cadastrar = (By.CSS_SELECTOR, '[data-testid="cadastrar"]')
    msg_caduser_ok = (By.CSS_SELECTOR, "div.alert a.alert-link")  # 🎯

    def __init__(self, driver):
        self.driver = driver

    def preencher_nome(self, nome):
        self.driver.find_element(*self.txt_nome).send_keys(nome)

    def preencher_email(self, email):
        self.driver.find_element(*self.txt_email).send_keys(email)

    def preencher_senha(self, senha):
        self.driver.find_element(*self.txt_senha).send_keys(senha)

    def marcar_administrador(self):
        checkbox = self.driver.find_element(*self.chk_administrador)
        if not checkbox.is_selected():
            checkbox.click()

    def desmarcar_administrador(self):
        checkbox = self.driver.find_element(*self.chk_administrador)
        if checkbox.is_selected():
            checkbox.click()

    def clicar_botao_cadastrar(self):
        self.driver.find_element(*self.btn_cadastrar).click()

    def cad_user_adm(self, nome, email, senha):
        self.preencher_nome(nome)
        self.preencher_email(email)
        self.preencher_senha(senha)
        self.marcar_administrador()
        self.clicar_botao_cadastrar()

    def verificar_mensagem_sucesso(self):
        try:
            elemento = WebDriverWait(self.driver, 3).until(
                EC.visibility_of_element_located(self.msg_caduser_ok)
            )
            return elemento.text.strip()
        except TimeoutException:
            return None






