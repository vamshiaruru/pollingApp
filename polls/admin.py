# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Questions, Choice


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'pub_date', 'was_recent')
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']})
    ]
    # The order is defined by the order in which we put the fieldsets. In this
    #  case field containing question text appears first. The first element in
    #  each tuple is the title of field set. We Can use the following instead
    # too.
    # fields = ['pub_date', 'question_text']
    # The order in the fields array is the same order with which these fields
    # appear in the admin site.
    # or we can create field sets
    inlines = [ChoiceInline]

admin.site.register(Questions, QuestionAdmin)
