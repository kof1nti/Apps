from django.contrib import admin
#from django.contrib.gis.admin import OSMGeoAdmin
from .models import Incidences,gm
from leaflet.admin import LeafletGeoAdminMixin
from leaflet_admin_list.admin import LeafletAdminListMixin
# Register your models here.

#class IncidencesAdmin(LeafletGeoAdminMixin):
class IncidencesAdmin(LeafletAdminListMixin, LeafletGeoAdminMixin, admin.ModelAdmin):

	list_display = ('name','location')


admin.site.register(Incidences, IncidencesAdmin)


class gmAdmin(LeafletAdminListMixin, LeafletGeoAdminMixin, admin.ModelAdmin):

	list_display = ('name','location')

admin.site.register(gm, gmAdmin)
