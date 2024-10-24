from django.contrib import admin
from django.urls import path, include
from users_app.views import homepage  # Import the homepage view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users_app.urls')),  # Include the users_app URLs
    path('', homepage, name='homepage'),  # Add this line for the root URL
]
