
#from django.urls import include,url 
from django.urls import re_path as url
from reporter.views import HomepageView
from djgeojson.views import (
    GeoJSONLayerView, TiledGeoJSONLayerView,
)
from django.views.generic import TemplateView
from reporter.views import gm_datasets



urlpatterns = [
	url(r'^$', HomepageView.as_view(), name= 'home'),
	url(r'^gm_data/$', gm_datasets, name= 'name'),
	url(r'^incidence_data/$', HomepageView.as_view(), name= 'home'),
	#url(r'^$', TemplateView.as_view(template_name='index.html'), name='home'),
	#url(r'^data.geojson$', GeoJSONLayerView.as_view(model=gm), name='name'),

]



#from django.urls import re_path as url
#from django.urls import include, re_path

#from views import HomepageView
#from django.urls import path , re_path



#from django.urls import include, re_path
#from myapp.views import home

#urlpatterns = [
    #re_path(r'^$', home, name='home'),
    #re_path(r'^reporter/', include('reporter.urls'),


#]


#from django.contrib import admin
#from django.urls import include, path

#urlpatterns = [
    #path('members/', include('members.urls')),
    #path('admin/', admin.site.urls),
#]


#from django.urls import path
#from.import views

#urlpatterns = [
#path('', home_view, name='home'),
#path('', HomepageView.as_view(), name= 'home'),
#path('', views.index, name='index'),
#]