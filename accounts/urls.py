from django.contrib.auth import views as auth_views
from django.urls import path

# 同じディレクトリ(今回はaccounts)からviews.pyをimportしている
from . import views  # .（ピリオド1つ）が同じディレクトリを表す

app_name = "accounts"

urlpatterns = [
    path(
        "signup/", views.SignupView.as_view(
            template_name='../templates/FrontFiles/login_signup/signup.html'), name="signup"
    ),  # 第三引数のnameはパターンネームといい、signup.htmlでビューを呼び出すために記述される
    path("login/", auth_views.LoginView.as_view(
        template_name='../templates/FrontFiles/login_signup/login.html'), name="login"),
    # auth_views.UserLoginViewでviews.pyの UserLoginView を呼び出している
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path('profile/<str:username>/', views.user_profile_view,
         name='user_profile'),
]
