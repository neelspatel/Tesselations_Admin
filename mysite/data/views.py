# Create your views here.
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import Http404
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import simplejson
from django.core import serializers
import csv
from StringIO import StringIO  
from zipfile import ZipFile  
from time import gmtime, strftime

@csrf_exempt
def getCSV(request, project_name):
	#first replaces underscores with spaces
	project_name = project_name.replace("_", " ")
	data = Data.objects.filter(project = project_name)
	
	in_memory = StringIO()  
	zip = ZipFile(in_memory, "a")  
          
	#first constructs the tags, beginning with the header
	header = data[0].tags
	header = header.splitlines(True)
	tags = str(header[0])
	for current in data:
		current_tags = str(current.tags)
		current_tags = current_tags.splitlines(True)
		#if there is a tag other than the header
		if len(current_tags) > 1:
			#appends all the non-header lines
			for i in range(len(current_tags) - 1):
				tags += str(current_tags[i + 1])

	zip.writestr("tags.csv", tags) 

	#next constructs the phases 
	header = data[0].phases
        header = header.splitlines(True)
        phases = str(header[0])
        for current in data:
                current_phases = str(current.phases)
                current_phases = current_phases.splitlines(True)
                #if there is a tag other than the header
                if len(current_phases) > 1:
                        #appends all the non-header lines
                        for i in range(len(current_phases) - 1):
                                phases += str(current_phases[i + 1])

        zip.writestr("phases.csv", phases)

	#finally constructs the attributes
	header = data[0].chars
        header = header.splitlines(True)
        chars = str(header[0])
        for current in data:
                current_chars = str(current.chars)
                current_chars = current_chars.splitlines(True)
                #if there is a tag other than the header
                if len(current_chars) > 1:
                        #appends all the non-header lines
                        for i in range(len(current_chars) - 1):
                                chars += str(current_chars[i + 1])
				chars += "\n"
				
        zip.writestr("chars.csv", chars)



	# fix for Linux zip files read in Windows  
	for file in zip.filelist:  
        	file.create_system = 0      
          
	zip.close()  
  
	response = HttpResponse(mimetype="application/zip")
	#EVENTUALLY: include timestamp
	type = "attachment; filename=CMS Data " + project_name + " " + strftime("%Y-%m-%d %H.%M.%S", gmtime())  + ".zip"  
	response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
        response["Access-Control-Max-Age"] = "1000"
        response["Access-Control-Allow-Headers"] = "*"
	response["Content-Disposition"] = type 
      
	in_memory.seek(0)      
	response.write(in_memory.read())  
      
	return response  

from boto.s3.connection import S3Connection

@csrf_exempt
def show(request):

	conn = S3Connection('AKIAIRXRKW4SYOFDYKSQ','o6tBp8DtA9dW3shBM1vKy0dlwVZcrssRleD53OO9')
	bucket = conn.get_bucket('datanautixcmstestproject')
	data = []
	for key in bucket.list():
		data.append({"name": key.name.encode('utf-8'), "url": key.generate_url(expires_in=43200).encode('utf-8')})

	return render(request, 'data/cmsdemo.html', {'data': data})

@csrf_exempt
def index(request):
	return HttpResponse("Hey, you're at the index for views in data")

@csrf_exempt
def detail(request, data_id):
	#try:
	#	#data_id is the call name, such as Sample_Call
	#	data = Data.objects.get(call=data_id)
	#except Data.DoesNotExist:
	#	raise Http404
	#return render(request, 'data/detail.html', {'data': data})
	#return HttpResponse("You're at call name %s." % data_id)
	#data_id is the call name, such as Sample_Call
	data = Data.objects.get(call=data_id)
	response = HttpResponse(serializers.serialize("json", [data]), mimetype='application/javascript')		
	response["Access-Control-Allow-Origin"] = "*"  
	response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"  
	response["Access-Control-Max-Age"] = "1000"  
	response["Access-Control-Allow-Headers"] = "*" 
	return response

@csrf_exempt
def snapshot_detail(request, data_id):
	snapshot = Snapshot.objects.get(id=data_id)
	response = HttpResponse(serializers.serialize("json", [snapshot]), mimetype='application/javascript')
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
        response["Access-Control-Max-Age"] = "1000"
        response["Access-Control-Allow-Headers"] = "*"
        return response

def timemachine(request, data_id):
	data = Data.objects.get(call=data_id)
	snapshots = Snapshot.objects.filter(call=data_id)
	if len(snapshots) == 0:
		return HttpResponse("Sorry, no snapshots found for " + data_id)
	else:
		#for each snapshot, get the details, and pass in the data to a template
		return render(request, 'data/timemachine.html', {'snapshots': snapshots, 'call': data_id, 'data':data})


@csrf_exempt
def new(request):
	print "in here"
	return render(request, 'data/new.html')
#	return HttpResponse("in here")

@csrf_exempt
def create(request):
	if request.method == 'POST':
		try:
			old = Data.objects.get(pk=request.POST['call'])
			form = DataForm(request.POST, instance = old)		
		except Data.DoesNotExist:
			form = DataForm(request.POST)		
		data = form.save()		
		print "\n\n" + serializers.serialize("json", [data]) + "\n\n"
		response = HttpResponse(serializers.serialize("json", [data]), mimetype='application/javascript')		
		response["Access-Control-Allow-Origin"] = "*"  
		response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"  
		response["Access-Control-Max-Age"] = "1000"  
		response["Access-Control-Allow-Headers"] = "*" 
		return response
