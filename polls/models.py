# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Questions(models.Model):
    """
    Each class here represents a table, and we define the various fields.
    """
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("Publication Date")


class Choice(models.Model):
    """
    Class to represent choice table. Has three fields, question, choice_text, and votes
    question acts as foreign key pointing to Questions table
    """
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
