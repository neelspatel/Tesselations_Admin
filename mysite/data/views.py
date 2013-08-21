# Create your views here.
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import Http404
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from data.models import AMA1, AMA1Form
import json

def main(request):	

	return render(request, 'data/view.html', {})

def list(request):
	existing = AMA1.objects.all()

	return render(request, 'data/list.html', {'list': existing})


def newAMA1(request):	
	form = AMA1Form()
	return render(request, 'data/AMA1.html', {'form': form})

def saveAMA1(request):
	if request.method == 'POST':		
		form = AMA1Form(request.POST)	

		#checks if it was an old existing form
		if form.is_valid() and form.cleaned_data['has_existing_id']:
			old = AMA1.objects.get(id=form.cleaned_data['has_existing_id'])
			form = AMA1Form(request.POST, instance = old)	
			data = form.save()				
			response = HttpResponse("Saved")
			return response
		else:
			data = form.save()				
			response = HttpResponse(data.id)		
			return response		

def existingAMA1(request, data_id):
	current = AMA1.objects.get(id=data_id)
	form = AMA1Form(instance = current)
	return render(request, 'data/AMA1.html', {'form': form, 'has_existing_id': data_id})
