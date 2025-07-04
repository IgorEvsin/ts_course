# Курс по анализу временных рядов

## Структура курса

### Глава 1. Одномерные временные ряды

#### Блок 1: Введение и основы
| Тема | Содержание | Материалы |
|------|------------|-----------|
| **0. Временные ряды как реализация случайного процесса** | <ul><li>Основные концепции и определения</li><li>Модели как фильтры vs предсказатели (ETS и ARIMA это и то и то)<li>Метрики качества прогноза: MAE, MAPE, sMAPE, MASE</li></ul> | [Adeshere: Введение в TS](https://habr.com/ru/articles/542638/) |

#### Блок 2: Декомпозиция рядов
| Тема | Содержание | Материалы |
|------|------------|-----------|
| **1. Компоненты временного ряда** | <ul><li>MECE-принцип бизнесового разложения</li><li>Тренды: линейные/нелинейные, детерминированные/стохастические</li><li>Сезонность: аддитивная и мультипликативная</li><li>Цикличность и шум</li><li>Наивные методы прогнозирования</li></ul> | [Habr: Компоненты ряда](https://habr.com/ru/articles/588320/)<br>[FPP3: Тренды](https://otexts.com/fpp3/stochastic-and-deterministic-trends.html)<br>[FPP3: Простые методы](https://otexts.com/fpp3/simple-methods.html) | 
| **2. Классические и эконометрические методы декомпозиции** | <ul><li>Скользящие средние и их варианты</li><li>Методы X-11 и X-12-ARIMA</li><li>SEATS (TRAMO/SEATS)</li><li>STL-декомпозиция</li><li>Экспоненциальное сглаживание (ETS)</li><li>Prophet от Facebook</li><li>Эконометрические фильтры (Ходрика-Прескотта)</li></ul> | [FPP3: Декомпозиция](https://otexts.com/fpp3/decomposition.html)<br>[FPP3: Таксономия](https://otexts.com/fpp3/taxonomy.html)<br>[FPP3: Prophet](https://otexts.com/fpp3/prophet.html) | 
| **3. Теория фильтрации сигналов** | <ul><li>Основы цифровой обработки сигналов</li><li>Разложение на сигнал и шум</li><li>Фильтр Калмана и его применения</li><li>Преобразование Фурье для TS</li><li>Вейвлет-анализ</li></ul> | Теория фильтрации сигналов<br>[FPP3: Сложная сезонность](https://otexts.com/fpp3/complexseasonality.html) | 

#### Блок 3: Свойства и преобразования рядов
| Тема | Содержание | Материалы |
|------|------------|-----------|
| **4. Преобразования временных рядов** | <ul><li>Преобразование Бокса-Кокса</li><li>Логарифмирование и степенные преобразования</li></ul> | [FPP3: Преобразования](https://otexts.com/fpp3/transformations.html) | 
| **5. Анализ свойств временного ряда** | <ul><li>Автокорреляция (ACF) и частичная автокорреляция (PACF)</li><li>Особенности работы с короткими рядами</li></ul> | [FPP3: STL Features](https://otexts.com/fpp3/stlfeatures.html) | 
| **6. Свойства стохастических процессов** | <ul><li>Стационарность и нестационарность</li><li>Эргодичность</li><li>Тесты на стационарность: Дики-Фуллера (ADF), KPSS</li><li>Эффект памяти и показатель Хёрста</li><li>Дробно-дифференцированные признаки</li><li>Спектральный анализ и спектральная плотность</li><li>Энтропия Шеннона для TS</li></ul> | [FPP3: Стационарность](https://otexts.com/fpp3/stationarity.html)<br>Chapter 5 de Prado | 
| **7. Аномалии и структурные изменения** | <ul><li>Типы аномалий в TS</li><li>Методы обнаружения выбросов</li><li>Структурные сдвиги и точки разладки</li><li>Кластеризация волатильности</li><li>Обработка пропусков данных</li></ul> | Chapter 18 de Prado | 

#### Блок 4: Прогнозирование и машинное обучение
| Тема | Содержание | Материалы |
|------|------------|-----------|
| **8. Оценка качества прогнозов** | <ul><li>Интервальные прогнозы и доверительные интервалы</li><li>CUSUM и следящий контрольный сигнал</li><li>Байесовские методы оценки</li><li>Гауссовские процессы (GPR)</li></ul> | [YouTube: Оценка качества прогноза](https://www.youtube.com/watch?v=Rmh6b96u6UU)<br>[FPP3: Точность распределений](https://otexts.com/fpp3/distaccuracy.html) |
| **9. Ансамбли моделей и стекинг** | <ul><li>Адаптивная композиция моделей</li><li>Селективное комбинирование прогнозов</li><li>Линейная агрегация взвешенных регрессий (ЛАВР)</li><li>Модели экспоненциального сглаживания (ETS)</li></ul> | [YouTube: Стекинг моделей](https://www.youtube.com/watch?v=Rmh6b96u6UU)<br>[FPP3: ETS](https://otexts.com/fpp3/ets.html) |
| **10. Практические аспекты прогнозирования** | <ul><li>Байесы в TS (forward-looking)</li><li>Влияние таймфрейма на волатильность и автокорреляцию</li><li>Технический анализ в финансах</li></ul> | [FPP3: Полезные предикторы](https://otexts.com/fpp3/useful-predictors.html)<br>[FPP3: Практическое прогнозирование](https://otexts.com/fpp3/practical.html)|
| **11. ML/DL для временных рядов** | <ul><li>Специализированные сплиттеры для TS</li><li>Кросс-валидация временных рядов</li><li>Бутстрап-методы для TS</li><li>BVD</li><li>Нейросетевые архитектуры для TS</li></ul> | [FPP3: Точность](https://otexts.com/fpp3/accuracy.html)<br>[FPP3: Выбор предикторов](https://otexts.com/fpp3/selecting-predictors.html)<br>[FPP3: Кросс-валидация TS](https://otexts.com/fpp3/tscv.html)<br>[FPP3: Бутстрап](https://otexts.com/fpp3/bootstrap.html) |

### Глава 2. Многомерные временные ряды

#### Блок 5: Взаимосвязи между рядами
| Тема | Содержание | Материалы |
|------|------------|-----------|
| **12. Анализ взаимосвязей** | <ul><li>Кросс-корреляция и её интерпретация</li><li>Проблема ложных корреляций</li><li>Коинтеграция и её тестирование</li><li>Причинно-следственный анализ (Granger causality)</li></ul> | [Habr: Многомерные TS](https://habr.com/ru/articles/542638/) |
| **13. Кластеризация временных рядов** | <ul><li>Метрики сходства для TS</li><li>Динамическое трансформирование времени (DTW)</li><li>Иерархические ряды и их особенности</li>Ряды как сумма/произведение других рядов</ul> | [YouTube: DTW](https://www.youtube.com/live/ShbWTtOyobE?si=AwAy6bUnz34GVmzY) |
| **14. Методы многомерного анализа** | <ul><li>Векторные авторегрессионные модели (VAR)</li><li>Копулы для моделирования зависимостей</li><li>Модели пространства состояний</li><li>Современные нейросетевые подходы</li></ul> | [FPP3: VAR](https://otexts.com/fpp3/VAR.html)<br>[FPP3: NNAR](https://otexts.com/fpp3/nnetar.html) | 
| **15. Панельные данные и анализ выживаемости** | <ul><li>Особенности работы с панельными данными</li><li>Основы анализа выживаемости</li></ul> | В разработке |

## Дополнительные ресурсы

### Практические материалы
- [Репозиторий GitHub с Jupyter-ноутбуками](https://github.com/IgorEvsin/ts_examples)

<table style="width: 100%; table-layout: fixed; border-collapse: collapse;">
  <colgroup>
    <col style="width: 30%">
    <col style="width: 50%">
    <col style="width: 20%">
  </colgroup>
  <thead>
    <tr style="border-bottom: 1px solid #ddd;">
      <th style="padding: 8px; text-align: left;">Тема</th>
      <th style="padding: 8px; text-align: left;">Содержание</th>
      <th style="padding: 8px; text-align: left;">Материалы</th>
    </tr>
  </thead>
  <tbody>
    <tr style="border-bottom: 1px solid #ddd;">
      <td style="padding: 8px; vertical-align: top;"><strong>1. Компоненты временного ряда</strong></td>
      <td style="padding: 8px; vertical-align: top;">
        <ul style="margin: 0; padding-left: 20px;">
          <li>MECE-принцип бизнесового разложения</li>
          <li>Тренды: линейные/нелинейные, детерминированные/стохастические</li>
          <li>Сезонность: аддитивная и мультипликативная</li>
          <li>Цикличность и шум</li>
          <li>Наивные методы прогнозирования</li>
        </ul>
      </td>
      <td style="padding: 8px; vertical-align: top;">
        <a href="https://habr.com/ru/articles/588320/">Habr: Компоненты ряда</a><br><br>
        <a href="https://otexts.com/fpp3/stochastic-and-deterministic-trends.html">FPP3: Тренды</a><br><br>
        <a href="https://otexts.com/fpp3/simple-methods.html">FPP3: Простые методы</a>
      </td>
    </tr>
    <tr style="border-bottom: 1px solid #ddd;">
      <td style="padding: 8px; vertical-align: top;"><strong>2. Классические и эконометрические методы декомпозиции</strong></td>
      <td style="padding: 8px; vertical-align: top;">
        <ul style="margin: 0; padding-left: 20px;">
          <li>Скользящие средние и их варианты</li>
          <li>Методы X-11 и X-12-ARIMA</li>
          <li>SEATS (TRAMO/SEATS)</li>
          <li>STL-декомпозиция</li>
          <li>Экспоненциальное сглаживание (ETS)</li>
          <li>Prophet от Facebook</li>
          <li>Эконометрические фильтры (Ходрика-Прескотта)</li>
        </ul>
      </td>
      <td style="padding: 8px; vertical-align: top;">
        <a href="https://otexts.com/fpp3/decomposition.html">FPP3: Декомпозиция</a><br><br>
        <a href="https://otexts.com/fpp3/taxonomy.html">FPP3: Таксономия</a><br><br>
        <a href="https://otexts.com/fpp3/prophet.html">FPP3: Prophet</a>
      </td>
    </tr>
    <tr>
      <td style="padding: 8px; vertical-align: top;"><strong>3. Теория фильтрации сигналов</strong></td>
      <td style="padding: 8px; vertical-align: top;">
        <ul style="margin: 0; padding-left: 20px;">
          <li>Основы цифровой обработки сигналов</li>
          <li>Разложение на сигнал и шум</li>
          <li>Фильтр Калмана и его применения</li>
          <li>Преобразование Фурье для TS</li>
          <li>Вейвлет-анализ</li>
        </ul>
      </td>
      <td style="padding: 8px; vertical-align: top;">
        Теория фильтрации сигналов<br><br>
        <a href="https://otexts.com/fpp3/complexseasonality.html">FPP3: Сложная сезонность</a>
      </td>
    </tr>
  </tbody>
</table>

<table style="width: 100%; table-layout: fixed; border-collapse: collapse; font-family: Arial, sans-serif;">
  <colgroup>
    <col style="width: 30%">
    <col style="width: 50%">
    <col style="width: 20%">
  </colgroup>
  <thead>
    <tr style="background-color: #f2f2f2; border-bottom: 2px solid #ddd;">
      <th style="padding: 12px 8px; text-align: left; font-weight: bold;">Тема</th>
      <th style="padding: 12px 8px; text-align: left; font-weight: bold;">Содержание</th>
      <th style="padding: 12px 8px; text-align: left; font-weight: bold;">Материалы</th>
    </tr>
  </thead>
  <tbody>
    <tr style="border-bottom: 1px solid #ddd;">
      <td style="padding: 10px 8px; vertical-align: top;"><strong>4. Преобразования временных рядов</strong></td>
      <td style="padding: 10px 8px; vertical-align: top;">
        <ul style="margin: 0; padding-left: 20px; line-height: 1.5;">
          <li>Преобразование Бокса-Кокса</li>
          <li>Логарифмирование и степенные преобразования</li>
        </ul>
      </td>
      <td style="padding: 10px 8px; vertical-align: top;">
        <a href="https://otexts.com/fpp3/transformations.html" style="color: #0066cc; text-decoration: none;">FPP3: Преобразования</a>
      </td>
    </tr>
    <tr style="border-bottom: 1px solid #ddd;">
      <td style="padding: 10px 8px; vertical-align: top;"><strong>5. Анализ свойств временного ряда</strong></td>
      <td style="padding: 10px 8px; vertical-align: top;">
        <ul style="margin: 0; padding-left: 20px; line-height: 1.5;">
          <li>Автокорреляция (ACF) и частичная автокорреляция (PACF)</li>
          <li>Особенности работы с короткими рядами</li>
        </ul>
      </td>
      <td style="padding: 10px 8px; vertical-align: top;">
        <a href="https://otexts.com/fpp3/stlfeatures.html" style="color: #0066cc; text-decoration: none;">FPP3: STL Features</a>
      </td>
    </tr>
    <tr style="border-bottom: 1px solid #ddd;">
      <td style="padding: 10px 8px; vertical-align: top;"><strong>6. Свойства стохастических процессов</strong></td>
      <td style="padding: 10px 8px; vertical-align: top;">
        <ul style="margin: 0; padding-left: 20px; line-height: 1.5;">
          <li>Стационарность и нестационарность</li>
          <li>Эргодичность</li>
          <li>Тесты на стационарность: Дики-Фуллера (ADF), KPSS</li>
          <li>Эффект памяти и показатель Хёрста</li>
          <li>Дробно-дифференцированные признаки</li>
          <li>Спектральный анализ и спектральная плотность</li>
          <li>Энтропия Шеннона для TS</li>
        </ul>
      </td>
      <td style="padding: 10px 8px; vertical-align: top;">
        <a href="https://otexts.com/fpp3/stationarity.html" style="color: #0066cc; text-decoration: none;">FPP3: Стационарность</a><br>
        Chapter 5 de Prado
      </td>
    </tr>
    <tr>
      <td style="padding: 10px 8px; vertical-align: top;"><strong>7. Аномалии и структурные изменения</strong></td>
      <td style="padding: 10px 8px; vertical-align: top;">
        <ul style="margin: 0; padding-left: 20px; line-height: 1.5;">
          <li>Типы аномалий в TS</li>
          <li>Методы обнаружения выбросов</li>
          <li>Структурные сдвиги и точки разладки</li>
          <li>Кластеризация волатильности</li>
          <li>Обработка пропусков данных</li>
        </ul>
      </td>
      <td style="padding: 10px 8px; vertical-align: top;">
        Chapter 18 de Prado
      </td>
    </tr>
  </tbody>
</table>


<table style="width:100%; table-layout:fixed; border-collapse:collapse; font-family:Arial,sans-serif;">
  <colgroup>
    <col style="width:30%">
    <col style="width:50%">
    <col style="width:20%">
  </colgroup>
  <thead>
    <tr style="background-color:#f5f5f5; border-bottom:2px solid #ddd;">
      <th style="padding:10px; text-align:left;">Тема</th>
      <th style="padding:10px; text-align:left;">Содержание</th>
      <th style="padding:10px; text-align:left;">Материалы</th>
    </tr>
  </thead>
  <tbody>
    <tr style="border-bottom:1px solid #eee;">
      <td style="padding:10px; vertical-align:top;"><strong>8. Оценка качества прогнозов</strong></td>
      <td style="padding:10px; vertical-align:top;">
        <ul style="margin:0; padding-left:20px;">
          <li>Интервальные прогнозы и доверительные интервалы</li>
          <li>CUSUM и следящий контрольный сигнал</li>
          <li>Байесовские методы оценки</li>
          <li>Гауссовские процессы (GPR)</li>
        </ul>
      </td>
      <td style="padding:10px; vertical-align:top;">
        <a href="https://www.youtube.com/watch?v=Rmh6b96u6UU" style="display:block; margin-bottom:5px;">YouTube: Оценка качества прогноза</a>
        <a href="https://otexts.com/fpp3/distaccuracy.html" style="display:block;">FPP3: Точность распределений</a>
      </td>
    </tr>
    <tr style="border-bottom:1px solid #eee;">
      <td style="padding:10px; vertical-align:top;"><strong>9. Ансамбли моделей и стекинг</strong></td>
      <td style="padding:10px; vertical-align:top;">
        <ul style="margin:0; padding-left:20px;">
          <li>Адаптивная композиция моделей</li>
          <li>Селективное комбинирование прогнозов</li>
          <li>Линейная агрегация взвешенных регрессий (ЛАВР)</li>
          <li>Модели экспоненциального сглаживания (ETS)</li>
        </ul>
      </td>
      <td style="padding:10px; vertical-align:top;">
        <a href="https://www.youtube.com/watch?v=Rmh6b96u6UU" style="display:block; margin-bottom:5px;">YouTube: Стекинг моделей</a>
        <a href="https://otexts.com/fpp3/ets.html" style="display:block;">FPP3: ETS</a>
      </td>
    </tr>
    <tr style="border-bottom:1px solid #eee;">
      <td style="padding:10px; vertical-align:top;"><strong>10. Практические аспекты прогнозирования</strong></td>
      <td style="padding:10px; vertical-align:top;">
        <ul style="margin:0; padding-left:20px;">
          <li>Байесы в TS (forward-looking)</li>
          <li>Влияние таймфрейма на волатильность и автокорреляцию</li>
          <li>Технический анализ в финансах</li>
        </ul>
      </td>
      <td style="padding:10px; vertical-align:top;">
        <a href="https://otexts.com/fpp3/useful-predictors.html" style="display:block; margin-bottom:5px;">FPP3: Полезные предикторы</a>
        <a href="https://otexts.com/fpp3/practical.html" style="display:block;">FPP3: Практическое прогнозирование</a>
      </td>
    </tr>
    <tr>
      <td style="padding:10px; vertical-align:top;"><strong>11. ML/DL для временных рядов</strong></td>
      <td style="padding:10px; vertical-align:top;">
        <ul style="margin:0; padding-left:20px;">
          <li>Специализированные сплиттеры для TS</li>
          <li>Кросс-валидация временных рядов</li>
          <li>Бутстрап-методы для TS</li>
          <li>BVD</li>
          <li>Нейросетевые архитектуры для TS</li>
        </ul>
      </td>
      <td style="padding:10px; vertical-align:top;">
        <a href="https://otexts.com/fpp3/accuracy.html" style="display:block; margin-bottom:5px;">FPP3: Точность</a>
        <a href="https://otexts.com/fpp3/selecting-predictors.html" style="display:block; margin-bottom:5px;">FPP3: Выбор предикторов</a>
        <a href="https://otexts.com/fpp3/tscv.html" style="display:block; margin-bottom:5px;">FPP3: Кросс-валидация TS</a>
        <a href="https://otexts.com/fpp3/bootstrap.html" style="display:block;">FPP3: Бутстрап</a>
      </td>
    </tr>
  </tbody>
</table>

### Глава 2. Многомерные временные ряды

<table style="width: 100%; table-layout: fixed; border-collapse: collapse; font-family: Arial, sans-serif; margin: 15px 0;">
  <colgroup>
    <col style="width: 30%">
    <col style="width: 50%">
    <col style="width: 20%">
  </colgroup>
  <thead>
    <tr style="background-color: #f8f9fa; border-bottom: 2px solid #dee2e6;">
      <th style="padding: 12px; text-align: left; font-weight: 600;">Тема</th>
      <th style="padding: 12px; text-align: left; font-weight: 600;">Содержание</th>
      <th style="padding: 12px; text-align: left; font-weight: 600;">Материалы</th>
    </tr>
  </thead>
  <tbody>
    <tr style="border-bottom: 1px solid #e9ecef;">
      <td style="padding: 12px; vertical-align: top;"><strong>12. Анализ взаимосвязей</strong></td>
      <td style="padding: 12px; vertical-align: top;">
        <ul style="margin: 0; padding-left: 20px; line-height: 1.6;">
          <li>Кросс-корреляция и её интерпретация</li>
          <li>Проблема ложных корреляций</li>
          <li>Коинтеграция и её тестирование</li>
          <li>Причинно-следственный анализ (Granger causality)</li>
        </ul>
      </td>
      <td style="padding: 12px; vertical-align: top;">
        <a href="https://habr.com/ru/articles/542638/" style="color: #0066cc; text-decoration: none;">Habr: Многомерные TS</a>
      </td>
    </tr>
    <tr style="border-bottom: 1px solid #e9ecef;">
      <td style="padding: 12px; vertical-align: top;"><strong>13. Кластеризация временных рядов</strong></td>
      <td style="padding: 12px; vertical-align: top;">
        <ul style="margin: 0; padding-left: 20px; line-height: 1.6;">
          <li>Метрики сходства для TS</li>
          <li>Динамическое трансформирование времени (DTW)</li>
          <li>Иерархические ряды и их особенности</li>
          <li>Ряды как сумма/произведение других рядов</li>
        </ul>
      </td>
      <td style="padding: 12px; vertical-align: top;">
        <a href="https://www.youtube.com/live/ShbWTtOyobE?si=AwAy6bUnz34GVmzY" style="color: #0066cc; text-decoration: none;">YouTube: DTW</a>
      </td>
    </tr>
    <tr style="border-bottom: 1px solid #e9ecef;">
      <td style="padding: 12px; vertical-align: top;"><strong>14. Методы многомерного анализа</strong></td>
      <td style="padding: 12px; vertical-align: top;">
        <ul style="margin: 0; padding-left: 20px; line-height: 1.6;">
          <li>Векторные авторегрессионные модели (VAR)</li>
          <li>Копулы для моделирования зависимостей</li>
          <li>Модели пространства состояний</li>
          <li>Современные нейросетевые подходы</li>
        </ul>
      </td>
      <td style="padding: 12px; vertical-align: top;">
        <a href="https://otexts.com/fpp3/VAR.html" style="color: #0066cc; text-decoration: none; display: block; margin-bottom: 8px;">FPP3: VAR</a>
        <a href="https://otexts.com/fpp3/nnetar.html" style="color: #0066cc; text-decoration: none;">FPP3: NNAR</a>
      </td>
    </tr>
    <tr>
      <td style="padding: 12px; vertical-align: top;"><strong>15. Панельные данные и анализ выживаемости</strong></td>
      <td style="padding: 12px; vertical-align: top;">
        <ul style="margin: 0; padding-left: 20px; line-height: 1.6;">
          <li>Особенности работы с панельными данными</li>
          <li>Основы анализа выживаемости</li>
        </ul>
      </td>
      <td style="padding: 12px; vertical-align: top;">
        В разработке
      </td>
    </tr>
  </tbody>
</table>