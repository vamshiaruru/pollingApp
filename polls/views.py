from django.http import HttpResponse
from .models import Questions, Choice
from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.template import loader


def index(request):
    """
    Welcome message for /poll
    :param request: HttpRequest Object
    :return: welcome string
    """
    return HttpResponse("Hello, world. You're at the polls index.")


def home(request):
    """
    Welcome message for home i.e /<emptystring>
    :param request: HttpRequest Object
    :return: welcome string
    """
    return HttpResponse("Welcome to your Django project")


def detail(request, question):
    """
    for /poll/<question_id>
    :param request: HttpRequest object
    :param question: question id
    :return: string with a little info
    """
    # try:
    #     q = Questions.objects.get(pk=question)
    #     response = "You are looking at the question {}".format(q.question_text)
    # except Questions.DoesNotExist:
    #     raise Http404("question does not exist")
    # return HttpResponse(response)
    q = get_object_or_404(Questions, pk=question)
    # There's also a get_list_or_404() function, which works just as get_object_or_404() - except using filter()
    #  instead of get(). It raises Http404 if the list is empty.
    return HttpResponse(render(request, 'polls/details.html', {'q':q}))


def results(request, question):
    """
    for /poll/<question_id>/results
    :param request: HttpRequest object
    :param question: question id
    :return: string with a little info
    """
    response = "You are looking at results of the question, {}".format(question)
    return HttpResponse(response)


def last_viewed(request):
    """
    for /poll/lastViewed
    :param request: HttpRequest object
    :return: string of last 5 questions, sorted in pub order
    """
    last_viewed_questions = Questions.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list': last_viewed_questions
    }
    # template = loader.get_template("last_viewed.html")
    # return HttpResponse(template.render(context, request))
    return render(request, 'polls/last_viewed.html', context)


def vote(request, question):
    """
    for /poll/<question_id>/vote
    :param request: HttpRequest object
    :param question: question id
    :return: string with a little info
    """
    return HttpResponse("You are voting for question {}".format(question))

