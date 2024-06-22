from django.urls import path
from .views import dashboard, driver_detail , AddDriverView , RemoveDriverView
urlpatterns = [
    path('', dashboard, name= 'dashboard'),
    path('add_driver/', AddDriverView.as_view(), name='add_driver'),
    path('remove_driver/', RemoveDriverView.as_view(), name='remove_driver'),
    path('driver/<str:driver_id>/', driver_detail, name='driver_detail'),

]