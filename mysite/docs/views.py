

from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.http import Http404


# Create your views here.
from .models import DocsLinux

from django.urls import reverse
from django.views import generic

import logging

def index(request):
    #alldata = DocsLinux.objects.all()[:200]
    alldata = DocsLinux.objects.all()
    
    #datadict = {}
    #for val in alldata:
    #if val.ptit not in datadict.keys():
    #    datadict[val.ptit] = (val,)
    #else:
    #    pass
    #    #datadict[val.ptit].append(val)
    
    #return render(request, 'polls/index.html', context)
    #return HttpResponse("Hello,kiwi world. You're at the polls index.")
    return render(request, 'docs/index.html', {'context': alldata})
    
    
#def detail(request):
#    return HttpResponse("Hello, daaaaa You're at the polls index.")
    

def detail(request, ppk_id):
    #infos = get_object_or_404(DocsLinux, pk=ppk_id)
    #return render(request, 'docs/detail.html', {'infos': infos})
    dd = DocsLinux.objects.get(pk=ppk_id)
    return render(request, 'docs/detail.html', {'infos': dd})
    
#class DetailView(generic.DetailView):
#    model = DocsLinux
#    template_name = 'docs/detail.html'