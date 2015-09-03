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
		user = User.objects.get(username=username, password=password)
		user.backend = 'django.contrib.auth.backends.ModelBackend'
		print user
		if user is not None:
			login(request, user)
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
			post = form.save(commit=False)
			post.user_id = request.user.pk
			post.save()
			return HttpResponseRedirect('/register/success/')
	
	else:
		form = ProfileRegistrationForm()

	return render(request, 'register.html', {'form' : form , 'user' : request.user })

def profile_register_success(request):
	return render(request, 'registrationSuccess.html', {})

def profile_edit(request, profile_id):
	if request.method == 'POST':
		form = ProfileRegistrationForm(request.POST, request.FILES)
		if form.is_valid():
			post = form.save(commit=False)
			post.user_id = request.user.pk
			post.save()
			return HttpResponseRedirect('/profile/list/')	
	else:
		profile = Profile.objects.get(pk=profile_id)
		print profile
		form = ProfileRegistrationForm(request.POST, request.FILES, instance=profile)

	return render(request, 'register.html', {'form' : form , 'user' : request.user })

def profile_delete(request):
	Profile.objects.get(pk=request.profile_id).delete()
	profiles = Profile.objects.filter(user=request.user)
	return render(request, 'profileList.html', { 'profiles_list' : profiles })

def profile_list(request):
	user = request.user
	profiles = Profile.objects.filter(user_id=user.pk)
	print profiles
	return render(request, 'profileList.html', { 'profiles_list' : profiles })