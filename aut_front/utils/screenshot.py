import os
from datetime import datetime

def salvar_print(driver, nome_base):
    # Cria o diretório de evidências, se não existir
    pasta = "reports/evidencias"
    os.makedirs(pasta, exist_ok=True)

    # Gera nome do arquivo com timestamp pra evitar sobrescrever
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    nome_arquivo = f"{nome_base}_{timestamp}.png"
    caminho = os.path.join(pasta, nome_arquivo)

    # Captura o print da tela
    driver.save_screenshot(caminho)
    return caminho


