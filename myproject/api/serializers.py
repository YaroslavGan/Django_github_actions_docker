from rest_framework import serializers
from .models import Task

# Сериализатор для модели Task
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task  # Связываем сериализатор с моделью Task
        fields = '__all__'  # Автоматически включаем все поля модели
