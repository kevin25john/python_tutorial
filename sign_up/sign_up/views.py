from django.shortcuts import render,render_to_response, RequestContext
from django.contrib import messages


def home(request):
    # Render page
    return render_to_response("index.html", locals(), context_instance=RequestContext(request))
    return render(request, "index.html")
    