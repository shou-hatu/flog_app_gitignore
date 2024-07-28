from django.urls import path
from . import views

urlpatterns = [
    path("home/", views.PostView.as_view(), name="home"),
    path('create/', views.PostCreateView.as_view(), name='create'),
    path('<int:pk>/', views.PostDetailView.as_view(), name='detail'),
    path('<int:pk>/delete/', views.PostDeleteView.as_view(), name='delete'),
    ]
