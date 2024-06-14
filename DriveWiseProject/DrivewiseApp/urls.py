from django.urls import path, include
from .views import register, login, home , about

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('dashboard/', include('dashboard.urls')),
]
