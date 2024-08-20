from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet

# Создаем маршрутизатор и регистрируем наш ViewSet
router = DefaultRouter()
router.register(r'tasks', TaskViewSet)

# Подключаем маршрутизатор к основным URL приложения
urlpatterns = [
    path('', include(router.urls)),
]
