from django.urls import path
from .views import VisitCreateAPIView

urlpatterns = [
    # Inne ścieżki URL Twojej aplikacji
    path('create-visit/', VisitCreateAPIView.as_view(), name='create-visit'),
]
