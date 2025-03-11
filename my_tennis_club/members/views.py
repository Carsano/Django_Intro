from django.template import loader
from django.http import HttpResponse


def members(request):
    template = loader.get('myfirst.html')
    return HttpResponse(template.render())
