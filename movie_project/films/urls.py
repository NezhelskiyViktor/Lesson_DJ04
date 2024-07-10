from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.page1, name='page1'),
    path('page2/', views.page2, name='page2'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
