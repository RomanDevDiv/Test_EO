from selenium.webdriver import Edge
driver = Edge()
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Настройка WebDriver
driver = webdriver.Edge(executable_path='C:\WebdriverEdge\msedgedriver.exe')

try:
    # Открываем сайт
    driver.get("https://shop.fitonapp.com")

    # Явное ожидание загрузки страницы (например, появления товаров)
    wait = WebDriverWait(driver, 10)  # Максимальное время ожидания: 10 секунд
    wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "product-index")))

    # Находим все товары
    products = driver.find_elements(By.CLASS_NAME, "product-index")
    print(f"Найдено товаров: {len(products)}")

    # Проходим по каждому товару
    for index, product in enumerate(products):
        # Находим ссылку на товар
        link = product.find_element(By.TAG_NAME, "a")

        # Кликаем по ссылке
        link.click()

        # Явное ожидание загрузки страницы товара
        wait.until(EC.presence_of_element_located((By.TAG_NAME, "h1")))  # Например, ждем заголовок

        # Возвращаемся на главную страницу
        driver.back()

        # Явное ожидание загрузки главной страницы
        wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "product-index")))

finally:
    # Закрываем браузер
    driver.quit()