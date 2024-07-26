from django.views.generic import TemplateView
from .models import Quiz, Player_result
from django.shortcuts import render

from django.contrib.auth import get_user_model


User = get_user_model()


def question_view(request):
    questions = Quiz.objects.all()
    params = {
            'user': request.user,
            'questions': questions,
        }
    return render(request, 'quiz/question.html', params)


def result_view(request):
    if request.method == 'POST':
        questions = Quiz.objects.all()
        score = 0
        correct = 0
        answered_num = 0
        player = request.user
        for q in questions:
            answered_num += 1
            print(request.POST.get(q.question))
            print(q.ans)
            if q.ans == request.POST.get(q.question):
                score += 0
                correct += 1
            elif q.op2 == request.POST.get(q.question):
                score += 1
            elif q.op3 == request.POST.get(q.question):
                score += 2
            elif q.op4 == request.POST.get(q.question):
                score += 3
        percent = score/(answered_num*3) * 100
        # Player_resultのデータを変数に格納
        player_result = Player_result.objects.create(user=player, flog_rate_invite=percent)
        print(Player_result.objects.all().values())
        # 変数にsave()メソッドを適用してデータベースに保存
        player_result.save()

        percent = player.player_result(percent)
        player.save()
        params = {
            'percent': percent,
            'answered_num': answered_num
        }
        return render(request, 'quiz/result.html', params)

    else:
        params = {
            'user': request.user,  
        }
        return render(request, 'quiz/question.html', params)


class HomeView(TemplateView):
    template_name = 'quiz/home.html'
