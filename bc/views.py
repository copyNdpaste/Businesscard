from django.shortcuts import render
from bc.models import Businesscard
from django.db.models import Q
from bc.forms import HTMLForm

# Create your views here.
def create(request):
    if request.method == "GET":
        return render(request, 'bc/create.html')
    elif request.method == "POST":
        bc = Businesscard()
        bc.company_name = request.POST.get('company_name')
        bc.position = request.POST.get('position')
        bc.name = request.POST.get('name')
        bc.company_addr = request.POST.get('company_addr')
        bc.mobile = request.POST.get('mobile')
        bc.email = request.POST.get('email')
        bc.site_addr = request.POST.get('site_addr')
        
        bc.save()

        datas = Businesscard.objects.all()

        context = {
            'datas': datas
        }

        return render(request, 'bc/list.html', context)
        
def list(request):
    datas = Businesscard.objects.all()
    form = HTMLForm()
    context = {
        'datas': datas,
        'form': form,
    }
    return render(request, 'bc/list.html', context)

def update(request):
    if request.method == 'GET':
        id = request.GET.get('id')
        data = Businesscard.objects.get(id=id)
        context = {
            'data': data
        }
        return render(request, 'bc/update.html', context)
    elif request.method == 'POST':
        bc = Businesscard()
        bc.company_name = request.POST.get('company_name')
        bc.position = request.POST.get('position')
        bc.name = request.POST.get('name')
        bc.company_addr = request.POST.get('company_addr')
        bc.mobile = request.POST.get('mobile')
        bc.email = request.POST.get('email')
        bc.site_addr = request.POST.get('site_addr')
        
        bc.save()

        datas = Businesscard.objects.all()
        context = {
            'datas': datas
        }
        return render(request, 'bc/list.html', context)

def delete(request):
    id = request.GET.get('id')
    datas = Businesscard.objects.all()
    data = Businesscard.objects.get(id=id)
    data.delete()
    context = {
        'datas': datas
    }
    return render(request, 'bc/list.html', context)

def search(request):
    info = request.GET.get('info')

    datas = Businesscard.objects.filter(
            Q(company_name__icontains=info) |
            Q(position__icontains=info) |
            Q(company_name__icontains=info) |
            Q(company_addr__icontains=info) |
            Q(mobile__icontains=info) |
            Q(email__icontains=info) |
            Q(site_addr__icontains=info)
        ).distinct()

    context = {
        'datas': datas
    }
    return render(request, 'bc/listresults.html', context)