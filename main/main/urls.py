from django.contrib import admin
from django.urls import path, include
from patient.views import home  # Import the home view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('patient.urls')),
    path('home/', home, name='home'),  # Added home endpoint
]