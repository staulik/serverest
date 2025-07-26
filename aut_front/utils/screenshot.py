import os
from datetime import datetime
import allure
from allure_commons.types import AttachmentType

def salvar_print(driver, nome_base):
    # Cria o diretório de evidências, se não existir
    pasta = "reports/evidencias"
    os.makedirs(pasta, exist_ok=True)

    # Gera nome do arquivo com timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    nome_arquivo = f"{nome_base}_{timestamp}.png"
    caminho = os.path.join(pasta, nome_arquivo)

    # Captura o print da tela
    driver.save_screenshot(caminho)

    # Anexa no Allure
    with open(caminho, "rb") as imagem:
        allure.attach(imagem.read(), name=nome_base, attachment_type=AttachmentType.PNG)

    return caminho



