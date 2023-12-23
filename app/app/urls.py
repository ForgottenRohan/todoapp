
from django.contrib import admin
from django.urls import path, include
from users.views import Tasks, CreateTasks, DeleteTasks

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Tasks.as_view(), name='main'),
    path('delete/', DeleteTasks.as_view(), name='delete_task'),
    path('create/', CreateTasks.as_view(), name='create_task'),
    path('users/', include('users.urls'), name='users'), 
]
