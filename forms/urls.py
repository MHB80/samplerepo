from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_login, name='login'),
    path('logout/',views.User_logout_view, name='logout'),
    path('data/', views.form_data_view, name="data"),
    path('formtemplate/',views.form_data_view,name='formsubmission'),
]