import time


def highlight_element(driver, element, duration=0.3, blinks=2):
    """
    Realça o elemento com uma borda amarela piscando (duplo blink).

    :param driver: Instância do WebDriver
    :param element: Elemento WebElement a ser destacado
    :param duration: Tempo de cada blink (em segundos)
    :param blinks: Quantidade de piscadas
    """
    original_style = element.get_attribute('style')
    highlight_style = "border: 3px solid yellow;"

    for _ in range(blinks):
        driver.execute_script("arguments[0].setAttribute('style', arguments[1]);", element, highlight_style)
        time.sleep(duration)
        driver.execute_script("arguments[0].setAttribute('style', arguments[1]);", element, original_style)
        time.sleep(duration)

