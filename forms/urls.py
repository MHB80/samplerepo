from django.urls import path
from . import views

urlpatterns = [
    # path('form/',views.,name = 'form'),
    path('', views.user_login, name='login'),
]