# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from models import AnalysisManager, Analysis, PeakManager, Peak, ModificationManager, Modification, Calculation

# FORMS
def analysisShowAllPage(request):
	context = {
		"analysis": Analysis.objects.filter(author=request.session['currentUser'])
	}
	return render(request, 'analysis_app/analysisShowAllPage.html', context)

def analysisNewPage(request):
	return render(request, 'analysis_app/analysisNewPage.html')

def analysisEditPage(request, id):
	context = {
		"analysis": Analysis.objects.get(id=id),
		"peaks": Peak.objects.get(id=id),
		"modifications": Modification.objects.get(id=id)
	}
	return render(request, 'analysis_app/analysisEditPage.html', context)

def analysisResultsPage(request, id):
	context = {
		"analysis": Analysis.objects.get(id=id),
		"peaks": Peak.objects.get(analysis=id),
		"modifications": Modification.objects.get(analysis=id)
	}

	return render(request, 'analysis_app/analysisResultsPage.html', context)

# ACTIONS

def createAnalysisModels(request):
	Analysis.objects.createNewAnalysis(request.POST, request)
	Peak.objects.createNewPeaks(request.POST)
	Modification.objects.createNewModifications(request.POST)
	return redirect('/analysis/showAll')

def editAnalysisModels(request):
	Analysis.objects.editAnalysis(request.POST)
	Peak.objects.editPeaks(request.POST)
	Modification.objects.editModifications(request.POST)
	return redirect('/analysis/showAll')