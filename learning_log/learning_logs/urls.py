"""Определяет схемы URL для learning_logs."""

from django.urls import path
from . import views
# from django.conf.urls import url

app_name = 'learning_logs'
urlpatterns = [
    #homepage
    path('', views.index, name='index'),
    #Page with list all topic
    path('topics/', views.topics, name='topics'),
    #Страница с подробной информацией по отдельной теме
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    #Страница для добавления новой темы
    path('new_topic/', views.new_topic, name='new_topic'),
    #Страница для добавления новой записи
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    #Страница для редактирования записи
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
]
