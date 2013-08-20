from django.db import models
from django.forms import ModelForm
from datetime import datetime

# Create your models here.
class Data(models.Model):
	call = models.CharField(max_length=255, primary_key=True)
	project = models.CharField(max_length=500)
	agent = models.CharField(max_length=500)
	value = models.TextField()
	tags = models.TextField()
	phases = models.TextField()
	chars = models.TextField()
	created_date = models.DateTimeField('created', null=True, blank=True)

	def __unicode__(self):
		return self.call

	def clean_call(self, string):
		return string.replace(" ", "_")

	def save(self):
		print "**** SAVING HERE ****"
		self.call = self.clean_call(self.call)
		self.created_date = datetime.now()

		#creates the snapshot
		snapshot = Snapshot()
		snapshot.call = self.call
		snapshot.project = self.project
		snapshot.agent = self.agent
		snapshot.value = self.value
		snapshot.tags = self.tags
		snapshot.phases = self.phases
		snapshot.chars = self.chars
		snapshot.date = self.created_date
		snapshot.save()

		super(Data, self).save()
	
	def saveFromSnapshot(self, snapshot_id):
		self.call = self.clean_call(self.call)

		snapshot = Snapshot.objects.get(id=snapshot_id)
		self.project = snapshot.project
		self.agent = snapshot.agent
		self.value = snapshot.value
		self.tags = snapshot.tags
		self.phases = snapshot.phases
		self.chars = snapshot.chars
		self.created_date = snapshot.date #important - this is the snapshot's original date		

		super(Data, self).save()

	def get_absolute_url(self):
		return u"/data/%s/" % self.call

class DataForm(ModelForm):
    class Meta:
        model = Data	   

class Snapshot(models.Model):
        call = models.CharField(max_length=255)
        project = models.CharField(max_length=500)
        agent = models.CharField(max_length=500)
        value = models.TextField()
        tags = models.TextField()
        phases = models.TextField()
        chars = models.TextField()
        date = models.DateTimeField('created', null=True, blank=True)

        def __unicode__(self):
                return self.call

        def clean_call(self, string):
                return string.replace(" ", "_")

        def save(self):
                print "**** SAVING HERE ****"
                super(Snapshot, self).save()

        def get_absolute_url(self):
                return u"/snapshot/%s/" % self.id

class SnapshotForm(ModelForm):
    class Meta:
        model = Snapshot
