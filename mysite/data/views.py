# Create your views here.
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import Http404
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from data.models import AMA1, AMA1Form

def AMA1(request):
	if request.method == 'POST':		
		form = AMA1Form(request.POST)		
		data = form.save()				
		response = HttpResponse("Saved!")		
		return response
	else:
		form = AMA1Form()
		return render(request, 'data/AMA1.html', {'form': form})
