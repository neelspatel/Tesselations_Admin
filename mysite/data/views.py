# Create your views here.
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import Http404
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from data.models import AMA1, AMA1Form
import json

def newAMA1(request):
	if request.method == 'POST':		
		form = AMA1Form(request.POST)	

		#checks if it was an old existing form
		if form.is_valid() and ('has_existing_id' in form.cleaned_data):
			old = AMA1.objects.get(id=form.cleaned_data['has_existing_id'])
			form = AMA1Form(request.POST, instance = old)	
			data = form.save()				
			response = HttpResponse("Existing: " + json.dumps(form.cleaned_data))		
			return response
		else:
			data = form.save()				
			response = HttpResponse("New: " + json.dumps(form.cleaned_data))			
			return response
	else:
		form = AMA1Form()
		return render(request, 'data/AMA1.html', {'form': form})

def existingAMA1(request, data_id):
	current = AMA1.objects.get(id=data_id)
	form = AMA1Form(instance = current)
	return render(request, 'data/AMA1.html', {'form': form, 'has_existing_id': data_id})
