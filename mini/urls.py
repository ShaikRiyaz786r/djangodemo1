from django.contrib import admin
from django.urls import path
from myapp.views import firstView,secondView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', firstView),
    path('signup/',secondView),
]
