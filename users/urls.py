from django.urls import path
from .views import register, Login
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('sign/', register, name='sign'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout')

]