# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import messages
from django.shortcuts import render, redirect
import bcrypt

from models import UserManager, User
from ..analysis_app.models import AnalysisManager, Analysis

# FORMS

def logRegUserPage(request):
	return render(request, 'loginReg_app/loginRegisterPage.html')

def dashUserPage(request):
	if 'currentUser' not in request.session:
		return render(request, 'loginReg_app/errorPage.html')
	else:
		context = {
			"user": User.objects.get(id=request.session['currentUser']),
			"analysis": Analysis.objects.all().order_by('-updated_at')[:5]
		}
		return render(request, 'loginReg_app/dashUserPage.html', context)

# USER ACTIONS

def loginUser(request):
	errors = User.objects.login_validator(request.POST, request)
	if len(errors):
		for tag, error in errors.iteritems():
			messages.error(request, error, extra_tags = tag)
		return redirect('/')
	else:
		if 'currentUser' not in request.session:
			request.session['currentUser'] = User.objects.get(email=request.POST['email']).id
			print("current user is " + str(request.session['currentUser']))
		return redirect('/dashboard')

def createUser(request):
	errors = User.objects.register_validator(request.POST)
	# Stop if errors exist
	if len(errors):
		for tag, error in errors.iteritems():
			messages.error(request, error, extra_tags = tag)
		return redirect('/')
	# Allow if no errors
	else:
		User.objects.createUser(request.POST, request)
		# create currentUser session variable
		if 'currentUser' not in request.session:
			request.session['currentUser'] = User.objects.last().id
			print(request.session['currentUser'])
		return redirect('/dashboard')

def logout(request):
	request.session.clear()
	return redirect('/')