# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from ..loginReg_app.models import User


# Create your models here.
class AnalysisManager(models.Manager):
	def analysis_validator(self, postData):
		errors = {}
		if len(postData['name']) < 2:
			errors["shortFirst"] = "Name must be more than 2 characters long."
		if len(postData['client']) < 5:
			errors["shortClient"] = "Client number must be at least 5 characters long."
		if len(postData['project']) != 3:
			errors["shortProject"] = "Project name must be exactly 3 characters long."
		if len(postdata['lcSequence']) == 0:
			errors["shortLC"] = "Please enter Light Chain Sequence."
		if len(postdata['hcSequence']) == 0:
			errors["shortHC"] = "Please enter Heavy Chain Sequence."

	def createNewAnalysis(self, postData, request):
		newAnalysis = self.create(
			name = postData['name'],
			collectionDate=postData['collectionDate'],
			client=postData['client'],
			project=postData['project'],
			hcSequence=postData['hcSequence'],
			lcSequence=postData['lcSequence'],
			author=User.objects.get(id=request.session['currentUser'])
			)
		return newAnalysis

	def editAnalysis(self, postData, id):
		current = Analysis.objects.get(id=id)
		current.name = postData['name']
		current.collectionDate = postData['collectonDate']
		current.client = postData['client']
		current.project = postData['project']
		current.hcSequence = postData['hcSequence']
		current.lcSequence = postData['lcSequence']
		current.update()

class PeakManager(models.Manager):
	def createNewPeaks(self, postData):
		newPeaks = self.create(
			numOfPeaks=postData['numOfPeaks'],
			peak1=postData['peak1'],
			peak2=postData['peak2'],
			peak3=postData['peak3'],
			peak4=postData['peak4'],
			peak5=postData['peak5'],
			peak6=postData['peak6'],
			peak7=postData['peak7'],
			peak8=postData['peak8'],
			peak9=postData['peak9'],
			peak10=postData['peak10'],
			peak11=postData['peak11'],
			peak12=postData['peak12'],
			peak13=postData['peak13'],
			peak14=postData['peak14'],
			peak15=postData['peak15'],
			analysis=Analysis.objects.last()
		)
		return newPeaks

	def editPeaks(self, postData, id):
		current = Peak.objects.get(id=id)
		current.peak1 = postData['peak1']
		current.peak2 = postData['peak2']
		current.peak3 = postData['peak3']
		current.peak4 = postData['peak4']
		current.peak5 = postData['peak5']
		current.peak6 = postData['peak6']
		current.peak7 = postData['peak7']
		current.peak8 = postData['peak8']
		current.peak9 = postData['peak9']
		current.peak10 = postData['peak10']
		current.peak11 = postData['peak11']
		current.peak12 = postData['peak12']
		current.peak13 = postData['peak13']
		current.peak14 = postData['peak14']
		current.peak15 = postData['peak15']
		current.update()

class ModificationManager(models.Manager):
	def createNewModifications(self, postData):
		print(postData)
		# for item in postData:
		# 	print(item)
		# 	if (postData[item] == ):
		# 		postData[item] = "0"
		print(postData)
		newModifications = self.create(
			gZero=postData['gZero'],
			gZeroF=postData['gZeroF'],
			gOneF=postData['gOneF'],
			gTwoF=postData['gTwoF'],
			manFive=postData['manFive'],
			manSix=postData['manSix'],
			manSeven=postData['manSeven'],
			manEight=postData['manEight'],
			manNine=postData['manNine'],
			pyroQ=postData['pyroQ'],
			pyroE=postData['pyroE'],
			sodiumAdduct=postData['sodiumAdduct'],
			waterAdduct=postData['waterAdduct'],
			lysLoss=postData['lysLoss'],
			analysis=Analysis.objects.last()
			)
		return newModifications

	def editModifications(self, postData, id):
		current = Modifications.objects.get(id=id)
		current.gZero = postData['gZero']
		current.gZeroF = postData['gZeroF']
		current.gOneF = postData['gOneF']
		current.gTwoF = postData['gTwoF']
		current.manFive = postData['manFive']
		current.manSix = postData['manSix']
		current.manSeven = postData['manSeven']
		current.manEight = postData['manEight']
		current.manNine = postData['manNine']
		current.pyroQ = postData['pyroQ']
		current.pyroE = postData['pyroE']
		current.sodiumAdduct = postData['sodiumAdduct']
		current.waterAdduct = postData['waterAdduct']
		current.lysLoss = postData['lysLoss']
		current.update()

class Analysis(models.Model):
	name = models.CharField(max_length=255)
	collectionDate = models.DateField()
	client = models.IntegerField()
	project = models.CharField(max_length=3)
	hcSequence = models.CharField(max_length=1000)
	lcSequence = models.CharField(max_length=1000)
	author = models.ForeignKey(User, related_name="analysis")
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = AnalysisManager()

class Peak(models.Model):
	numOfPeaks = models.IntegerField()
	peak1 = models.IntegerField()
	peak2 = models.IntegerField()
	peak3 = models.IntegerField()
	peak4 = models.IntegerField()
	peak5 = models.IntegerField()
	peak6 = models.IntegerField()
	peak7 = models.IntegerField()
	peak8 = models.IntegerField()
	peak9 = models.IntegerField()
	peak10 = models.IntegerField()
	peak11 = models.IntegerField()
	peak12 = models.IntegerField()
	peak13 = models.IntegerField()
	peak14 = models.IntegerField()
	peak15 = models.IntegerField()
	analysis = models.OneToOneField(Analysis, related_name="peaks")
	objects = PeakManager()

class Modification(models.Model):
	gZero = models.IntegerField(null=True, blank=True)
	gZeroF = models.IntegerField(null=True, blank=True)
	gOneF = models.IntegerField(null=True, blank=True)
	gTwoF = models.IntegerField(null=True, blank=True)
	manFive = models.IntegerField(null=True, blank=True)
	manSix = models.IntegerField(null=True, blank=True)
	manSeven = models.IntegerField(null=True, blank=True)
	manEight = models.IntegerField(null=True, blank=True)
	manNine = models.IntegerField(null=True, blank=True)
	pyroQ = models.IntegerField(null=True, blank=True)
	pyroE = models.IntegerField(null=True, blank=True)
	lysLoss = models.IntegerField(null=True, blank=True)
	sodiumAdduct = models.IntegerField(null=True, blank=True)
	waterAdduct = models.IntegerField(null=True, blank=True)
	analysis = models.OneToOneField(Analysis, related_name="modifications")
	objects = ModificationManager()

class Calculation(models.Model):
	hcMass = models.IntegerField()
	lcMass = models.IntegerField()
