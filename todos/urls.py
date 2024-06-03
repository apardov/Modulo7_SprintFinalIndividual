from django.urls import path

from todos import views

app_name = 'todos'
urlpatterns = [
    path('', views.authenticated, name='authenticated'),
    path('create/', views.create_todo, name='create_todo'),
    path('view/<int:todo_id>/', views.view_todo, name='view_todo'),
    path('modify/<int:todo_id>/', views.modify_todo, name='modify_todo'),
    path('delete/<int:todo_id>/', views.delete_todo, name='delete_todo'),
    path('complete_todo/<int:todo_id>/', views.complete_todo, name='complete_todo')
]
