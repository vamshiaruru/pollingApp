# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime

from django.utils import timezone
from django.test import TestCase
from .models import Questions, Choice


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
