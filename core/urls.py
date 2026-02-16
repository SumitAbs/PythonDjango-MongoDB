from django.contrib import admin
from django.urls import path, include

# Professional comment: Root routing - delegates 'users/' and home to accounts app
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')), 
]