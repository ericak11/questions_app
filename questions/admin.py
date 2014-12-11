from django.contrib import admin
from questions.models import Question
from questions.models import Company
from questions.models import Answer


# Register your models here.
admin.site.register(Question)
admin.site.register(Company)
admin.site.register(Answer)
