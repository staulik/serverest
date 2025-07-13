from pages.login_page import LoginPage

class LoginLibrary:
    def __init__(self):
        self.driver = None
        self.page = None

    def set_driver(self, driver):
        """Recebe o WebDriver criado pelo SeleniumLibrary e instancia a LoginPage."""
        self.driver = driver
        self.page = LoginPage(driver)

    def validar_elementos_visuais(self):
        """Chama o método de validação da LoginPage."""
        self.page.validar_elementos_visuais()
