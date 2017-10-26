from django.conf.urls import url
from django.contrib import admin

from . import views

urlpatterns = [
# FORMS
	url(r'^$', views.logRegUserPage),
	url(r'^dashboard$', views.dashUserPage),

# USER ACTIONS
	url(r'^loginUser$', views.loginUser),
	url(r'^create$', views.createUser),
	url(r'^logout$', views.logout),
]