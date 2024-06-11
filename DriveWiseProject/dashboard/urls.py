from django.urls import path
from .views import dashboard, driver_detail , AddDriverView
urlpatterns = [
    path('', dashboard, name= 'dashboard'),
    path('add_driver/', AddDriverView.as_view(), name='add_driver'),
    path('driver/<str:driver_id>/', driver_detail, name='driver_detail'),

]