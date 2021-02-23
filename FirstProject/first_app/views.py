from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import User
from . import forms

# imports to handle login
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout


# Create your views here.

def user_login(request):

    if request.method == 'POST':
        # we need to use the get() method because the form created in the
        # html template with the name='username'
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse('Account not active!')
        else:
            return  HttpResponse('Invalid login data provided!')

    else:
        return render(request, 'first_app/login.html', {})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

@login_required
def special(request):
    return HttpResponse("You're logged in, nice!")

def signup(request):

    signedup = False

    if request.method == 'POST':
        signup_form = forms.SignupForm(data=request.POST)
        profile_form = forms.UserProfileInfoForm(data=request.POST)

        if signup_form.is_valid() and profile_form.is_valid():
            user = signup_form.save()
            # hash the password
            user.set_password(user.password)
            user.save()

            # commit = False to avoid saving- first need to make ensure other user attributes match
            profile = profile_form.save(commit=False)
            profile.user = user

            # handle the uploaded files
            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            signedup = True
        else:
            print(signup_form.errors, profile_form.errors)

    else:
        # if the request was not post, that is user has not submitted anything, in that case set up the forms
        signup_form = forms.SignupForm()
        profile_form = forms.UserProfileInfoForm()

    return render(request, 'first_app/signup.html',
                            {'signup_form':signup_form,
                             'profile_form': profile_form,
                             'signedup': signedup})



def second(request):
    seconddict = {'insert_from_second': "This is the second page under first page!"}
    return render(request, 'first_app/second.html', context=seconddict)

def first(request):
    return HttpResponse("This is the first page! Home page of first_app")

def index(request):
    dict = {'insert_1': "This is the home page. Hello World!",
            'insert_2': "Please go to /user to review the data."}
    return render(request, 'first_app/index.html', context=dict)

def user(request):
    user_list = User.objects.all()
    user_dict = {'access_users' : user_list}
    return render(request, 'first_app/user.html', context=user_dict)

def form_name_view(request):
    form = forms.FormName()

    if request.method == 'POST':
        form = forms.FormName(request.POST)

        if form.is_valid():
            # DO SOMETHING CODE
            form.save(commit=True)
            form = forms.FormName()

    return render(request, 'first_app/form_page.html', context={'form':form})
