

from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render

#docs
from .models import DocsLinux

def index(request):
    print('aaaa')
    #latest_question_list = DocsLinux.objects.order_by('id')[:5]
    context = {'latest_question_list': 'aaaaaaaaaaaa'}
    #return render(request, 'polls/index.html', context)

# ...
#def detail(request, ppk_id):
#    print(ppk_id)
#    try:
#        question = DocsLinux.objects.get(pk=ppk_id)
#    except Question.DoesNotExist:
#        raise Http404("Question does not exist")
#    return render(request, 'docs/detail.html', {'question': question})