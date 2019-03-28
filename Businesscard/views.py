from django.shortcuts import render
from bc.models import Businesscard

def index(request):
    datas = Businesscard.objects.all()
    context = {
        'datas': datas,
    }

    return render(request, 'Businesscard/index.html', context)