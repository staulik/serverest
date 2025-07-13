from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import tempfile  # Para criar diretórios temporários únicos

def setup_browser():
    # Criando um diretório temporário único para dados do usuário
    user_data_dir = tempfile.mkdtemp()

    options = Options()
    options.add_argument(f"user-data-dir={user_data_dir}")  # Especificando o diretório de dados
    options.add_argument("--headless")  # Se precisar rodar em modo headless (sem interface gráfica)
    options.add_argument("--no-sandbox")  # Para evitar erro de sandbox no GitHub Actions
    options.add_argument("--disable-dev-shm-usage")  # Evita problemas de memória

    # Inicializando o ChromeDriver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    return driver
