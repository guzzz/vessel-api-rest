from django.contrib import admin

from .models import Equipment


def activate(modeladmin, request, queryset):
	queryset.update(status='active')
activate.short_description = "Activate selected equipments"


def inactivate(modeladmin, request, queryset):
	queryset.update(status='inactive')
inactivate.short_description = "Inactivate selected equipments"


class EquipmentAdmin(admin.ModelAdmin):
	list_display = ('code','status','name','vessel')
	list_filter = ('status',)
	search_fields = ('code',)
	actions = [activate, inactivate]

	class Media:
		js = ('js/admin/custom_admin.js',)

admin.site.register(Equipment, EquipmentAdmin)

