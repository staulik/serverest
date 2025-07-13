from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def setup_browser():
    options = Options()
    options.add_argument('--disable-logging')  # Desativa alguns logs
    options.add_argument('--log-level=3')  # Minimiza log (fatal apenas)
    options.add_experimental_option('excludeSwitches', ['enable-logging'])  # Remove o "DevTools listening"

    service = ChromeService(ChromeDriverManager().install())

    driver = webdriver.Chrome(service=service, options=options)
    return driver
