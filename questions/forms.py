from django.contrib.auth.models import User
from questions.models import Company, Question, Answer
from django import forms

class DateInput(forms.DateInput):
    input_type = 'date'


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    username = forms.CharField(label='Email', widget=forms.EmailInput())

    class Meta:
        model = User
        fields = ('username', 'password', 'first_name', 'last_name')

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('title', 'content', 'interview_round', 'date')
        widgets = {
            'date': DateInput()
        }

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ('content',)

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ('name', 'location')
