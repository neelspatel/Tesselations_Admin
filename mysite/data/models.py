from django.db import models
from django.forms import ModelForm
from datetime import datetime
from django import forms


# Create your models here.
grievance_categories = (
    ('Compensation', 'Compensation'),
    ('Land', 'Land'),
    ('Accident/Damage', 'Accident/Damage'),
    ('Environmental', 'Environmental'),
    ('Health', 'Health'),
    ('Safety/Security', 'Safety/Security'),
    ('Behavior/Conduct', 'Behavior/Conduct'),
    ('Misinformation', 'Misinformation'),
    ('Recruitment', 'Recruitment'),
    ('Other', 'Other'),    
)

entities = (
	('Project', 'Project'),
	('Contractor', 'Contractor'),
	('Government', 'Government'),
	('Other', 'Other'),
)

class JQueryUIDatepickerWidget(forms.DateInput):
    def __init__(self, **kwargs):
        super(forms.DateInput, self).__init__(attrs={"size":10, "class": "dateinput"}, **kwargs)

class AMA1(models.Model):
	grievance_received_by = models.TextField(null=True, blank=True)
	date_of_recording = models.TextField(null=True, blank=True)
	name_and_id_of_person_with_grievance = models.TextField(null=True, blank=True)
	contact_details = models.TextField(null=True, blank=True)
	location = models.TextField(null=True, blank=True)
	prod_zone = models.TextField(null=True, blank=True)
	alleged_grievance = models.TextField(null=True, blank=True)
	what_happened = models.TextField(null=True, blank=True)
	when = models.TextField(null=True, blank=True)
	where = models.TextField(null=True, blank=True)
	who = models.TextField(null=True, blank=True)
	observations = models.TextField(null=True, blank=True)
	grievance_category = forms.ChoiceField(grievance_categories)
	additional_documents = models.TextField(null=True, blank=True)
	has_grievance_been_raised_before = models.TextField(null=True, blank=True)
	proposed_solutions_according_to_complainer = models.TextField(null=True, blank=True)
	entity_involved = forms.ChoiceField(entities)
	name_of_supervisor = models.TextField(null=True, blank=True)
	comments_from_contacted_person = models.TextField(null=True, blank=True)
	follow_up_actions = models.TextField(null=True, blank=True)
	response_details = models.TextField(null=True, blank=True)
	grievance_resolution_responsibility = models.TextField(null=True, blank=True)
	date_of_response = models.TextField(null=True, blank=True)
	data_created_date = models.DateTimeField('Entry created:', null=True, blank=True)

	def save(self):
		self.data_created_date = datetime.now()
		super(AMA1, self).save()

class AMA1Form(ModelForm):
	class Meta:
		model = AMA1
		exclude = ['data_created_date']

