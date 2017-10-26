# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import re
import bcrypt

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
	def createUser(self, postData, request):
		hash1 = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
		newUser = self.create(
			first_name = postData['first_name'],
			last_name = postData['last_name'],
			company = postData['company'],
			email = postData['email'],
			password = hash1,
		)
		return newUser

	def register_validator(self, postData):
		errors={}
		if len(postData['first_name']) < 2:
			errors["shortFirst"] = "First name must be more than 2 charactes long."
		if len(postData['last_name']) < 2:
			errors["shortLast"] = "Last name must be more than 2 characters long."
		if not EMAIL_REGEX.match(postData['email']):
			errors["emailformat"] = "Email format must be _____@___.com"
		if (User.objects.filter(email=postData['email'])):
			errors["exists"] = "This email already exists in our database. Please enter a different email or login below."
		if (postData['password'] != postData['confPassword']):
			errors["noMatch"] = "Your password does not match. Please try again."
		return errors
	def login_validator(self, postData, request):
		errors={}
		if not (User.objects.filter(email=postData['email'])):
			errors["doesntexists"] = "This email does not exist in our database. Please register above."
		elif bcrypt.checkpw(postData['password'].encode(), User.objects.get(email=postData['email']).password.encode()) == False:
			errors['wrongPassword'] = "Incorrect Password. Please try again."
		if ('currentUser' in request.session):
			errors["loggedIn"] = "Someone is already logged in. Please log out before trying to log in."
		return errors

class User(models.Model):
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	email = models.CharField(max_length=255)
	password = models.CharField(max_length=255)
	company = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = UserManager()
