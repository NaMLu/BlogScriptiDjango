from django.shortcuts import render

# Create your views here.
def anasayfa(request):
	title = "Ana sayfa"
	
	return render(request, "anasayfa.html", locals())