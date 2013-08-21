# Create your views here.
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import Http404
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from data.models import AMA1, AMA1Form

def newAMA1(request):
	if request.method == 'POST':		
		form = AMA1Form(request.POST)	

		#checks if it was an old existing form
		if form.is_valid() and ('has_existing_id' in form.cleaned_data):
			data = form.save()				
			response = HttpResponse("Saved, it already existed!")		
			return response
		else:
			data = form.save()				
			response = HttpResponse("Saved!")		
			return response
	else:
		form = AMA1Form()
		return render(request, 'data/AMA1.html', {'form': form})

def existingAMA1(request, data_id):
	current = AMA1.objects.get(id=data_id)
	form = AMA1Form(instance = current)
	return render(request, 'data/AMA1.html', {'form': form})
