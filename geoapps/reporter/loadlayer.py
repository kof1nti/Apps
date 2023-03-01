import os
from django.contrib.gis.utils import LayerMapping
from .models import Incidences,gm

gm_mapping = {
    'name': 'name',
    'location': 'location',
    'geom': 'MULTIPOLYGON',
}

#gm_shp = os.path.dirname(os.path.dirname(os.path.abspath(__file__),'data/gama2.shp'))
gm_shp = os.path.abspath(os.path.join(os.path.dirname(__file__),'data/gama2.shp'))

def run(verbose=True):
	lm = LayerMapping(gm, gm_shp, gm_mapping, transform = False , encoding='utf-8')
	lm.save(strict=True, verbose=verbose)

