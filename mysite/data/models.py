from django.db import models
from django.forms import ModelForm
from datetime import datetime

# Create your models here.

class AMA1(models.Model):
	grievance_received_by = models.TextField()
	
