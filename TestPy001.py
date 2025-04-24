# from selenium.webdriver import Edge
# driver = Edge()
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# # Настройка WebDriver
# driver = webdriver.Edge(executable_path='C:\WebdriverEdge\msedgedriver.exe')

# try:
#     # Открываем сайт
#     driver.get("https://shop.fitonapp.com")

#     # Явное ожидание загрузки страницы (например, появления товаров)
#     wait = WebDriverWait(driver, 10)  # Максимальное время ожидания: 10 секунд
#     wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "product-index")))

#     # Находим все товары
#     products = driver.find_elements(By.CLASS_NAME, "product-index")
#     print(f"Найдено товаров: {len(products)}")

#     # Проходим по каждому товару
#     for index, product in enumerate(products):
#         # Находим ссылку на товар
#         link = product.find_element(By.TAG_NAME, "a")

#         # Кликаем по ссылке
#         link.click()

#         # Явное ожидание загрузки страницы товара
#         wait.until(EC.presence_of_element_located((By.TAG_NAME, "h1")))  # Например, ждем заголовок

#         # Возвращаемся на главную страницу
#         driver.back()

#         # Явное ожидание загрузки главной страницы
#         wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "product-index")))

# finally:
#     # Закрываем браузер
#     driver.quit()
#     #update test


import http.client

conn = http.client.HTTPSConnection('search.wb.ru')
headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,ru;q=0.8',
    'dnt': '1',
    'origin': 'https://www.wildberries.ru',
    'priority': 'u=1, i',
    'referer': 'https://www.wildberries.ru/catalog/0/search.aspx?search=dell%20xps%2015',
    'sec-ch-ua': '"Microsoft Edge";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36 Edg/135.0.0.0',
    'x-captcha-id': 'Catalog 1|1|1745462520|AA==|c5c53ff4729d47ef8ce814c1a760f358|wqmTkE1onBpXdUffep5WTNksvJEcrQlASBcb8NagPUh',
    'x-queryid': 'qid501854181173139142720250423224209',
    'x-userid': '0',
}
conn.request(
    'GET',
    '/exactmatch/ru/common/v13/search?ab_testing=false&appType=1&curr=rub&dest=-1257786&hide_dtype=13&lang=ru&query=dell%20xps%2015&resultset=filters&spp=30&suppressSpellcheck=false',
    headers=headers
)
response = conn.getresponse()   