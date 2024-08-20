import pytest
from .models import Task

@pytest.mark.django_db
def test_task_creation():
    # Создаем новую задачу
    task = Task.objects.create(title="Test Task", description="Test Description", completed=False)
    
    # Проверяем, что задача была создана корректно
    assert task.title == "Test Task"
    assert not task.completed
