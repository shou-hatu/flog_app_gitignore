from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DeleteView, DetailView, ListView
from django.views.generic.edit import CreateView
from .models import Post, Like
from django.http import JsonResponse

class HomeView(LoginRequiredMixin, ListView):
    template_name = "Posts/home.html"
    # Postをモデルに指定
    model = Post
    # select_relatedを用いることで発行されたクエリによってユーザー情報とツイート情報がidをキーとして結合された状態のレコードが返ってくる
    # そのため{{Post.user}}{{Post.content}},{{Post.created_at}}で再度クエリを発行する必要がなくなり、N+1問題を解決できる
    queryset = Post.objects.select_related("user")


class PostCreateView(LoginRequiredMixin, CreateView):
    template_name = "Posts/create.html"
    # Postモデルを指定
    model = Post
    # contentのみ表示
    fields = ['content']
    success_url = reverse_lazy('Posts:home')

    def form_valid(self, form):
        # フォームがエラーなく送信された際に発動するメソッド
        # データの受取・保存の役割を担う
        # self.request.userログインしているユーザー
        # form.instance.user：フォームを送ったユーザー
        # フォームを送ったユーザー情報にツイートボタンを押したユーザーを格納
        form.instance.user = self.request.user
        # super().で継承することでform_validのもともとの機能も保つ
        return super().form_valid(form)


class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post
    template_name = 'Posts/detail.html'
    queryset = Post.objects.select_related("user")


class PostDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'Posts/delete.html'
    model = Post
    success_url = reverse_lazy("Posts:home")