import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.patches import Patch

# Настройка стиля
plt.style.use("seaborn-v0_8")
fig, (ax1, ax2) = plt.subplots(
    2, 1, figsize=(16, 10), height_ratios=[2, 1], sharex=True
)

# Генерация данных (еженедельные данные вместо месячных)
np.random.seed(42)
dates = pd.date_range(
    "2014-01-01", "2023-12-31", freq="W"
)  # Еженедельно вместо ежемесячно
n = len(dates)

# Компоненты временного ряда
trend = 0.15 * np.arange(n)  # Линейный тренд (скорректирован для недельных данных)
seasonality = 8 * np.sin(2 * np.pi * np.arange(n) / 52) + 4 * np.sin(
    2 * np.pi * np.arange(n) / 26
)  # Сезонность (годовая и полугодовая)
noise = np.random.normal(0, 3, n)  # Шум

# Фактические значения
actual = trend + seasonality + noise + 50

# Прогноз (с некоторой ошибкой)
forecast = (
    trend + seasonality * 0.85 + np.random.normal(1, 2, n) + 50
)  # Прогноз с ошибкой

# Разделение на обучающую и тестовую выборки
split_point = int(n * 0.6)  # 60% для обучения, 40% для теста

# Добавление выбросов
actual[split_point + 20] += 20
actual[split_point + 60] -= 20

# Остатки
residuals = actual - forecast

train_dates = dates[:split_point]
test_dates = dates[split_point:]

# Первый график - временной ряд и прогноз (БЕЗ РАЗРЫВА)
ax1.plot(
    dates,
    actual,
    label="Фактические значения",
    color="#2E86AB",
    linewidth=1.5,
    alpha=0.9,
)
ax1.plot(
    test_dates,
    forecast[split_point:],
    label="Прогноз",
    color="#A23B72",
    linewidth=2,
    linestyle="-",
    marker="",
    markersize=2,
)

# Заливка для доверительного интервала прогноза
ax1.fill_between(
    test_dates,
    forecast[split_point:] - 8,
    forecast[split_point:] + 8,
    alpha=0.2,
    color="#A23B72",
    label="Доверительный интервал прогноза",
)

# Вертикальная линия начала прогноза
ax1.axvline(
    x=test_dates[0],
    color="red",
    linestyle=":",
    alpha=0.7,
    linewidth=2,
    label="Начало прогноза",
)

ax1.set_title(
    "Временной ряд с трендом, сезонностью и прогнозом",
    fontsize=32,  # Увеличено в 2 раза (было 16)
    fontweight="bold",
    pad=40,  # Увеличено пропорционально
)
ax1.set_ylabel("Значение", fontsize=24)  # Увеличено в 2 раза (было 12)
ax1.legend(loc="upper left", fontsize=24)  # Увеличена легенда
ax1.grid(True, alpha=0.3)

# Увеличение размера меток на осях
ax1.tick_params(axis="both", which="major", labelsize=20)

# Второй график - барчарт остатков (ТОЛЬКО для периода прогноза)
colors = ["#FF6B6B" if res > 0 else "#51A851" for res in residuals[split_point:]]
bars = ax2.bar(test_dates, residuals[split_point:], color=colors, alpha=0.8, width=5)

ax2.axhline(y=0, color="black", linewidth=0.8, linestyle="-")
ax2.set_title(
    "Остатки прогноза (Факт - Прогноз)",
    fontsize=32,  # Увеличено в 2 раза
    fontweight="bold",
    pad=40,
)
ax2.set_xlabel("Дата", fontsize=24)  # Увеличено
ax2.set_ylabel("Остаток", fontsize=24)  # Увеличено
ax2.grid(True, alpha=0.3)

# Создание кастомной легенды для остатков
legend_elements = [
    Patch(facecolor="#FF6B6B", label="Факт > Прогноз", alpha=0.8),
    Patch(facecolor="#51A851", label="Факт < Прогноз", alpha=0.8),
]
ax2.legend(handles=legend_elements, loc="upper right", fontsize=24)  # Увеличена

# Форматирование оси X
ax2.tick_params(axis="x", rotation=45, labelsize=20)  # Увеличены метки дат
ax2.xaxis.set_major_formatter(plt.matplotlib.dates.DateFormatter("%Y-%m"))

# Установка пределов по оси X
x_min = dates[0]
x_max = dates[-1]
ax1.set_xlim(x_min, x_max)
ax2.set_xlim(x_min, x_max)

plt.tight_layout(pad=3.0)  # Увеличен отступ для больших шрифтов
plt.show()
