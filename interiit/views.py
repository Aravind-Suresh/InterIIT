from django.shortcuts import render, render_to_response
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from interiit.models import Profile, Details
from interiit.forms import ProfileRegistrationForm
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.forms.formsets import formset_factory

#@login_required
def profile_register(request):
	if request.method == 'POST':
		form = ProfileRegistrationForm(request.POST, request.FILES)
		if form.is_valid():
			context = {}
			return HttpResponseRedirect('/register/success/')
	
	else:
		form = ProfileRegistrationForm()

	return render(request, 'register.html', {'form' : form , 'user' : request.user })

def profile_register_success(request):
	return render(request, 'registrationSuccess.html', {})