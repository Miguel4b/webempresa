from django.shortcuts import render, HttpResponse


# Create your views here.
def home(request):
	#return HttpResponse( 'Hola ')
	return render(request, "core/index.html",{})
