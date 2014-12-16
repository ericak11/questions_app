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
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render(request, 'register/login.html', {})



def register(request):
    # Like before, get the request's context.
    context = RequestContext(request)

    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        user_form = UserForm(data=request.POST)
        # If the two forms are valid...
        if user_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()

            # Update our variable to tell the template registration was successful.
            registered = True

        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            print user_form.errors

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = UserForm()

    # Render the template depending on the context.
    return render(request, 'register/register.html', {
            'user_form': user_form, 'registered': registered})

@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)

    # Take the user back to the homepage.
    return HttpResponseRedirect('/')

@login_required
def companys(request):
    company_list = Company.objects.all()
    context_dict = {'companys': company_list}
    return render(request, 'company/index.html', context_dict)

@login_required
def add_question(request, pk):
    # Like before, get the request's context.
    context = RequestContext(request)
    registered = False
    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        question_form = QuestionForm(data=request.POST, initial={'user': request.user, 'company': pk})
        # If the two forms are valid...
        if question_form.is_valid():
            # Save the user's form data to the database.
            question_form.instance.user = request.user
            question_form.instance.company = Company.objects.get(id=pk)
            question_form.save()


            # Update our variable to tell the template registration was successful.
            registered = True

        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            print question_form.errors

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        question_form = QuestionForm()

    # Render the template depending on the context.
    return render(request, 'question/new.html', {
            'question_form': question_form, 'registered': registered})

@login_required
def add_answer(request, pk):
    # Like before, get the request's context.
    context = RequestContext(request)
    registered = False
    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        answer_form = AnswerForm(data=request.POST, initial={'user': request.user, 'question': pk})
        # If the two forms are valid...
        if answer_form.is_valid():
            # Save the user's form data to the database.
            answer_form.instance.user = request.user
            answer_form.instance.question = Question.objects.get(id=pk)
            answer_form.save()


            # Update our variable to tell the template registration was successful.
            registered = True

        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            print answer_form.errors

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        answer_form = AnswerForm()

    # Render the template depending on the context.
    return render(request, 'answer/new.html', {
            'answer_form': answer_form, 'registered': registered, 'question': Question.objects.get(id=pk) })

@login_required
def add_company(request):
    # Like before, get the request's context.
    context = RequestContext(request)
    registered = False
    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        company_form = CompanyForm(data=request.POST, initial={'user': request.user})
        # If the two forms are valid...
        if company_form.is_valid():
            # Save the user's form data to the database.
            company_form.instance.user = request.user
            company_form.save()


            # Update our variable to tell the template registration was successful.
            registered = True

        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            print company_form.errors

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        company_form = CompanyForm()

    # Render the template depending on the context.
    return render(request, 'company/new.html', {
            'company_form': company_form, 'registered': registered})
