from django.shortcuts import render, redirect
from .models import Post, Like
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.http import JsonResponse

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'post/post_list.html', {'posts': posts})


@login_required
def create_post(request):
    if request.method == 'POST':
        post = Post(user=request.user, content=request.POST['content'])
        post.save()
        return redirect('post_list')
    return render(request, 'post/create.html')


def post_detail(request, pk):
    """日記の詳細ページの表示"""
    post = get_object_or_404(Post, pk=pk)
    like = Like.objects.filter(post=post, user=request.user)
    is_liked = like.exists()
    like_count = Like.objects.filter(post=post).count()

    context = {
        'post': post,
        'is_liked': is_liked,
        'like_count': like_count,
    }

    return render(request, 'detail.html', context)


def like_post(request):
    """日記のいいね処理"""
    post_pk = request.POST.get('post_pk')#POSTメソッドのbodyに格納されているpost_pkを取得
    post = get_object_or_404(Post, pk=post_pk)
    like = Like.objects.filter(post=post, user=request.user)
    context = {}
    if like.exists():
        like.delete()
        context['method'] = 'delete'
    else:
        like.create(post=post, user=request.user)
        context['method'] = 'create'
    #該当の投稿のいいねの数を取得
    context['like_count'] = Like.objects.filter(post=post).count()
    return JsonResponse(context)

