from django.urls import path
from . import views

urlpatterns = [
    path('detail/<int:pk>', views.post_detail, name="detail"),
    path('like-post', views.like_post, name="like_post"),
    path('post_list', views.post_list, name="post_list"),
    path('create/', views.create_post, name='create_post'),
    ]
