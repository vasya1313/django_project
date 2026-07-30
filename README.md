# Блог

Проект **Блог** это обучающий проект в рамках курса **Python**. Направленный на изучение веб-разработки с использованием **Django**.

### Инструкция по установке:

Скачать проект:

```powershell
git clone https://github.com/vasya1313/django_project.git
```

Для установки необходимых зависимостей выполните команду:

```powershell
uv sync
```

### Запуск сервера локально:

Для запуска сервера выполните команду:

```powershell
make run
```

Для выхода нажмите **CTRL+C**

## Быстрый старт

Следуйте пошаговой инструкции для разворачивания и локального запуска проекта на вашем компьютере.

### 1. Установка зависимостей
Проект использует менеджер пакетов `uv`. Установите все необходимые зависимости, запустив команду:

```bash
uv sync
```

### 2. Настройка переменных окружения
Создайте локальный файл `.env` на основе предоставленного шаблона `.env.example`:

* **Linux / macOS:**
  ```bash
  cp .env.example .env
  ```
* **Windows (CMD):**
  ```cmd
  copy .env.example .env
  ```

Откройте созданный файл `.env` и укажите необходимые значения параметров (секретный ключ Django, флаг отладки `DEBUG`, настройки базы данных PostgreSQL):

```env
DEBUG=True
SECRET_KEY=django-insecure-your-secret-key-here
ALLOWED_HOSTS=127.0.0.1,localhost
DATABASE_URL=postgres://myuser:mypassword@127.0.0.1:5432/mydb
```

### 3. Запуск базы данных PostgreSQL в Docker
Для работы с базой данных разверните и запустите локальный контейнер PostgreSQL:

```bash
docker run   --name blog_db   -e POSTGRES_USER=myuser   -e POSTGRES_PASSWORD=mypassword   -e POSTGRES_DB=mydb   -p 5432:5432   -v blog_db_data:/var/lib/postgresql/data   -d postgres:17
```

> **Примечание:** Если контейнер уже был создан ранее, запустите его командой:
> ```bash
> docker start blog_db
> ```

### 4. Применение миграций
Выполните миграции для создания структуры таблиц в PostgreSQL:

```bash
uv run manage.py migrate
```

*(Опционально)* Если необходимо загрузить тестовые данные из дампа:
```bash
uv run manage.py loaddata datadump.json
```

### 5. Запуск сервера разработки
Запустите локальный сервер Django:

```bash
uv run manage.py runserver
```

После этого проект будет доступен в браузере по адресу `http://127.0.0.1:8000/`
