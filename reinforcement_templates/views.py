from django.http import HttpResponse
from django.shortcuts import render

def new_profile(request):
    form_to_fields = {"fancy_form": ["email", "username", "pin", "website", "address", "alias"]}
    context = {"forms": form_to_fields}
    return HttpResponse(render(request, 'profiles/new.html', context))
