from django.shortcuts import render
from bc.models import Businesscard

def index(request):
    data = Businesscard.objects.get(id=9)
    context = {
        'data': data,
    }

    return render(request, 'Businesscard/index.html', context)