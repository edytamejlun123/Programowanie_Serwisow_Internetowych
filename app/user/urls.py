from django.urls import path

from . import views


app_name = 'user'

urlpatterns = [
    path('create/', views.CreateUserView.as_view(), name='create'),
    path('token/', views.CreateTokenView.as_view(), name='token'),
    path('profile/', views.ManageUserView.as_view(), name='profile'),
    path('auto-list', views.AutoListAPIView.as_view(), name='auto-list'),
    path('visit-list', views.VisitListAPIView.as_view(), name='visit-list'),

]
