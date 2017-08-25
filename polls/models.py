# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime
from django.utils import timezone
from django.db import models


class Questions(models.Model):
    """
    Each class here represents a table, and we define the various fields.
    """
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("Publication Date")

    def __str__(self):
        return self.question_text

    def was_recent(self):
        """
        Tells whether or not this question was published in the last day
        :return: True or False
        """
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


class Choice(models.Model):
    """
    Class to represent choice table. Has three fields, question, choice_text,
    and votes question acts as foreign key pointing to Questions table
    """
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
