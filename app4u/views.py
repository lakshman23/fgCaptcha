from app4u.forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect,HttpResponse
from django.template import RequestContext


# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse

from app4u.models import Images_Real,Images_Fake

from app4u.forms import RealForm,FakeForm

def list(request):
    # Handle file upload
    if request.method == 'POST':
        form = RealForm(request.POST, request.FILES)

        if form.is_valid():
            newdoc = Images_Real(real = request.FILES['real_image'])
            newdoc.save()

            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('list'))
    else:
        form = RealForm() # A empty, unbound form

    # Load documents for the list page
    documents = Images_Real.objects.all()

    # Render list page with the documents and the form
    return render_to_response(
        'app4u/list.html',
        {'documents': documents, 'form': form},
        context_instance=RequestContext(request)
    )

def list1(request):
    # Handle file upload
    if request.method == 'POST':
        form = FakeForm(request.POST, request.FILES)

        if form.is_valid():
            newdoc = Images_Fake(fake = request.FILES['fake_image'])
            newdoc.save()

            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('list'))
    else:
        form = FakeForm() # A empty, unbound form

    # Load documents for the list page
    documents = Images_Fake.objects.all()

    # Render list page with the documents and the form
    return render_to_response(
        'app4u/list1.html',
        {'documents': documents, 'form': form},
        context_instance=RequestContext(request)
    )

def listprint(request):
    # if request.method == 'POST':
    form = FakeForm(request.POST, request.FILES)
    form1 = RealForm(request.POST, request.FILES)

    documents = Images_Fake.objects.all() 
    documents1 = Images_Real.objects.all() 

    # Render list page with the documents and the form
    return render_to_response(
        'app4u/printlist.html',
        {'documents': documents, 'form': form,'documents1': documents1, 'form1': form1},
        context_instance=RequestContext(request)
    )

def index(request):
    return render_to_response('app4u/index.html')

 
@csrf_protect
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password1'],
            email=form.cleaned_data['email']
            )
            return HttpResponseRedirect('/register/success/')
    else:
        form = RegistrationForm()
    variables = RequestContext(request, {
    'form': form
    })
 
    return render_to_response(
    'registration/register.html',
    variables,
    )
def main(request) :
    return render_to_response('registration/home.html')

def register_success(request):
    return render_to_response(
    'registration/success.html',
    )

def admin_loginn(request):
    return render_to_response(
    'registration/admin_login.html',
    )

def user_loginn(request):
    return render_to_response(
    'registration/user_login.html',
    )
def select(request):
    return render_to_response(
    'registration/select.html',
    )    
 
def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')
 
@login_required
def home(request):
    return render_to_response(
    'home.html',
    { 'user': request.user }
    )

def homey(request):
    return render_to_response(
    'registration/homey.html',
    )
