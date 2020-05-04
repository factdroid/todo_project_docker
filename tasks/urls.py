from django.urls import path

from .views import TaskListAndCreate, TaskUpdateView, TaskDeleteView

urlpatterns = [
    path('', TaskListAndCreate.as_view(), name='tasklistcreate'),
    path('<int:pk>/edit/', TaskUpdateView.as_view(), name='taskupdate'),
    path('<int:pk>/delete/', TaskDeleteView.as_view(), name='taskdelete')
]