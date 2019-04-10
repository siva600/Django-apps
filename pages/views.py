from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home_view(request, *args, **kwargs):
    return render(request, 'home.html', {})


def contact_view(request, *args, **kwargs):
    return render(request, 'contact.html', {})


def about_view(request, *args, **kwargs):
    my_context = {
        "title": "this is about us",
        "this_is_true": True,
        "my_number": 12312,
        "my_list": [312, 456, 789, "Abc", 3123]
    }

    return render(request, 'about.html', my_context)