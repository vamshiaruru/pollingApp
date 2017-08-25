# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime

from django.utils import timezone
from django.test import TestCase
from .models import Questions
from django.urls import reverse


def create_question(question_text, days):
    """
    Create a question with the given question_text and published the given
    number of days offset to now. negative for past, positive for future
    """
    time = timezone.now() + datetime.timedelta(days=days)
    return Questions.objects.create(question_text=question_text, pub_date=time)


class QuestionsModelTests(TestCase):

    def test_was_recent_with_future_question(self):
        """
        Was_recent must return false for questions whose pub_date is in future
        :return: Bool, True or False
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Questions(pub_date=time)
        self.assertIs(future_question.was_recent(), False)

    def test_was_recent_with_recent_question(self):
        """
        Was_recent must return true for questions whose pub_date is within in
        last day
        :return: Bool True or False
        """
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59,
                                                   seconds=59)
        recent_question = Questions(pub_date=time)
        self.assertIs(recent_question.was_recent(), True)

    def test_was_recent_with_old_question(self):
        """
        For an old question with more than one day, this must return False
        :return: Bool True or False
        """
        time = timezone.now() - timezone.timedelta(days=1, seconds=1)
        old_question = Questions(pub_date=time)
        self.assertIs(old_question.was_recent(), False)


class QuestionIndexViwTests(TestCase):
    def test_no_questions(self):
        """
        If no Questions exist, appropriate Error message must be displayed.
        """
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available")
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    def test_past_question(self):
        """
        Past pub_date must be displayed
        """
        create_question(question_text='past test question', days=-30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(response.context['latest_question_list'],
                                 ['<Questions: past test question>'])

    def test_future_question(self):
        """
        future pub_date shouldn't be displayed
        """
        create_question(question_text='past test question', days=+30)
        response = self.client.get(reverse('polls:index'))
        self.assertContains(response, "No polls are available")
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    def test_future_question_and_past_question(self):
        """
        Even if both past and future questions exist, only past questions
        are displayed.
        """
        create_question(question_text="Past question.", days=-30)
        create_question(question_text="Future question.", days=30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            ['<Questions: Past question.>']
        )

    def test_two_past_questions(self):
        """
        The questions index page may display multiple questions.
        """
        create_question(question_text="Past question 1.", days=-30)
        create_question(question_text="Past question 2.", days=-5)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            ['<Questions: Past question 2.>', '<Questions: Past question 1.>']
        )


class QuestionsDetialViewTests(TestCase):
    def test_future_question(self):
        """
        when searching for a question in future, return must be a 404 not found.
        """
        future_question = create_question(question_text='dummy_test', days=5)
        url = reverse('polls:detail', args=(future_question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_past_question(self):
        """
        for past questions, detail view must display details.
        """
        past_quesiton = create_question(question_text='dummy_test', days=-5)
        url = reverse('polls:detail', args=(past_quesiton.id,))
        response = self.client.get(url)
        self.assertContains(response, past_quesiton.question_text)
