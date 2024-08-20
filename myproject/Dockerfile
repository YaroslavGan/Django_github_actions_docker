# Используем официальный образ Python в качестве базового
FROM python:3.9-slim

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем файлы проекта в контейнер
COPY . /app

# Устанавливаем зависимости, указанные в requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Выполняем миграции для настройки базы данных
RUN python manage.py migrate

# Открываем порт 8000 для доступа к приложению
EXPOSE 8000

# Запускаем сервер при старте контейнера
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
