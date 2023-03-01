
from django.db import models
from django.contrib.gis.db import models
#from django.db.models import Manager as GeoManager
#from django.contrib.gis.db.models.functions import Length
#from django.contrib.gis.db.models.manager import GeoManager
#from django.db.models.manager import Manager
from django.db.models import Manager as GeoManager

# Create your models here.
class Incidences(models.Model):
    name = models.CharField(max_length=20)
    location = models.PointField(srid=4326)
    #location= models.PointField(srid=4326,default='SRID=3857;POINT(0.0 0.0)')
    #objects = models.Geomanager()
    #objects = models.Geomanager()

    def __unicode__(self):
    	return self.name

    class Meta:
    	verbose_name_plural= " Incidences"

class gm(models.Model):
    name = models.CharField(max_length=50)
    location = models.FloatField(blank=True, null=True)
    geom = models.MultiPolygonField(srid=4326)


    def __unicode__(self):
    	return self.gm