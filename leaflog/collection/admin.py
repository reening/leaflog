from django.contrib import admin

from .models import Location, Taxon


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    pass


@admin.register(Taxon)
class TaxonAdmin(admin.ModelAdmin):
    pass
