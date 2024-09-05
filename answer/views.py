from django.shortcuts import render, redirect
from main import models


def getQuiz(request, id):
    quiz = models.Quiz.objects.get(id=id)
    return render(request, 'answer/get-quiz.html', {'quiz':quiz})


def quizDetail(request, id):
    quiz = models.Quiz.objects.get(id=id)
    return render(request, 'answer/quiz-detail.html', {'quiz': quiz})

def makeAnswer(request, id):
    quiz = models.Quiz.objects.get(id=id)
    answer = models.Answer.objects.create(quiz=quiz, author=request.user)
    for key, value in request.POST.items():
        if key.isdigit():
            models.AnswerDetail.objects.create(
                answer=answer, 
                question=models.Question.objects.get(id=int(key)), 
                user_choice=models.Option.objects.get(id=int(value)))
    return redirect('results')


def results(request):
    results = models.Answer.objects.filter(author=request.user)
    return render(request, 'answer/natijalar.html', {'result_list':results})


def result_detail(request, id):
    quiz = models.Quiz.objects.get(id=id)
    answer = models.Answer.objects.get(quiz=quiz, author=request.user)
    answers = models.AnswerDetail.objects.filter(answer=answer)
    return render(request, 'answer/natija-detail.html', {'result':answers})