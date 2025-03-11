import csv
import numpy as np
import matplotlib.pyplot as plt

# Чтение данных из CSV и обработка
csv_filename = "divan_prices.csv"
data = []

try:
    with open(csv_filename, "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader)  # Пропускаем заголовок
        for row in reader:
            try:
                price = row[0].replace("руб.", "").replace("₽", "").strip()  # Убираем 'руб.' и '₽'
                price = int("".join(filter(str.isdigit, price)))  # Оставляем только цифры
                data.append(price)
            except ValueError:
                print(f"Ошибка обработки строки: {row}")

    # Перезапись файла с обработанными данными
    with open(csv_filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Цена"])
        for price in data:
            writer.writerow([price])
except FileNotFoundError:
    print(f"Файл {csv_filename} не найден.")
    exit()

# Проверка наличия данных
if not data:
    print("Нет данных для анализа.")
    exit()

# Расчет средней цены
average_price = np.mean(data)
print(f"Средняя цена: {average_price:.2f} ₽")

# Построение гистограммы
plt.figure(figsize=(10, 6))
plt.hist(data, bins=20, color='skyblue', edgecolor='black')
plt.axvline(average_price, color='red', linestyle='dashed', linewidth=2, label=f'Средняя цена: {average_price:.2f} ₽')
plt.xlabel("Цена (₽)")
plt.ylabel("Количество товаров")
plt.title("Распределение цен на диваны")
plt.legend()
plt.grid(True)
plt.show()