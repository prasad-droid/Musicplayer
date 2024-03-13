from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage),
    path('login', views.loginpage),
    path('signup', views.signuppage),
    path('playlist/<int:id>', views.playlistpage),
    path('music', views.mymusicpage),
    path('showlist/<int:id>', views.showlist),
    path('showalbum/<int:id>', views.showalbum),
    path('likepage', views.searchpage),
    path('songplay/<str:string_id>', views.songplay)
]