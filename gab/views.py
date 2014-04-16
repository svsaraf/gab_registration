from gab.forms import UserForm, UserProfileForm
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from gab.models import UserProfile
from django.contrib import messages


def index(request):
	context = RequestContext(request)

	return render_to_response(
		'gab/index.html',
		{},
		context)

def user_logout(request):
	logout(request)
	return HttpResponseRedirect('/')

def user_login(request):
	context = RequestContext(request)

	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']

		user = authenticate(username=username, password=password)

		if user is not None:
			if user.is_active:
				profile = UserProfile.objects.get(user=user)
				if profile.verified:
					login(request, user)
					login_message = ""
					return HttpResponseRedirect('/')
				else:
					logout(request)
					login_message = "Profile is not verified! Check your email!"
					return render_to_response('gab/register.html', {'login_message': login_message}, context)
			else:
				return HttpResponse("Your account is disabled.")
		else:
			print "Invalid login details: {0}, {1}".format(username, password)
			return HttpResponse("Invalid login details supplied")
	else: 
		return render_to_response('gab/register.html', {}, context)

def register(request):
	context = RequestContext(request)

	registered = False

	if request.method == 'POST':
		user_form = UserForm(data=request.POST)
		profile_form = UserProfileForm(data=request.POST)

		if user_form.is_valid() and profile_form.is_valid():
			user = user_form.save()
			user.username = user.email
			# print user.first_name

			user.set_password(user.password)
			user.save()

			profile = profile_form.save(commit=False)
			profile.user = user

			profile.save()

			registered = True

			return render_to_response('gab/verification.html',
				{'registered':registered}, context)
		else:
			print user_form.errors, profile_form.errors
	else:
		user_form = UserForm()
		profile_form = UserProfileForm()

	return render_to_response(
			'gab/register.html',
			{'user_form': user_form, 'profile_form': profile_form, 'registered': registered},
			context)

# Create your views here.
