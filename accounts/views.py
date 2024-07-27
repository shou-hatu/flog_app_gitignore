from django.conf import settings
from django.contrib.auth import authenticate, get_user_model, login,logout
from django.urls import reverse_lazy
from django.views.generic import CreateView
from quiz.models import Player_result
from django.shortcuts import render, redirect
from django.db.models import Max, Min


from .forms import SignupForm, UserUpdateForm

User = get_user_model()


class SignupView(CreateView):
    form_class = SignupForm
    template_name = "accounts/signup.html"
    success_url = reverse_lazy(settings.LOGIN_REDIRECT_URL)  # 遷移先の指定

    def form_valid(self, form):  # form_valid関数のオーバーライド
        response = super().form_valid(form)
        username = form.cleaned_data["username"]
        password1 = form.cleaned_data["password1"]  # passwordはキーに存在しないためpassword1にする
        user = authenticate(self.request, username=username, password=password1)
        login(self.request, user)
        return response


def user_profile_view(request, username):
    user = User.objects.get(username=username)  # usernameフィールドと受け取った入力値が等しくなるような行を抽出
    player_result = Player_result.objects.filter(user=user)
    max_rate_invite = player_result.aggregate(Max('flog_rate_invite'))['flog_rate_invite__max']
    max_rate_date = player_result.aggregate(Max('flog_rate_date'))['flog_rate_date__max']
    max_rate_confession = player_result.aggregate(Max('flog_rate_confession'))['flog_rate_confession__max']
    min_rate_invite = player_result.aggregate(Min('flog_rate_invite'))['flog_rate_invite__min']
    min_rate_date = player_result.aggregate(Min('flog_rate_date'))['flog_rate_date__min']
    min_rate_confession = player_result.aggregate(Min('flog_rate_confession'))['flog_rate_confession__min']
    print(max_rate_invite)
    params = {
        'player_result': player_result,
        'username': username,
        'max_rate_invite': max_rate_invite,
        'max_rate_date': max_rate_date,
        'max_rate_confession': max_rate_confession,
        'min_rate_invite': min_rate_invite,
        'min_rate_date': min_rate_date,
        'min_rate_confession': min_rate_confession
    }
    return render(request, 'accounts/user_profile.html', params)


def user_edit_view(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        # password_form = PasswordChangeForm(request.user, request.POST)
        if user_form.is_valid():
            user_form.save()
            # password_form.save()
            # update_session_auth_hash(request, password_form.user)
            return redirect('accounts/user_profile')  # 更新後にプロフィールページにリダイレクト
    else:
        user_form = UserUpdateForm(instance=request.user)
        # password_form = PasswordChangeForm(request.user)

    context = {
        'user_form': user_form,
        # 'password_form': password_form,
    }
    return render(request, 'accounts/user_profile.html', context)

def logout_view(request):
    logout(request)
    return redirect('welcome:welcome')
