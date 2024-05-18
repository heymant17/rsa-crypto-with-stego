from django.urls import path
from . import views

urlpatterns=[
path('',views.home,name="home"),
path('register',views.register,name="register"),
path('login',views.login,name="login"),
path('profile',views.profile,name="profile"),
path('createroom', views.createroom, name="createroom"),
path('viewroom', views.viewroom,name="viewroom"),
path('<str:room_name>', views.room, name="room")
]
