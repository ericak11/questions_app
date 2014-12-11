from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __unicode__(self):              # __unicode__ on Python 2
        return self.name

class Question(models.Model):
    user = models.ForeignKey(User)
    company = models.ForeignKey(Company)
    title = models.CharField(max_length=200)
    content = models.TextField(max_length=2000)
    INTERVIEW_ROUND = (
        ('phone', 'Phone Interview'),
        ('code', 'Take Home Code Challenge'),
        ('inPerson', 'In Person Interview'),
    )
    date = models.DateField()
    interview_round = models.CharField(max_length=10, choices=INTERVIEW_ROUND)
    def __unicode__(self):              # __unicode__ on Python 2
        return self.title

class Answer(models.Model):
    question = models.ForeignKey(Question)
    content = models.TextField(max_length=2000)
    def __unicode__(self):              # __unicode__ on Python 2
        return self.question
