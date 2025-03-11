from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import csv
import time

# Настройка Selenium
options = Options()
options.add_argument("--headless")  # Запуск в фоновом режиме
options.add_argument("--disable-blink-features=AutomationControlled")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get("https://www.divan.ru/category/divany-i-kresla")

# Ожидание загрузки страницы
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.XPATH, "//span[@data-testid='price']")))

# Прокрутка страницы для загрузки всех товаров
last_height = driver.execute_script("return document.body.scrollHeight")
while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

# Сбор данных
prices = driver.find_elements(By.XPATH, "//span[@data-testid='price']")
data = []

if not prices:
    print("Не удалось найти цены. Проверьте селекторы.")
else:
    for price in prices:
        try:
            data.append([price.text])
        except Exception as e:
            print(f"Ошибка при обработке цены: {e}")

# Сохранение в CSV
csv_filename = "divan_prices.csv"
with open(csv_filename, "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Цена"])
    writer.writerows(data)

print(f"Данные сохранены в {csv_filename}")

# Закрытие браузера
driver.quit()
