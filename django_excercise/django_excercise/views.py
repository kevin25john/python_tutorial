from django.shortcuts import render_to_response, RequestContext
from django_excercise.script import prime


def my_view(request):
    a=prime(1,10)
    b='string'
    c=10
    return render_to_response('index.html',locals(), context_instance=RequestContext(request))