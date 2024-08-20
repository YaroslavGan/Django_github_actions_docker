import pytest
from rest_framework.test import APIClient
from .models import Task

@pytest.mark.django_db
def test_create_task():
    client = APIClient()  # Создаем клиента для API запросов
    response = client.post('/api/tasks/', {'title': 'Test Task', 'description': 'Test Description', 'completed': False})
    
    # Проверяем успешное создание задачи
    assert response.status_code == 201
    assert Task.objects.count() == 1  # Убедимся, что задача действительно добавлена

@pytest.mark.django_db
def test_get_tasks():
    # Создаем тестовую задачу в базе данных
    Task.objects.create(title="Test Task", description="Test Description", completed=False)
    
    client = APIClient()
    response = client.get('/api/tasks/')  # Отправляем GET-запрос для получения списка задач
    
    # Проверяем успешное получение списка задач
    assert response.status_code == 200
    assert len(response.data) == 1  # Убедимся, что возвращена одна задача
