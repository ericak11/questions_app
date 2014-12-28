from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from questions.forms import UserForm, QuestionForm, AnswerForm, CompanyForm
from django.template import RequestContext
from django.shortcuts import get_object_or_404, render, render_to_response
from IPython import embed
from django.contrib.auth.decorators import login_required
from questions.models import Company, Question, Answer
from django.core.urlresolvers import reverse
from django.views import generic
from django.views.generic import DetailView

class CompanyDetailView(generic.DetailView):
    model = Company
    template_name = 'company/detail.html'

class QuestionDetailView(generic.DetailView):
    model = Question
    template_name = 'question/detail.html'


def user_login(request):
    # Like before, obtain the context for the user's request.
    context = RequestContext(request)

    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
        username = request.POST['username']
        password = request.POST['password']

        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)
        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)
                return HttpResponseRedirect('/questions/companys')
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your questions account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            print "Invalid login details: {0}, {1}".format(email, password)
            return HttpResponse("Invalid login details supplied.")

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        if request.user.is_authenticated():
            return HttpResponseRedirect('/questions/companys')
        else:
            return render(request, 'register/login.html', {})



def register(request):
    context = RequestContext(request)
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            registered = True
        else:
            print user_form.errors
    else:
        user_form = UserForm()
    return render(request, 'register/register.html', {
            'user_form': user_form, 'registered': registered})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')

@login_required
def companys(request):
    company_list = Company.objects.all()
    context_dict = {'companys': company_list}
    return render(request, 'company/index.html', context_dict)

@login_required
def add_question(request, pk):
    context = RequestContext(request)
    registered = False
    if request.method == 'POST':
        question_form = QuestionForm(data=request.POST, initial={'user': request.user, 'company': pk})
        if question_form.is_valid():
            question_form.instance.user = request.user
            question_form.instance.company = Company.objects.get(id=pk)
            question_form.save()
            registered = True
        else:
            print question_form.errors
    else:
        question_form = QuestionForm()
    return render(request, 'question/new.html', {
            'question_form': question_form, 'registered': registered})

@login_required
def add_answer(request, pk):
    context = RequestContext(request)
    registered = False
    if request.method == 'POST':
        answer_form = AnswerForm(data=request.POST, initial={'user': request.user, 'question': pk})
        if answer_form.is_valid():
            answer_form.instance.user = request.user
            answer_form.instance.question = Question.objects.get(id=pk)
            answer_form.save()
            registered = True
        else:
            print answer_form.errors
    else:
        answer_form = AnswerForm()
    return render(request, 'answer/new.html', {
            'answer_form': answer_form, 'registered': registered, 'question': Question.objects.get(id=pk) })

@login_required
def add_company(request):
    context = RequestContext(request)
    registered = False
    if request.method == 'POST':
        company_form = CompanyForm(data=request.POST, initial={'user': request.user})
        if company_form.is_valid():
            company_form.instance.user = request.user
            company_form.save()
            registered = True
        else:
            print company_form.errors
    else:
        company_form = CompanyForm()
    return render(request, 'company/new.html', {
            'company_form': company_form, 'registered': registered})
