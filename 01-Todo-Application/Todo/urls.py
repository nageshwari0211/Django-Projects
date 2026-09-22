from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.signup, name='signup'),          # 127.0.0.1:8000
    path('login/', views.login_view, name='login'), # 127.0.0.1:8000/login/
    path('todo/', views.todo, name='todo'),         # 127.0.0.1:8000/todo/
    path('logout/', views.logout_view, name='logout'),
]