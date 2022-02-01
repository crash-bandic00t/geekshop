from django.urls import URLPattern, path
from . import views

app_name = 'authapp'
urlpatterns = [
    path('login/', views.login),

]