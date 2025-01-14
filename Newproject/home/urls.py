from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/',views.login,name='login'),
    path('signup/',views.signup,name='signup'),
    path('input/',views.studentForm,name="studentForm"),
    path('info/',views.getinfo,name='getinfo')
]
