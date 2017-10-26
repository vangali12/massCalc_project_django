from django.contrib import admin
from django.conf.urls import url

from . import views

urlpatterns = [

# FORMS
	url(r'^showAll$', views.analysisShowAllPage),
	url(r'^new$', views.analysisNewPage),
	url(r'^edit/(?P<id>\d+)$', views.analysisEditPage),
	url(r'^results/(?P<id>\d+)$', views.analysisResultsPage),

# ACTIONS
	url(r'^createAnalysis$', views.createAnalysisModels),
	url(r'^editAnalysis$', views.editAnalysisModels),
]