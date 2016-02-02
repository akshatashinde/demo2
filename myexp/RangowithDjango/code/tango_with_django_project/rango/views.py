from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	context_dict_index = {'boldmessage': "I am bold font from the context_dict_index"}
	return render(request, 'rango/index.html', context_dict_index)
def about(request):
	context_dict_about = {'boldmsg': "I am bold font from the context_dict_about"}
	return render(request, 'rango/about.html',context_dict_about)
