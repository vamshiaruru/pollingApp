from django.http import HttpResponse, HttpResponseRedirect
from .models import Questions, Choice
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic
from django.utils import timezone


class IndexView(generic.ListView):
    template_name = 'polls/last_viewed.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Questions.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Questions
    template_name = 'polls/results.html'

    def get_queryset(self):
        return Questions.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Questions
    template_name = 'polls/results.html'


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


def vote(request, question):
    """
    for /poll/<question_id>/vote
    :param request: HttpRequest object
    :param question: question id
    :return: string with a little info
    """
    question = get_object_or_404(Questions, pk=question)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        if 'voteButton' in request.POST:
            context = {
                'question': question,
                'error_message': "You didn't select a choice"
            }
            return render(request, 'polls/details.html', context)
        elif Choice.DoesNotExist:
            context = {
                'question': question,
             }
            return render(request, 'polls/details.html', context)
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Return a HttpResponseRedirect after succesfully dealing with POST Data.
        #  This prevents data from being posted
        # twice if a user hits the back button
        return HttpResponseRedirect(reverse('polls:results',
                                            args=(question.id,)))
