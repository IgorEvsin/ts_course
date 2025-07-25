# Руководство по внесению вклада
Добро пожаловать в проект учебника по временным рядам! Мы рады вашему участию.


## Содержание
1. [Структура проекта](#-структура-проекта)
2. [Процесс внесения изменений](#-процесс-внесения-изменений)
3. [Требования к оформлению](#-требования-к-оформлению)
4. [Сборка проекта](#-сборка-проекта)


## Структура проекта
```
.
├── code_examples/      # Примеры кода на Python
├── images/             # Графики и изображения
├── src/                # Исходные tex-файлы
│   ├── chapters/       # Главы учебника
├── tex/                # Стилевые файлы
├── README.md
├── CONTRIBUTING.md
├── main.tex            # Главный файл
└── main.pdf            # Скомпилированный учебник

```


## Процесс внесения изменений
### 1. Подготовка репозитория
```bash
# Клонируйте репозиторий
git clone git@github.com:IgorEvsin/ts_course.git
# Перейдите в директорию проекта
cd ts_course
```
### 2. Создание ветки
```bash
# Обновите основную ветку
git checkout main
git pull origin main
# Создайте новую ветку
git checkout -b type/краткое-описание
```
**Правила именования веток**:
| Тип        | Пример                   | Когда использовать         |
|------------|--------------------------|----------------------------|
| `feature/` | `feature/ch3-arima`      | Добавление нового материала |
| `fix/`     | `fix/typo-ch2`           | Исправление ошибок         |

### 3. Внесение изменений
**Для текста учебника**:
- Размещайте изменения в соответствующих файлах в `src/chapters/`
- Используйте [семантические коммиты](https://www.conventionalcommits.org/en/v1.0.0/):
  ```bash
  git commit -m "feat: добавить раздел про ARIMA модели"
  git commit -m "fix: исправить опечатку в главе 2"
  ```
- В качестве форматтера мы используем `tex-fmt`, его конфиг размещен в корне проекта в файле `tex-fmt.toml`
- Мы также используем pre-commit, пожалуйста установите его перед тем как делать коммиты

**Для примеров кода**:
1. Добавьте скрипт в `code_examples/` (формат: `chX_topicY.py`)
2. Вставьте в текст учебника:
```latex
\begin{minipage}{\linewidth}
    \lstinputlisting[
        style=python,
        caption={Пример реализации модели ARIMA}
    ]{code_examples/ch3_arima.py}
\end{minipage}
```
**Для графиков**:
- Формат: PDF (предпочтительно) или PNG
- Название файла: `chX_figY_description.ext`
- Вставка в текст:
```latex
\begin{figure}[h]
    \centering
    \includegraphics[width=0.8\textwidth]{images/ch2_fig1_acf_pacf.pdf}
    \caption{Графики ACF и PACF}
    \label{fig:acf-pacf}
\end{figure}
```
### 4. Проверка сборки
Перед коммитом убедитесь, что проект компилируется:
```bash
pdflatex -output-directory=./ -interaction=nonstopmode src/main.tex
```
### 5. Создание Pull Request
1. Загрузите ветку на GitHub:
   ```bash
   git push origin feature/your-branch-name
   ```
2. На GitHub:
   - Откройте Pull Request в ветку `main`
   - Добавьте понятное описание изменений
   - Укажите связанные issues (через #номер)
   - Прикрепите скриншоты для визуальных изменений
   - Назначьте 1-2 ревьюверов
### 6. Процесс ревью
- Дождитесь обратной связи от ревьюверов
- Вносите необходимые правки в ту же ветку
- После получения апрува изменения будут смержены
- Удалите ветку после мержа (на GitHub и локально)

## Требования к оформлению
### Текстовый контент
- **Новые термины**: выделяйте курсивом при первом упоминании
- **Математические формулы**:
  ```latex
  \begin{equation}
      X_t = c + \sum_{i=1}^p \phi_i X_{t-i} + \varepsilon_t
  \end{equation}
  ```
- **Перекрестные ссылки**: используйте `\ref{fig:example}` и `\cite{author2023}`
### Примеры кода
- Соответствуйте PEP8 для Python-кода
- Добавляйте комментарии для сложных участков
- Тестируйте код перед добавлением
### Изображения
- Разрешение: минимум 300 DPI
- Подписи: полные описания с номером главы
- Источники: указывайте для заимствованных изображений
## Сборка проекта
### Требования
- [TeX Live](https://www.tug.org/texlive/) (Рекомендуем) или [MiKTeX](https://miktex.org/)
- Python 3.8+ (для генерации графиков)
- Рекомендуемые пакеты: `pdflatex`, `biber`, `make`
### Команды сборки
Базовая компиляция:
```bash
pdflatex -output-directory=./ -interaction=nonstopmode src/main.tex
```
Полная сборка (с библиографией и перекрестными ссылками):
```bash
pdflatex -synctex=1 -interaction=nonstopmode -file-line-error main.tex
biber main
pdflatex -synctex=1 -interaction=nonstopmode -file-line-error main.tex
pdflatex -synctex=1 -interaction=nonstopmode -file-line-error main.tex
```
## 🤝 Спасибо за ваш вклад в развитие учебника! 🤝