from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.index, name="index"),
    path('login', views.login_view, name="login"),
    path('register', views.register, name="register"),
    path('logout', views.logout, name="logout"),
    path('setup', views.setup, name="setup"),
    path('me', views.me, name='me'),
    path('profiles/<str:name>', views.profiles, name='profiles'),
    path('search/<str:context>', views.search, name='search'),

    # API Routes

    path('conversations/post')
]
