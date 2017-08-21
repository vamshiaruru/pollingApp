from django.http import HttpResponse
from .models import Questions, Choice
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
    response = "You are looking at the question {}".format(question)
    return HttpResponse(response)


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
    template = loader.get_template("last_viewed.html")
    context = {
        'latest_question_list': last_viewed_questions
    }
    return HttpResponse(template.render(context, request))


def vote(request, question):
    """
    for /poll/<question_id>/vote
    :param request: HttpRequest object
    :param question: question id
    :return: string with a little info
    """
    return HttpResponse("You are voting for question {}".format(question))

