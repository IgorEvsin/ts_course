# Программа курса по временным рядам

## Структура курса

### Глава 1. Одномерные временные ряды

#### Блок: Интро
0. **Тема**: Временные ряды как реализация случайного процесса  
    - **Содержание**:
        - Разница между моделью как фильтром и как предсказателем. ETS, ARIMA можно использовать и так, и так.  
    - **Материалы**:
        - [Adeshere](https://habr.com/ru/articles/542638/)  

#### Блок: Декомпозиция ряда
1. **Тема**: Компоненты ряда  
    - **Содержание**:  
        - MECE бизнесовое разложение ряда (см. иерархические ряды).  
        - Тренд (линейный и нелинейный, детерминированный и стохастический).  
        - Сезонность. Цикличность. Шум.  
        - Наивные методы.  
    - **Материалы**:  
        - [Habr: Компоненты ряда](https://habr.com/ru/articles/588320/#comment_23712377)  
        - [Habr: Детерминированные и стохастические тренды](https://habr.com/ru/articles/821231/#comment_26942703)  
        - [FPP3: Stochastic and Deterministic Trends](https://otexts.com/fpp3/stochastic-and-deterministic-trends.html)  
        - [FPP3: Transformations](https://otexts.com/fpp3/transformations.html)  
        - [FPP3: Complex Seasonality](https://otexts.com/fpp3/complexseasonality.html)  
        - [FPP3: Simple Methods](https://otexts.com/fpp3/simple-methods.html)  

2. **Тема**: Классические и эконометрические методы декомпозиции ряда  
    - **Содержание**:  
        - Классика: скользящее окно, X-11, SEATS, STL, ETS (и его вариации), Prophet.  
        - Эконометрические фильтры (Прескотт).  
    - **Материалы**:  
        - [FPP3: Decomposition](https://otexts.com/fpp3/decomposition.html)  
        - [FPP3: Taxonomy](https://otexts.com/fpp3/taxonomy.html)  
        - [FPP3: Prophet](https://otexts.com/fpp3/prophet.html)  
        - Теория фильтрации  

3. **Тема**: Теория фильтрации сигналов  
    - **Содержание**:  
        - Разложение на сигнал и шум.  
        - Калман, Фурье, вейвлет, технические индикаторы.  
    - **Материалы**:
        - Теория фильтрации  

#### Блок: Свойства рядов и преобразования
4. **Тема**: Преобразования временного ряда  
    - **Содержание**:
        - Бокс-Кокс, другие преобразования и их назначение.  
    - **Материалы**:  
        - [FPP3: Transformations](https://otexts.com/fpp3/transformations.html#mathematical-transformations)  

5. **Тема**: Свойства временного ряда  
    - **Содержание**:
        - ACF/PACF, выраженность тренда и сезонности.  
    - **Материалы**:
        - [FPP3: STL Features](https://otexts.com/fpp3/stlfeatures.html)  

6. **Тема**: Свойства процесса  
    - **Содержание**:  
        - Эргодичность, стационарность.  
        - DF/ADF, KPSS тест.  
        - Эффект памяти. Херст. Дробно-дифференцированные признаки.  
        - Спектральный анализ. Спектральная энтропия (Шэннона).  
    - **Материалы**:  
        - [FPP3: Stationarity](https://otexts.com/fpp3/stationarity.html)  
        - Chapter 5 de Prado  

7.  - **Тема**: Аномалии, структурные сдвиги, пропуски  
    - **Содержание**:
        - Смена режима: кластеризация волатильности, скачки.  
    - **Материалы**:
        - Chapter 18 de Prado  

#### Блок: ML
8. **Тема**: Оценка качества прогноза. Интервальные прогнозы.  
    - **Содержание**: CUSUM, следящий контрольный сигнал. Байес, GPR.  
    - **Материалы**:  
        - [YouTube: Оценка качества прогноза](https://www.youtube.com/watch?v=Rmh6b96u6UU)  
        - [FPP3: Distributional Accuracy](https://otexts.com/fpp3/distaccuracy.html)  

9. **Тема**: Стекинг моделей  
    - **Содержание**:
        - Адаптивная композиция/селективная модель, ЛАВР, ETS.  
    - **Материалы**:  
        - [YouTube: Стекинг моделей](https://www.youtube.com/watch?v=Rmh6b96u6UU)  
        - [FPP3: ETS](https://otexts.com/fpp3/ets.html)  

10. **Тема**: Полезные советы. Технический анализ.  
    - **Содержание**: TS biases (forward-looking). Влияние таймфрейма на волатильность и автокорреляцию.  
    - **Материалы**:  
        - [FPP3: Useful Predictors](https://otexts.com/fpp3/useful-predictors.html)  
        - [FPP3: Practical Forecasting](https://otexts.com/fpp3/practical.html)  

11. **Тема**: ML/DL for TS  
    - **Содержание**:  
        - Сплиттеры, метрики качества прогноза.  
        - Бутстрап, BVD.  
    - **Материалы**:  
        - [FPP3: Accuracy](https://otexts.com/fpp3/accuracy.html)  
        - [FPP3: Selecting Predictors](https://otexts.com/fpp3/selecting-predictors.html)  
        - [FPP3: Time Series Cross-Validation](https://otexts.com/fpp3/tscv.html)  
        - [FPP3: Bootstrap](https://otexts.com/fpp3/bootstrap.html)  

### Глава 2. Многомерные временные ряды (TBU!)
12. **Тема**: Взаимосвязь между рядами  
    - **Содержание**:
        - Ложные корреляции. Коинтеграция. Причинность.  
    - **Материалы**:
        - [Habr: Временные ряды](https://habr.com/ru/articles/542638/)  

13. **Тема**: Кластеризация временных рядов  
    - **Содержание**:
        - DTW. Иерархические ряды.  
    - **Материалы**:
        - [YouTube: DTW](https://www.youtube.com/live/ShbWTtOyobE?si=AwAy6bUnz34GVmzY)  

14. **Тема**: Моделирование многомерных временных рядов  
    - **Содержание**:
        - Копулы, VAR, современные методы.  
    - **Материалы**:  
        - [FPP3: VAR](https://otexts.com/fpp3/VAR.html)  
        - [FPP3: Neural Network AR](https://otexts.com/fpp3/nnetar.html)  

15. **Тема**: Панельные данные. Анализ выживаемости  
    - **Содержание**:
        - В разработке.  