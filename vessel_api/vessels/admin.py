from django.contrib import admin

from .models import Vessel


class VesselAdmin(admin.ModelAdmin):
	search_fields = ('code',)

	class Media:
		js = ('js/admin/custom_admin.js',)

admin.site.register(Vessel, VesselAdmin)
