from django.urls import path

from . import views

app_name = "quiz"

urlpatterns = [
    # path('index/', views.IndexView.as_view(), name='index'),
    path('question/', views.question_view, name='question'),
    path('result/', views.result_view, name='result'),
    path('home/', views.HomeView.as_view(), name='home'),
]
