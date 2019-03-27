from django.shortcuts import render
from bc.models import Businesscard

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
    context = {
        'datas': datas
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
    srch = request.GET.get('search')
    info = request.GET.get('info')
    if srch == 'company_name':
        datas = Businesscard.objects.get(company_name=info)
    elif srch == 'position':
        datas = Businesscard.objects.get(position=info)
    elif srch == 'name':
        datas = Businesscard.objects.get(name=info)
    elif srch == 'company_addr':
        datas = Businesscard.objects.get(company_addr=info)
    elif srch == 'mobile':
        datas = Businesscard.objects.get(mobile=info)
    elif srch == 'email':
        datas = Businesscard.objects.get(email=info)
    elif srch == 'site_addr':
        datas = Businesscard.objects.get(site_addr=info)
        
    context = {
        'datas': datas
    }
    return render(request, 'bc/listone.html', context)