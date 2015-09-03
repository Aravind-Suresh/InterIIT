from django.shortcuts import render, render_to_response
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from interiit.models import Profile, Details
from interiit.forms import ProfileRegistrationForm
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.forms.formsets import formset_factory

from django.contrib.auth import authenticate, login

def login_view(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		#user = User.objects.get(username=username, password=password)
		user = User.objects.get(pk=1)
		print user
		if user is not None:
			#login(request, user)
			return HttpResponseRedirect('/profile/list/')
		else:
			return HttpResponseRedirect('/login/')
	else:
		return render(request, 'login.html', {})

def logout_view(request):
	logout(request)
	return HttpResponseRedirect('/login/')

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

def profile_edit(request):
	if request.method == 'POST':
		form = ProfileRegistrationForm(request.POST, request.FILES, instance=profile)
		if form.is_valid():
			form.save();
			return HttpResponseRedirect('/profile/list/')	
	else:
		profile = Profile.objects.get(pk=request.profile_id)
		form = ProfileRegistrationForm(request.POST, request.FILES, instance=profile)

	return render(request, 'register.html', {'form' : form , 'user' : request.user })

def profile_delete(request):
	Profile.objects.get(pk=request.profile_id).delete()
	profiles = Profile.objects.filter(user=request.user)
	return render(request, 'profileList.html', { 'profiles_list' : profiles })

def profile_list(request):
	if request.user is None:
		user = User.objects.get(pk=1)
	else:
		user = request.user
	profiles = Profile.objects.filter(user=user.pk)
	return render(request, 'profileList.html', { 'profiles_list' : profiles })