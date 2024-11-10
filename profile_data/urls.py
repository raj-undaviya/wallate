from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='homePage'),
    path('register/', views.register, name='registerPage'),
    path('dashboard/', views.dashboard, name='dashbaordPage')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)