"""Platzigram Views"""

# Django
from django.http import HttpResponse, JsonResponse

# Utilities
from datetime import datetime

def hello_world(request):
    """Return a greeting"""
    return HttpResponse('Hello, world! Current server time is {now}'.format(
        now=datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
        ))

def sorted_numbers(request):
    """Return JSON response with a List of sorted numbers"""
    # import pdb; pdb.set_trace()
    numbers = sorted(map(int, request.GET['numbers'].split(',')))
    return JsonResponse({'sorted_numbers': numbers})
    
def say_hi(request, name, age):
    """Return a greeting"""
    if age < 12:
        message = f"Sorry {name} you are not allowed here."
    else:
        message = f'Hola {name}! Welcome to platzigram'
    return HttpResponse(message)