from django.contrib import admin

from main.models import Vehicle


class VehicleAdmin(admin.ModelAdmin):
    list_display = ["brand", "model", "year_of_manufacture", "registration_number"]


admin.site.register(Vehicle, VehicleAdmin)
