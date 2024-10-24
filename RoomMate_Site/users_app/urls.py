from django.urls import path
from .views import homepage, login_view, register_view, user_info_view
from . import views


urlpatterns = [
    path('', homepage, name='homepage'),  # Set the homepage view for the root URL of users_app
    path('login/', login_view, name='login'),  # Login page
    path('register/', register_view, name='register'),  # Registration page
    path('user_info/', user_info_view, name='user_info'),  # User info page
    path('dashboard/', views.dashboard_view, name='dashboard'),  # Add this if it's missing
]
