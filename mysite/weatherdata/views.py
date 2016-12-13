from django.http import HttpResponse
from django.template import loader
from .models import Post, Weather


def index(request):
    template = loader.get_template('weatherdata/template.html')
    context={
        'general': Post.objects.all(),
        'weather_data': Weather.objects.all(),
    }    
    return HttpResponse(template.render(context,request))
