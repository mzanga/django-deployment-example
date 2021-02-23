from django.urls import path
from first_app import views

# Template Tagging
app_name = 'first_app'

urlpatterns = [
    path('login/', views.user_login, name='user_login'),
    path('', views.first, name='first'),
    path('second_page/', views.second, name='second'),
    path('users/', views.user, name='user'),
    path('form/', views.form_name_view, name='form'),
    path('signup/', views.signup, name='signup'),
]
