from django.urls import path

from . import views

urlpatterns = [

    path('', views.home,name='home'),
    path('card1/', views.card1,name="card1"),
    path('card2/', views.card2,name="card2"),
    path('card3/', views.card3,name="card3"),
    path('details/<int:id>/',views.details, name="details"),
    path('signup/',views.signup,name="signup"),
    path('login/', views.user_login, name="login"),
    path('logout/', views.user_logout, name="user_logout"),
]