from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.serializers import serialize
#from django.http import HttpResponse
from djgeojson.views import GeoJSONLayerView
from .models import gm


class HomepageView(TemplateView):
	template_name = 'index.html'


def gm_datasets(request):
	Gm = serialize('geojson', gm.objects.all(),geometry_field='geom', fields=('name',))
	return HttpResponse(Gm,content_type='json')

#from django.shortcuts import render
#from django.http import HttpResponse

#def index(request):
    #return HttpResponse("<h1>Welcome to geoapps portal</h1>")
    #return render(request,'index.html')
# Create your views here.
