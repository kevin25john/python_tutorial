from django.shortcuts import render,render_to_response, RequestContext
from django.contrib import messages

from .forms import SignupForm

def home(request):
    form = SignupForm(request.POST or None)
    if request.method=="POST":
        if form.is_valid():
            human = True
            save_it= form.save(commit=False)
            save_it.save()
            messages.success(request,"Thankyou for registering!")
        else:
            form = SignupForm(request.POST or None)
            messages.error(request,"Uhoh! Correct the errors below.") 
    else:
        form = SignupForm(request.POST or None)    
    
    # Render page
    return render_to_response("signupform.html", locals(), context_instance=RequestContext(request))
    return render(request, "signupform.html")