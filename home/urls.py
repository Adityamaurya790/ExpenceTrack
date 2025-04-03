# filepath: d:\cse\semester-8\Django\expenceTrack\home\urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),  # About page
    path('contact/', views.contact, name='contact'),  # Contact page
    path('login/', views.login, name='login'),  # Login page
    path('signup/', views.signup, name='signup'),  # Signup page
    path('user/', views.user_page, name='user_page'),  # User page
    path('logout/', views.logout_view, name='logout'),  # Logout page

    path('admin/', views.admin, name='admin'),  # Admin page
    path('messages/', views.messages,name='messages'),  # Messages page
]